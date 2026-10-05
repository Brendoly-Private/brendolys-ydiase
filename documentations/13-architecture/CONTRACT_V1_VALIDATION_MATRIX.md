# CONTRACT v1 — Validation Matrix

Statut : `VALIDATION-BASELINE-DEFINED / EXECUTION-PENDING`
Référence : `CONTRACT_REGISTRY.md`

## 1. But

Cette matrice définit les tests minimaux permettant de faire évoluer un contrat de `ACTIVE-LOGICAL` vers `PHYSICAL-READY`, et un contrat alimentant un service DERIVED vers `REBUILDABLE`.

Elle ne déclare aucun contrat validé tant que les preuves d'exécution ne sont pas enregistrées.

## 2. Priorités

### P0 — invariant de sécurité/cohérence
Bloque toute activation du contrat :
- schéma v1 et identité owner/consumer ;
- champs requis et compatibilité ;
- enum inconnu ;
- duplicate delivery/idempotence ;
- out-of-order/stale version ;
- DELETE/WITHDRAW/REVOKE/EXPIRE lorsqu'applicable ;
- Privacy/purpose/tenant lorsqu'applicable ;
- replay sans répéter un effet externe ;
- autorité source préservée.

### P1 — préproduction
- backward/forward compatibility ;
- snapshot + catch-up ;
- FULL_REBUILD pour DERIVED ;
- convergence ;
- producer/consumer contract tests ;
- quarantine/DLQ ou refus explicite ;
- reprise après indisponibilité consumer ;
- observabilité/correlation ;
- dépréciation/coexistence v1→vNext.

### P2 — exploitation
- replay massif ;
- mesure propagation/freshness/removal ;
- RTO/recovery mesuré ;
- capacity/backpressure ;
- chaos/restart ;
- rollback/version coexistence sous charge.

Aucun seuil numérique n'est fixé ici sans BIA/SLO/ADR.

## 3. Suite de tests canonique

| Test ID | Invariant | Attendu |
|---|---|---|
| V1-COMP-01 | ajout champ optionnel | consumer v1 continue |
| V1-COMP-02 | suppression/rename champ requis | CI/registry refuse |
| V1-COMP-03 | changement type/sémantique requis | nouvelle version majeure requise |
| V1-COMP-04 | enum inconnu | UNKNOWN/UNSUPPORTED, jamais interprétation positive |
| V1-COMP-05 | champ inconnu | ignoré ou conservé selon policy, sans crash |
| V1-COMP-06 | producer nouveau / consumer ancien | coexistence ou refus explicite |
| V1-IDEM-01 | même event/request livré N fois | un seul changement logique |
| V1-IDEM-02 | même version reçue N fois | état identique |
| V1-IDEM-03 | effet externe rejoué | aucun double paiement/envoi/commande/décision |
| V1-ORD-01 | v5→v7→v6 | v6 ne remplace pas v7 |
| V1-ORD-02 | DELETE/REVOKE v8 puis UPSERT v7 | objet non ressuscité |
| V1-ORD-03 | agrégats distincts entrelacés | aucune dépendance à ordre global |
| V1-REV-01 | revoke/withdraw/expire | propagation prioritaire et état final correct |
| V1-PRV-01 | purpose absent/invalide | fail closed si requis |
| V1-PRV-02 | révocation CNS puis replay | donnée interdite ne réapparaît pas |
| V1-PRV-03 | tenant/scope incorrect | aucune fuite inter-tenant/horizontale |
| V1-RPL-01 | replay complet | même état logique autorisé |
| V1-RPL-02 | snapshot + catch-up | convergence avec flux continu |
| V1-RPL-03 | replay d'une décision/run historique | restaure la décision, ne la recalcule pas |
| V1-RPL-04 | consumer indisponible puis reprise | catch-up sans perte ni double effet |
| V1-DRV-01 | FULL_REBUILD DERIVED | reconstruction depuis autorités/sources déclarées |
| V1-DRV-02 | rebuild sans source optionnelle | mode dégradé conforme au contrat |
| V1-DRV-03 | watermark | aucune lacune/rollback silencieux |
| V1-DRV-04 | delete/revoke pendant rebuild | état final respecte suppression/révocation |
| V1-CTR-01 | producer contract test | payload conforme au schéma v1 |
| V1-CTR-02 | consumer contract test | toutes variantes v1 autorisées acceptées |
| V1-CTR-03 | payload incompatible | refus/quarantaine observable |
| V1-SEC-01 | secret/credential dans payload | test/CI bloque |
| V1-SEC-02 | minimisation | aucun champ personnel non nécessaire |
| V1-OBS-01 | correlation | contract/event/request/source version traçables |
| V1-DEP-01 | v1→vNext | dépréciation/coexistence/rollback démontrés |

