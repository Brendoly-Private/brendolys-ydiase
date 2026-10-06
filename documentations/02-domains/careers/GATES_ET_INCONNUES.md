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
| modèle de gap/transition | N/A | **DEFINED** | consommé |
| UNKNOWN vs MISSING | N/A | **DEFINED** | REQUIRED |
| blocking/required/preferred | N/A | **DEFINED** | REQUIRED |
| faisabilité | N/A | **DEFINED** | consommé |
| incertitude/explicabilité | provenance assertions | **DEFINED** | REQUIRED |
| reproductibilité | version/provenance | **DEFINED** | REQUIRED |
| coefficients/pondérations | N/A | TBD-VALIDATION | TBD-VALIDATION |
| biais/équité | N/A | TBD-VALIDATION | TBD-VALIDATION |
| Privacy/rétention snapshots | catalogue | TBD-BEFORE-ACTIVE | TBD-BEFORE-ACTIVE |
| RPO/RTO/SLO | TBD-PREPROD C2 | TBD-PREPROD C2 | selon frontière future |
| restore | TBD-PREPROD | TBD-PREPROD | selon frontière future |
| contrats physiques | TBD-PREPROD | TBD-PREPROD | TBD |

## Politique normative

Le calcul est défini dans `../../03-systems/policies/YD-MS-CAR-002/CAREER_GAP_TRANSITION_POLICY.md`.

Un gap est multidimensionnel. Aucun score global ne peut compenser un prérequis bloquant. `UNKNOWN` n'est jamais assimilé à `MISSING`. Une transition conserve entrées, versions, hypothèses, incertitude et explication.

## Décisions maintenues

Fusion physique CAR-002 + CAR-003 maintenue avec gate d'extraction. CAR-004 reste logique.

## Restant avant ACTIVE

Les coefficients, seuils, règles pays physiques, validation métier, tests de biais/équité, Privacy/rétention et preuves préproduction restent ouverts.

Statut : `DOMAIN-BASELINE-CANDIDATE / CAREER-TRANSITION-SEMANTICS-DEFINED`.
