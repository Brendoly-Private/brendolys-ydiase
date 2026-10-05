# Gates et inconnues — Compétences et connaissances

Statut : `DOMAIN-REVIEW-CANDIDATE`

| Gate | SKL-001 | SKL-002 |
|---|---|---|
| ownership | DEFINED | DEFINED |
| séparation taxonomie/profil individuel | DEFINED | DEFINED |
| provenance | DEFINED | DEFINED |
| IA non autoritative | DEFINED | DEFINED |
| contrats EDU/CAR/PRF/ASM | LOGICAL-DEFINED | LOGICAL-DEFINED |
| gouvernance taxonomique | TBD-PREPROD | N/A |
| modèle de niveau/proficiency | référence canonique versionnée | **DEFINED** |
| niveau vs confiance vs fraîcheur | N/A | **DEFINED** |
| modèle de SkillEvidence | N/A | **DEFINED** |
| règles de dérivation UserSkill | N/A | **DEFINED-SEMANTIC** |
| correction/révocation/historique | N/A | **DEFINED** |
| contradiction | N/A | **DEFINED** |
| politique d'inférence | IA non autoritative | **DEFINED** |
| coefficients/seuils de dérivation | N/A | TBD-VALIDATION |
| durées de fraîcheur | N/A | TBD-VALIDATION |
| Privacy/finalités/rétention | standard catalogue | TBD-BLOCKING-BEFORE-ACTIVE |
| contrôle d'accès horizontal | N/A | TBD-BLOCKING-BEFORE-ACTIVE |
| RPO/RTO/SLO | TBD-PREPROD C2 | TBD-BIA/PREPROD C1 |
| restore indépendant | TBD-PREPROD | TBD-PREPROD C1 |
| IAM physique | TBD-PREPROD | TBD-PREPROD |
| contrats physiques | TBD-PREPROD | TBD-PREPROD |

## Décision SKL-002

La sémantique de dérivation est définie dans `../13-architecture/microservices/YD-MS-SKL-002/SKILL_STATE_DERIVATION_POLICY.md`.

Un UserSkill est un état versionné et reproductible. Le niveau, la confiance et la fraîcheur sont indépendants. Les preuves sont historisées ; corrections et révocations produisent de nouvelles versions au lieu d'écraser l'historique.

Les paramètres numériques ne sont volontairement pas inventés : coefficients, seuils et durées doivent être validés avec des données et critères métier/psychométriques adaptés.

## Profondeur

SKL-001 suit le profil C2.

SKL-002 est C1. Avant production : BIA, RPO/RTO, backup/restore, tests d'accès horizontal, Privacy et restauration indépendante restent obligatoires.

La sémantique n'est plus bloquante pour poursuivre l'architecture. Les paramètres numériques et Privacy restent des gates avant activation.

Statut : `DOMAIN-BASELINE-CANDIDATE / SKL-002-SEMANTICS-DEFINED`.