## 4. Profils de validation

Les profils évitent de recopier 30 tests sur chaque ligne.

- `BASE` = COMP-01..06, IDEM-01..02, ORD-01/03, CTR-01..03, OBS-01, DEP-01.
- `K1-STATE` = BASE + IDEM-03 si effet, ORD-02, REV-01, RPL-01/04.
- `PRIV` = PRV-01..03 + SEC-01/02.
- `PROJ` = BASE + ORD-02 + REV-01 + RPL-01/02/04.
- `DECISION` = K1-STATE + RPL-03.
- `EFFECT` = K1-STATE + IDEM-03.
- `DERIVED` = PROJ + DRV-01..04.
- `FIN` = EFFECT + PRIV lorsque PII + provider transaction uniqueness.
- `PUBLIC-PROJ` = PROJ + SEC-01.

## 5. Matrice — contrats transversaux et personnels

| Contract | Profil | P0 spécifique | P1 spécifique | Gate |
|---|---|---|---|---|
| IDN-SUBJECT | K1-STATE+PRIV | disable/revoke account ne peut être annulé par ancien event | snapshot/catch-up | PHYSICAL-READY |
| CNS-PRIVACY-DECISION | K1-STATE+PRIV | NOT-DETERMINABLE≠ALLOW; revoke prioritaire | restore préserve ordre des revocations | PHYSICAL-READY |
| CFG-COUNTRY-CONFIG | PROJ | aucune valeur pays implicite; ancien config ne rollback pas nouveau | snapshot/catch-up multi-version | PHYSICAL-READY |
| AUD-GOVERNED-EVENT | BASE+PRIV | append-only; replay n'exécute pas l'action | audit continuity | PHYSICAL-READY |
| NTF-REQUEST | EFFECT+PRIV | même request_ref = pas double message | outage/retry provider | PHYSICAL-READY |
| NTF-DELIVERY | BASE+PRIV | attempts ne deviennent pas nouveaux sends | delivery reconciliation | PHYSICAL-READY |
| PRF-CURRENT-PROFILE | PROJ+PRIV | correction/version; revoke CNS retire accès | independent projection recovery | PHYSICAL-READY |
| PRF-HISTORY | PROJ+PRIV | historique non destructif; ancienne version ne remplace pas nouvelle | snapshot/catch-up | PHYSICAL-READY |
| SKL-USER-SKILLS | PROJ+PRIV | evidence correction non destructive; UNKNOWN non promu | replay evidence/version | PHYSICAL-READY |
| ASM-RESULT | DECISION+PRIV | replay restaure method/result version | correction history | PHYSICAL-READY |
| ORI-REC-REQUEST | K1-STATE+PRIV | duplicate request ne crée pas plusieurs runs logiquement concurrents | retry/correlation | PHYSICAL-READY |
| REC-ORI-RESULT | DECISION+PRIV | replay ne rerank pas avec modèle courant | evidence snapshot reproducibility | PHYSICAL-READY |
| REC-PROJECTION | PROJ+PRIV | ancienne run ne remplace pas current selection | rebuild projection | PHYSICAL-READY |
| OPP-MATCH-RESULT | DECISION+PRIV | replay ne rematche pas | input snapshot verification | PHYSICAL-READY |
| APP-APPLICATION | K1-STATE+PRIV | duplicate submit ≠ 2 applications; transitions monotones selon policy | concurrency/retry | PHYSICAL-READY |
| EMP-RECRUITMENT | DECISION+PRIV | décision duplicate/out-of-order contrôlée | audit/fairness trace | PHYSICAL-READY |
| ADMIN-COMMAND | EFFECT+PRIV | replay ne réexécute pas commande | target reconciliation | PHYSICAL-READY |

## 6. Matrice — référentiels, data et domaines

