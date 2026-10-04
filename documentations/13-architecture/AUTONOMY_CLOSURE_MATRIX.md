# D3 Autonomy Closure Matrix — BRENDOLYS YDIASE

Statut : `D3-closure-in-progress`

## 1. Objet

Cette matrice pilote la fermeture documentaire des 47 microservices métier et 4 composants de plateforme avant le Contract Registry. Elle ne remplace pas les `AUTONOMY_PROFILE.md` : elle indique ce qui est déjà décidé, ce qui doit être fermé avant le Contract Registry, ce qui peut attendre le gate préproduction et ce qui exige une ADR.

## 2. Statuts normatifs

- `DEFINED` : décision présente et exploitable.
- `TBD-BLOCKING` : information absente qui empêche de figer un contrat ou une frontière.
- `TBD-PREPROD` : information obligatoire avant `ready-for-production`, mais qui n'empêche pas la poursuite de D3.
- `ADR-REQUIRED` : choix d'architecture qui ne doit pas être inventé dans le profil.
- `NOT-APPLICABLE` : champ non applicable, avec justification.

Un simple `TBD` non qualifié est interdit dans la closure finale.

## 3. Blocs contrôlés

`OWN` ownership; `DATA` autorité/classification/datastore; `REC` backup/restore ou rebuild; `IAM` realms/audience/scopes; `CTR` API/events/projections; `NET` DNS/flux/secrets/certificats; `OBS` logs/métriques/traces/health; `REL` criticité/SLO/RPO/RTO/mode dégradé; `DEP` CI/CD/scaling/rollback; `OPS` runbook/DR/rétention/decommission.

## 4. Matrice des 47 microservices métier

| Boundary | Nature | Crit. | OWN | DATA | REC | IAM | CTR | NET | OBS | REL | DEP | OPS | Blocage D3 principal |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| YD-MS-PRF-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-BLOCKING | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | audience/scopes PRF |
| YD-MS-EDU-001 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage de frontière |
| YD-MS-EDU-002 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage de frontière |
| YD-MS-EDU-003 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage de frontière |
| YD-MS-EDU-004 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage de frontière |
| YD-MS-SKL-001 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage de frontière |
| YD-MS-SKL-002 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | privacy/scopes avant prod |
| YD-MS-CAR-001 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage de frontière |
| YD-MS-CAR-002 | MIXED | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | séparer AUTH/DERIVED avant prod |
| YD-MS-ASM-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-ORI-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-REC-001 | MIXED | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | module RSH reste non autoritatif |
| YD-MS-SRH-001 | DERIVED | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | TBD-BLOCKING | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | contrats/versions/rétention sources |
| YD-MS-LAB-001 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-LAB-002 | MIXED | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | méthodologies autoritatives à isoler |
| YD-MS-OPP-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-OPP-002 | MIXED | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-APP-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | contrats candidature à figer |
| YD-MS-EMP-001 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-EMP-002 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-CNT-001 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | contrats MOD à figer |
| YD-MS-CNT-002 | DERIVED | C3 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | TBD-BLOCKING | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | contrats/versions/rétention sources |
| YD-MS-COM-001 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | contrats MOD à figer |
| YD-MS-LRN-001 | MIXED | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | séparer ressources propres/projections |
| YD-MS-NTF-001 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | provider/retention avant prod |
| YD-MS-PRT-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-AMB-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | mandat/scopes à figer |
| YD-MS-DAT-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-DAT-002 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | raw retention à fixer avant prod |
| YD-MS-DAT-003 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-DAT-004 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-DAT-005 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-KNW-001 | DERIVED | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | TBD-BLOCKING | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | contrats/versions/rétention sources |
| YD-MS-ANL-001 | DERIVED | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | TBD-BLOCKING | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | contrats/versions/rétention sources |
| YD-MS-ANL-002 | MIXED | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | entitlement contract à figer |
| YD-MS-ANL-003 | MIXED | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | entitlement contract à figer |
| YD-MS-AI-002 | DERIVED | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | TBD-BLOCKING | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | corpus/contracts/rétention sources |
| YD-MS-AI-003 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | preuve/règles de vérification à figer |
| YD-MS-BIL-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | contrats entitlement structurants |
| YD-MS-BIL-002 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | provider/ledger/idempotence à figer |
| YD-MS-MKT-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | contrats order/billing à figer |
| YD-MS-SPN-001 | AUTH | C2 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | séparation ranking organique maintenue |
| YD-MS-DPR-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | TBD-BLOCKING | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | licence + privacy/agrégation |
| YD-MS-INT-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | evidence contract à figer |
| YD-MS-MOD-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | ownership fonctionnel défini; personnes avant prod |
| YD-MS-CFG-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | aucun blocage D3 |
| YD-MS-CNS-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | purpose/scopes propagation à figer |

