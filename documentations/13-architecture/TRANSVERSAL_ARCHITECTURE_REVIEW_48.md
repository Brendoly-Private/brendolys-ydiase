# Revue transversale d'architecture — 48 microservices BRENDOLYS YDIASE

Statut : `TRANSVERSAL-REVIEW-COMPLETE / REMEDIATION-TRACKED`
Périmètre : 48 microservices métier physiques. Les 4 composants plateforme et frontières LOGICAL/DEFERRED sont contrôlés lorsqu'ils affectent ces 48.

## 1. Références canoniques

La revue croise :
- `MICROSERVICE_BOUNDARY_REVIEW.md`
- `AUTONOMY_PROFILE_REGISTER.md` + 48 profils
- `DATA_OWNERSHIP_MATRIX.md`
- `DEPENDENCY_MAP.md`
- `EVENT_MAP.md`
- `DERIVED_RECOVERY_REGISTER.md`
- `DDD_REVIEW.md`
- politiques/phase closures déjà établies.

En cas de divergence historique, Boundary Review + ADR actifs déterminent la frontière physique.

## 2. Inventaire vérifié

- 48 microservices métier : CONFIRMÉ.
- Nature : 36 AUTH, 7 MIXED, 5 DERIVED.
- Criticité candidate : 23 C1, 24 C2, 1 C3.
- DERIVED purs : SRH-001, CNT-002, KNW-001, ANL-001, AI-002.
- Tous les 48 possèdent un `AUTONOMY_PROFILE.md`.
- 4 composants plateforme autonomes restent hors comptage métier.
- BRENDOLYS Identity reste plateforme externe.
- CAR-004, LAB-003 et AI-004 restent DEFERRED.

## 3. Verdict autorité / ownership

### PASS
Les frontières majeures déjà fermées ne présentent pas de duplication autoritative connue :
- PRF-001 ≠ PRF-002 ;
- EDU-001/002/003/004 protégés ;
- SKL-001 ≠ SKL-002 ;
- CAR-001 ≠ CAR-002 ;
- ASM ≠ ORI ≠ REC ;
- LAB-001 ≠ LAB-002 ;
- OPP-001 ≠ OPP-002 ≠ APP-001 ≠ EMP-002 ;
- DAT-001/002/003/004/005 séparés ;
- LRN ne possède ni Program EDU, ni Skill SKL, ni offre MKT ;
- KNW/SRH ne deviennent pas sources métier ;
- BIL-001 ≠ BIL-002 ;
- SPN reste isolé des scores organiques ;
- CNS/CFG/MOD/AUD gardent leurs autorités transversales.

### Remédiations documentaires appliquées
- REC-002 est désormais explicitement SUPERSEDED dans les vues historiques concernées ; APP-001 est canonique.
- INS-001 et EMP-003 sont alignés comme BFF/logical-only sans datastore/agrégat métier propre.
- ADM-001 reste admin plane sans ownership des objets administrés.

## 4. Dépendances et cycles

Six relations bidirectionnelles documentées restent acceptables uniquement sous leur pattern anti-cycle :
1. EDU-002 ↔ EDU-003 : ref + événement CurriculumPublished.
2. SKL-001 ↔ CAR-001 : projection Skill + evidence events.
3. ORI-001 ↔ REC-001 : request/job + résultat corrélé immuable.
4. MOD-001 ↔ domaines : demande/objet + décision ; aucune écriture DB croisée.
5. BIL-001 ↔ API-001 : entitlement commercial distinct du rate-limit technique.
6. PRT-001 ↔ DAT-001 : accord juridique PRT distinct de traduction opérationnelle DAT.

Verdict : `NO-REQUIRED-SYNCHRONOUS-A→B→A-CYCLE-KNOWN`.

Gate : le futur Contract Registry doit permettre un contrôle automatisé des cycles synchrones.

## 5. Événements

### PASS structurel
- owner de schéma explicite ;
- version/idempotence/retry présents au niveau D3 ;
- ordre global non supposé ;
- aggregate version utilisée lorsque nécessaire ;
- événements personnels minimisés ;
- priorité prévue pour consent/revocation, modération bloquante, retrait modèle et expiration opportunité ;
- replay interdit de répéter aveuglément paiements/messages/décisions/commandes admin.

### Dette à corriger dans le Contract Registry
- `ORI-002` apparaît encore comme producteur logique dans certains événements alors qu'il est module de ORI-001 : acceptable sémantiquement, mais le producteur physique doit être `YD-MS-ORI-001`.
- `INS-001`, `EMP-003`, `ADM-001` peuvent conserver des noms logiques de contrats/events, mais l'identité workload/producteur physique doit être celle du BFF/admin plane défini.
- AI-004 apparaît dans la topologie cible alors qu'il est DEFERRED : les contrats doivent porter `FUTURE/DEFERRED` tant qu'aucun ADR ne l'extrait.
- paramètres numériques de propagation, rétention, payload et compatibilité restent PREPROD.

## 6. Frontières DDD

### Confirmées
Les 48 frontières du Boundary Review sont cohérentes avec les besoins d'autonomie actuels.

### Décisions historiques réconciliées
La DDD Review initiale contenait des classifications antérieures à la Boundary Review. Elle est maintenant annotée comme historique pour :
CAR-002, OPP-002, LRN-001, AI-002, AI-003 et REC-002.