| Contract | Profil | P0 spécifique | P1 spécifique | Gate |
|---|---|---|---|---|
| EDU-INSTITUTION | PROJ | status/version owner EDU | snapshot/catch-up | PHYSICAL-READY |
| EDU-PROGRAM | PROJ | publication/version | snapshot/catch-up | PHYSICAL-READY |
| EDU-CURRICULUM | PROJ | curriculum version + relation Program sans cycle transactionnel | replay publication | PHYSICAL-READY |
| EDU-QUALIFICATION | PROJ | country/framework version conservée | snapshot/catch-up | PHYSICAL-READY |
| SKL-TAXONOMY | PROJ | mapping≠équivalence implicite | taxonomy migration test | PHYSICAL-READY |
| CAR-OCCUPATION | PROJ | requirements/version; country context | snapshot/catch-up | PHYSICAL-READY |
| CAR-TRANSITION | PROJ+PRIV | UNKNOWN≠MISSING; scenario assumptions versionnées | scenario replay | PHYSICAL-READY |
| EMP-EMPLOYER | PROJ | verification dimension/version | suspend/revoke catch-up | PHYSICAL-READY |
| OPP-OPPORTUNITY | K1-STATE | EXPIRE/WITHDRAW/SUSPEND priment ancien publish | APP current-state validation | PHYSICAL-READY |
| PRT-SOURCE-RIGHTS | K1-STATE | revoked/expired right ne renaît pas au replay | reconciliation DAT-001 | PHYSICAL-READY |
| DAT-SOURCE-POLICY | K1-STATE | NOT-DETERMINABLE fail closed acquisition | source policy restore | PHYSICAL-READY |
| DAT-ACQUISITION | BASE | même raw/hash/submission ne crée pas duplicat non gouverné | quarantine/retry | PHYSICAL-READY |
| DAT-PROVENANCE | PROJ | lineage append/version; preuve non réécrite | snapshot/replay | PHYSICAL-READY |
| DAT-QUALITY | DECISION | NOT-ASSESSABLE≠PASS; override versionné | decision replay | PHYSICAL-READY |
| DAT-REFERENCE | PROJ | mapping/version historique | snapshot/catch-up | PHYSICAL-READY |
| LAB-SIGNALS | PROJ | retraction; coverage/confidence conservés | replay observation→signal | PHYSICAL-READY |
| LAB-INTELLIGENCE | PROJ | methodology/version; revision non destructive | snapshot/catch-up | PHYSICAL-READY |
| CNT-CONTENT | PROJ | unpublish/moderation retire visibilité | snapshot/catch-up | PHYSICAL-READY |
| COM-ACTIVITY | BASE+PRIV | duplicate activity | replay/minimisation | PHYSICAL-READY |
| MOD-DECISION | DECISION+PRIV | blocking/revoke prioritaire | policy-version replay | PHYSICAL-READY |
| LRN-RESOURCE | PROJ | withdraw/retire; resource≠skill acquired | snapshot/catch-up | PHYSICAL-READY |
| AMB-SUBMISSION | BASE+PRIV | duplicate submission | retry/quarantine | PHYSICAL-READY |
| BFF-INSTITUTION-SUBMISSION | BASE+PRIV | BFF ne devient pas owner EDU | retry/quarantine | PHYSICAL-READY |

## 7. Matrice — DERIVED

| Derived service | Contrats sources à tester | P0 | P1 avant REBUILDABLE |
|---|---|---|---|
| SRH-001 | EDU/CAR/OPP/CNT/LRN-SEARCHABLE + KNW enrichment | delete/withdraw/expire/revoke; access filters; source version; KNW optionnel | FULL_REBUILD sans KNW → catch-up → enrichment → convergence |
| CNT-002 | CNT-FEEDABLE, COM-FEED-SIGNALS, MOD-CONTENT-DECISION, SPN-PLACEMENT | moderation/revoke prioritaire; sponsor n'altère pas organic rank | FULL_REBUILD + privacy/visibility convergence |
| KNW-001 | EDU/SKL/CAR/LAB-KNOWLEDGE | source asserted vs inferred; delete/revoke; provenance | FULL_REBUILD + graph/source watermarks + convergence |
| ANL-001 | YD-CTR-<DOMAIN>-ANALYTICS-v1 instances | purpose/grain/source version; delete/revoke selon métrique | registre concret des sources + FULL_REBUILD + metric convergence |
| AI-002 | SRH-RETRIEVAL, KNW-GROUNDING, CNS-CORPUS-AUTHORIZATION | fail closed Privacy; provenance; revoked corpus absent | corpus rebuild + grounding convergence + access tests |

Règle : aucun service ci-dessus ne quitte `REBUILD-UNVERIFIED` sur documentation seule.

## 8. Matrice — économie, produits et IA