## 5. Matrice des 4 composants plateforme

| Boundary | Nature | Crit. | OWN | DATA | REC | IAM | CTR | NET | OBS | REL | DEP | OPS | Écart plateforme à fermer |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| YD-PLT-AI-001 | MIXED | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-BLOCKING | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | policies/routing metadata séparés de toute vérité métier; audiences par use case |
| YD-PLT-MLP-001 | AUTH | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | artefact/model storage et approval chain à figer |
| YD-PLT-API-001 | MIXED | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-BLOCKING | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | client/audience/scope/entitlement model à figer |
| YD-PLT-AUD-001 | AUTH append-only | C1 | TBD-PREPROD | DEFINED | TBD-PREPROD | TBD-PREPROD | DEFINED | ADR-REQUIRED | TBD-PREPROD | TBD-PREPROD | ADR-REQUIRED | TBD-PREPROD | ingestion contract + retention/immutability à figer |

## 6. Blocages avant Contract Registry

Le Contract Registry peut être construit comme registre candidat, mais il ne peut pas être déclaré stable tant que les éléments suivants ne sont pas traités dans les contrats correspondants :

1. `PRF-IAM` : audiences, scopes et claims minimaux de Profile.
2. `DPR-LICENSING` : droits/licences attachés aux Data Products.
3. `DPR-PRIVACY-AGGREGATION` : règles de privacy, anonymisation/agrégation et statut distribuable.
4. `DERIVED-SOURCE-CONTRACTS` : contrats/versions, rétention et replay des sources des cinq DERIVED purs.
5. `PLT-AI-IAM` : audiences et politiques d'accès de AI Gateway par cas d'usage.
6. `PLT-API-IAM` : modèle clients API, audiences, scopes et relation avec Entitlement.

Ces points sont `TBD-BLOCKING` pour la stabilisation des contrats concernés, pas pour la poursuite de la documentation D3.

## 7. ADR transversales requises

Les choix suivants restent volontairement `ADR-REQUIRED` pour les 51 frontières : runtime cible; moteur(s) de datastore; stratégie de workload identity; gestionnaire de secrets/certificats; convention DNS physique; mécanisme de policy réseau; plateforme d'observabilité; stratégie de déploiement; autoscaling; broker/transport physique lorsque nécessaire.

Ces ADR peuvent produire des standards communs, mais chaque frontière garde credentials, namespace, policies, quotas, cycle de déploiement et responsabilité propres.

## 8. Gates préproduction communs

Avant `ready-for-production`, chaque frontière doit fermer : owners et suppléants; artefact; runtime; datastore/migrations; classification détaillée; backup/restore ou rebuild; dernier test; RPO/RTO/SLO; IAM complet; secrets/certificats; flux réseau; observabilité; health; quotas; scaling; rollback; runbook; incident owner; DR; rétention/suppression; decommission.

Pour les cinq DERIVED purs, `REBUILDABLE` et un `FULL_REBUILD` réussi sont obligatoires.

## 9. Verdict D3

- Frontières physiques : `STABLE-CANDIDATE`.
- 51 profils présents : oui.
- Données/autorité principales : suffisamment définies pour continuer D3.
- Autonomie opérationnelle : incomplète; fermeture préproduction obligatoire.
- Contract Registry : autorisé en `candidate`, interdit en `stable` tant que les six familles de blocages de la section 6 ne sont pas fermées.
