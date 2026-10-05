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
| modèle de niveau/proficiency | référence canonique à définir/versionner | TBD-BLOCKING-BEFORE-IMPLEMENTATION |
| règles de dérivation UserSkill | N/A | TBD-BLOCKING-BEFORE-IMPLEMENTATION |
| Privacy/finalités/rétention | standard catalogue | TBD-BLOCKING-BEFORE-ACTIVE |
| contrôle d'accès horizontal | N/A | TBD-BLOCKING-BEFORE-ACTIVE |
| RPO/RTO/SLO | TBD-PREPROD C2 | TBD-BIA/PREPROD C1 |
| restore indépendant | TBD-PREPROD | TBD-PREPROD C1 |
| IAM physique | TBD-PREPROD | TBD-PREPROD |
| contrats physiques | TBD-PREPROD | TBD-PREPROD |

## Inconnues critiques SKL-002

Avant implémentation de la logique de compétence individuelle, il faut décider :
1. comment un niveau est représenté sans confondre échelle canonique et score d'une source ;
2. quelles preuves peuvent créer, augmenter, diminuer, expirer ou invalider un UserSkill ;
3. comment sont conservées confiance, fraîcheur, provenance et méthode ;
4. quelles inférences sont automatiques, révisables ou soumises à validation ;
5. comment une correction PRF-002 ou ASM se propage sans réécrire l'historique de façon opaque.

Ces inconnues ne bloquent pas la documentation des autres domaines, mais bloquent l'implémentation correcte de SKL-002.

## Profondeur

SKL-001 suit le profil C2.

SKL-002 est C1. Avant production, une BIA, des objectifs RPO/RTO, une politique backup/restore, des tests d'accès horizontal, Privacy et restauration indépendante seront obligatoires. Leur détail doit être produit au moment où les règles de dérivation et l'implémentation sont suffisamment stables pour être testables.

Statut : `DOMAIN-BASELINE-CANDIDATE / SKL-002-IMPLEMENTATION-GATES-OPEN`.