| Contract | Profil | P0 spécifique | P1 spécifique | Gate |
|---|---|---|---|---|
| BIL-ENTITLEMENT | K1-STATE+PRIV | revoke entitlement prioritaire | reconciliation provider/subscription | PHYSICAL-READY |
| BIL-BILLING | FIN | provider transaction unique; replay zéro double charge | provider reconciliation | PHYSICAL-READY |
| MKT-ORDER | FIN | duplicate order/fulfillment interdit | billing/order reconciliation | PHYSICAL-READY |
| SPN-CAMPAIGN | K1-STATE | commercial state ne touche jamais organic score | isolation regression suite | PHYSICAL-READY |
| SPN-DELIVERY | EFFECT | duplicate delivery non double-billable | billing reconciliation | PHYSICAL-READY |
| API-USAGE | BASE | sequence/bucket dedupe | usage reconciliation | PHYSICAL-READY |
| DPR-RELEASE | K1-STATE | release immutable; revoke/suspend prioritaire | source snapshot reproducibility | PHYSICAL-READY |
| INT-EDITION | DECISION | édition historique non recalculée silencieusement | evidence snapshot replay | PHYSICAL-READY |
| MLP-MODEL-LIFECYCLE | K1-STATE | retired/unapproved model ne redevient pas active par event ancien | deployment reconciliation | PHYSICAL-READY |
| AI-GROUNDED-RETRIEVAL | K1-STATE+PRIV | unauthorized purpose/corpus fail closed | retrieval/corpus recovery | PHYSICAL-READY |
| AI-VERIFICATION | DECISION+PRIV | replay restaure verdict/version, ne reverifie pas silencieusement | evidence/run trace | PHYSICAL-READY |
| AI-ORCHESTRATION | — | aucun test d'activation tant que DEFERRED | ADR extraction requis | DEFERRED |

## 9. Contrats DEFERRED / SUPERSEDED

- `YD-CTR-LAB-FORECAST-v1` : tests de schéma possibles, aucune gate PHYSICAL-READY tant que LAB-003 reste DEFERRED.
- `YD-CTR-AI-ORCHESTRATION-v1` : idem tant que AI-004 reste DEFERRED.
- `YD-CTR-REC-002-*` : aucun test de compatibilité nouvelle ; toute nouvelle utilisation doit échouer au lint/CI.

## 10. Critères de passage ACTIVE-LOGICAL → PHYSICAL-READY

Un contrat est `PHYSICAL-READY` seulement si :
1. schéma machine-readable v1 existe ;
2. owner et consumers physiques sont résolus ;
3. P0 applicable = PASS ;
4. producer/consumer contract tests = PASS ;
5. Privacy/IAM/tenant tests applicables = PASS ;
6. idempotence/retry/quarantine = PASS ;
7. snapshot/replay applicable = PASS ;
8. compatibility v1 = PASS ;
9. SLO/freshness/removal nécessaire est approuvé ;
10. observabilité/correlation = PASS ;
11. rollback/deprecation procedure existe ;
12. preuves référencées dans le registre de validation.

`UNKNOWN`, `NOT-TESTED` ou `NOT-ASSESSABLE` sur un P0 applicable ≠ PASS.

## 11. Critères DERIVED-SOURCE → REBUILDABLE

En plus de PHYSICAL-READY pour les sources critiques :
1. snapshot ou replay window suffisante prouvée ;
2. watermarks compatibles ;
3. FULL_REBUILD exécuté ;
4. catch-up exécuté ;
5. duplicate/out-of-order testés ;
6. DELETE/WITHDRAW/REVOKE testés ;
7. Privacy revocation pendant rebuild testée si applicable ;
8. source optionnelle indisponible testée ;
9. convergence logique vérifiée ;
10. RTO de rebuild mesuré et validé par BIA/SLO.

## 12. Evidence Register

Chaque exécution future doit enregistrer :
`contract_id | schema_version | test_id | environment | producer_version | consumer_version | result | evidence_ref | executed_at | reviewer/approval_ref`.

Aucun nom de personne n'est imposé ici. Le mécanisme d'approbation sera défini avec la gouvernance CI/CD.

## 13. Ordre d'exécution recommandé

### Wave 0 — lint/registry
Tous les contrats : IDs uniques, owners, versions, privacy, no superseded usage.

### Wave 1 — P0 K1
CNS, IDN, PRF personnel, SKL-002, ASM/ORI/REC, OPP/APP/EMP-002, PRT/DAT rights-quality, MOD, BIL/MKT, DPR/INT, MLP/AI.

### Wave 2 — P0 DERIVED
SRH, CNT-002, KNW, ANL-001, AI-002.

### Wave 3 — P0/P1 K2
EDU/SKL taxonomy/CAR catalog/LAB/CNT/LRN/COM/NTF/AMB/API/SPN.

### Wave 4 — PREPROD
FULL_REBUILD, outage/catch-up, compatibility migration, SLO measurements, RTO.

## 14. Verdict

`CONTRACT-V1-VALIDATION-BASELINE-DEFINED / TEST-EXECUTION-PENDING`.

Cette matrice définit ce qu'il faut prouver. Elle ne transforme aucun contrat en `PHYSICAL-READY` et aucun service DERIVED en `REBUILDABLE` sans preuves d'exécution.
