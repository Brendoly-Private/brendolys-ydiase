# Gates et inconnues — Éducation et institutions

Statut : `DOMAIN-REVIEW-CANDIDATE`

## Gates

| Gate | État | Condition |
|---|---|---|
| frontières EDU-001..004 | DEFINED | ownership distinct |
| Institution vs Program | DEFINED | référence sans transfert d'ownership |
| Program vs Curriculum | DEFINED | pas de transaction distribuée |
| Program vs Qualification | DEFINED | QualificationRef gouvernée |
| Curriculum vs Skills | DEFINED | SKL-001 reste autorité |
| historique individuel | DEFINED | PRF-002 possède EducationRecord |
| multi-pays | DEFINED | contexte/version explicites, pas de règle continentale hardcodée |
| IA et équivalences | DEFINED | IA non autoritative |
| Country Framework Burkina | TBD-PREPROD | bindings/règles validés |
| workflows contribution/validation | TBD-PREPROD | rôles et séparation des fonctions |
| RPO/RTO/SLO | TBD-PREPROD | analyse par frontière C2 |
| rétention/versioning | TBD-PREPROD | politique par agrégat |
| contrats physiques | TBD-PREPROD | API/events/projections versionnés |
| IAM physique | TBD-PREPROD | clients/scopes/workload identities |
| restore tests | TBD-PREPROD | restauration indépendante démontrée |

## Inconnues acceptées

Datastores, protocoles physiques, runtime, formats d'événements, DNS, quotas/autoscaling, stockage des preuves et modèles physiques restent ouverts. Ils ne bloquent pas la baseline métier.

## Confrontations avant ACTIVE

À confronter avec Skills, Career, PRF-002, CFG, DAT, Search, Knowledge, Orientation et Recommendation.

## Profondeur documentaire

Les quatre frontières sont C2 AUTH. Backup/restore indépendant est obligatoire, mais la documentation C1 de PRF-002 n'est pas reproduite automatiquement. Une BIA/DR détaillée supplémentaire n'est créée que si criticité, réglementation, blast radius ou implémentation le justifie.

## Blocage

Aucun `TBD-BLOCKING` n'empêche de poursuivre.

Statut : `DOMAIN-BASELINE-CANDIDATE`.