### Frontières à surveiller
- INS-001 : rester BFF seulement tant qu'il n'acquiert pas workflow durable/autorité propre.
- EMP-003 : rester BFF ; aucune DB métier.
- RSH-001 : reste module REC tant qu'il n'acquiert pas autorité académique/cycle autonome.
- LAB-003 : forecasting reste dans LAB-002 tant que modèle/lifecycle/SLO propres ne justifient pas extraction.
- CAR-004 : simulation reste capacité CAR-002 jusqu'au trigger ADR.
- AI-004 : orchestration reste capacité logique/plateforme minimale jusqu'au trigger ADR.

## 7. Criticité C1/C2/C3

Distribution : 23 C1 / 24 C2 / 1 C3.

Verdict : `COHERENT-AS-CANDIDATE`, pas encore exploitation-validé.

Points de vigilance :
- C1 : PRF, SKL individuel, ASM/ORI/REC, OPP-001, APP/EMP-002, droits/provenance/validation, AI verification, billing/entitlement, marketplace, data/intelligence products, moderation, CFG/CNS.
- C2 : catalogues et services reconstruisibles/analytique ou moins transactionnels.
- CNT-002 Feed reste seul C3, cohérent avec sa nature DERIVED et dégradation acceptable.

Aucun changement de classe n'est imposé par cette revue. Les BIA/SLO/RPO/RTO peuvent encore provoquer un ADR de reclassement.

## 8. DERIVED

5 purs : SRH-001, CNT-002, KNW-001, ANL-001, AI-002.

Invariants PASS :
- aucune autorité primaire ;
- sources candidates identifiées ;
- watermark/replay/snapshot requis ;
- delete/revoke représentables ;
- FULL/PARTIAL/CATCH_UP requis ;
- fraîcheur explicite.

État : les 5 restent `REBUILD-UNVERIFIED`.

Conséquence : aucun des cinq ne doit passer production avant FULL_REBUILD réussi, convergence vérifiée et compatibilité rétention/snapshot prouvée.

## 9. Doublons / collisions

Aucune collision autoritative bloquante connue après réconciliation.

Doublons intentionnels autorisés :
- projections locales minimales ;
- snapshots immuables nécessaires à une décision/run ;
- index Search/Graph/Analytics/AI reconstructibles ;
- vues BFF sans ownership métier.

Interdits :
- statut Application concurrent hors APP ;
- Skill individuel concurrent hors SKL-002 ;
- Program concurrent hors EDU ;
- Opportunity concurrent hors OPP-001 ;
- pays/configuration concurrent hors CFG ;
- consent/purpose concurrent hors CNS ;
- ranking organique influencé par SPN ;
- vérité métier créée par KNW/SRH/ANL/AI.

## 10. Risques ouverts classés

### R1 — REMEDIATED-D3 — Contract Registry canonique matérialisé
`CONTRACT_REGISTRY.md` centralise désormais IDs, owners/consumers, types, autorité, données minimales, Privacy, idempotence, replay, compatibilité et criticité. Restent HIGH pour préproduction : schémas physiques, contract tests, SLO et preuves de replay/rebuild.

### R2 — HIGH — DERIVED non reconstruits
5/5 sont REBUILD-UNVERIFIED.

### R3 — HIGH — domaines non encore fermés sémantiquement en profondeur
Analytics/AI, Content/Community/Moderation, Billing/Marketplace/Sponsoring, Partner/Ambassador, Notification, Data/Intelligence Products restent à auditer/fermer selon priorité produit.

### R4 — MEDIUM — topologie logique vs physique
ORI-002, BFF/admin-plane et AI-004 doivent être matérialisés avec identité physique correcte dans Contract Registry.

### R5 — MEDIUM — valeurs exploitation
RPO/RTO/SLO, freshness, retention et propagation restent largement TBD-PREPROD.

### R6 — MEDIUM — sécurité dynamique
IAM/IDOR/tenant, revocation propagation et purpose enforcement doivent être prouvés par tests, pas seulement documentation.

## 11. Ordre recommandé après revue

1. Fermer `ANL-001` avant ANL-002/003 en s'appuyant sur `CONTRACT_REGISTRY.md`.
2. Fermer AI-002 puis AI-003 et réconcilier le rôle de AI Gateway/AI-004 deferred.
3. Fermer Content/Community/Moderation si ces surfaces entrent dans le pilote.
4. Fermer économie : BIL/MKT/SPN avant monétisation.
5. Matérialiser progressivement les schémas physiques et contract tests des contrats activés au pilote.
6. Exécuter les plans de FULL_REBUILD des 5 DERIVED à l'approche de la préproduction.

## 12. Verdict global

`ARCHITECTURE-COHERENT-WITH-REMEDIATIONS / NO-KNOWN-AUTHORITY-COLLISION / NO-REQUIRED-SYNC-CYCLE / PREPROD-NOT-READY`.

La cible de **48 microservices métier** reste valide. La revue ne justifie ni fusion globale ni création de nouveaux microservices à ce stade.

Le principal risque n'est plus le découpage DDD : il se déplace vers **la matérialisation des contrats, les preuves de reconstruction, les contrôles IAM/Privacy et les paramètres d'exploitation**.
