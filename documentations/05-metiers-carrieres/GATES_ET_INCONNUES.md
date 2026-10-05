# Gates et inconnues — Métiers et carrières

Statut : `DOMAIN-REVIEW-CANDIDATE`

| Gate | CAR-001 | CAR-002 + CAR-003 | CAR-004 logique |
|---|---|---|---|
| ownership | DEFINED | DEFINED | DEFINED-LOGICAL |
| Skills ownership | DEFINED | via projections | via projections |
| faits vs inférences | DEFINED | DEFINED | DEFINED |
| input versions | applicable | REQUIRED | REQUIRED |
| fusion CAR-002/CAR-003 | N/A | VALIDATED-WITH-EXTRACTION-GATE | consommateur |
| modèle de preuve métier | TBD-VALIDATION | N/A | N/A |
| Country Framework | TBD-PREPROD | contexte requis | contexte requis |
| modèle de gap/transition | N/A | TBD-BEFORE-IMPLEMENTATION | consommé |
| incertitude/explicabilité | provenance assertions | TBD-BEFORE-ACTIVE | TBD-BEFORE-ACTIVE |
| Privacy/rétention snapshots | catalogue | TBD-BEFORE-ACTIVE | TBD-BEFORE-ACTIVE |
| RPO/RTO/SLO | TBD-PREPROD C2 | TBD-PREPROD C2 | selon frontière future |
| restore | TBD-PREPROD | TBD-PREPROD | selon frontière future |
| contrats physiques | TBD-PREPROD | TBD-PREPROD | TBD |

## Décisions maintenues

La fusion physique CAR-002 + CAR-003 reste valide conformément à `SENSITIVE_MERGER_REVIEW.md`. Une divergence durable de dataset, modèle, SLO, charge, équipe, Privacy/rétention ou cycle de déploiement déclenche un ADR.

CAR-004 reste logique : son existence dans les services D2 n'autorise pas à créer silencieusement un nouveau microservice.

## Blocages

Aucun blocage n'empêche de poursuivre l'architecture des autres domaines.

Avant implémentation personnalisée de CAR-002/003, le modèle de gap/transition et les règles d'incertitude/explication doivent être fermés. Avant ACTIVE, Privacy/rétention et contrats physiques doivent être validés.

Statut : `DOMAIN-BASELINE-CANDIDATE`.
