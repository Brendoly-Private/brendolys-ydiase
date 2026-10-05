# K2 — Preuve de catalogue Education

Statut : `draft / validation-required`

## Objectif

Tester la YDIASE Knowledge Architecture sur un vertical dont les frontières sont déjà documentées avant généralisation au dépôt.

## Périmètre

Le prototype enregistre :

- `YD-DOM-EDU` — domaine Éducation et institutions
- `YD-SYS-EDU-CATALOG` — abstraction système candidate
- `YD-MS-EDU-001` — Institution Catalog
- `YD-MS-EDU-002` — Program Catalog
- `YD-MS-EDU-003` — Curriculum & Module
- `YD-MS-EDU-004` — Qualification Framework

Le System ne fusionne pas les quatre microservices. Il fournit un niveau de lecture supérieur pour l'humain, l'IA et les outils.

## Sources actuelles

- `documentations/03-education-institutions/README.md`
- `documentations/13-architecture/SERVICE_MAP.md`
- `documentations/13-architecture/DATA_OWNERSHIP_MATRIX.md`
- `documentations/13-architecture/MICROSERVICE_BOUNDARY_REVIEW.md`
- définitions `YD-SVC-EDU-*`
- Knowledge Packs `YD-MS-EDU-*`

## Questions de validation

La preuve est satisfaisante lorsque le catalogue permet de résoudre sans ambiguïté :

1. le domaine d'un microservice Education
2. le System auquel il appartient
3. le service logique qu'il matérialise
4. ses agrégats autoritatifs
5. les données qu'il consomme
6. ses documents de référence
7. son état architecture, implémentation, déploiement et documentation
8. l'impact potentiel d'une modification d'un agrégat

## Limites

Les API, événements, exigences, ADR et contrôles de sécurité ne sont pas inventés lorsqu'ils ne sont pas encore résolus dans les sources. K2 les reliera après extraction et validation.

## Condition de généralisation

Aucun catalogue global des autres domaines ne devient normatif avant validation de cette preuve et correction des défauts de l'ontologie ou des schémas identifiés pendant Education.