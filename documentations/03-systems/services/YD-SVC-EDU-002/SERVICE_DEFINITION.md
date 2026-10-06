# YD-SVC-EDU-002 — Program Catalog Service

`domain: education-institutions` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Program`, `ProgramVersion`, `ProgramOffering`, `AdmissionRuleSet`.

## Source autoritative
YD-SVC-EDU-002.

## Données consommées
Institution/Campus (EDU-001), Qualification refs (EDU-004), Curriculum refs (EDU-003), provenance/quality (DAT-003/004), country config (CFG-001).

## Incohérences
Le programme ne doit pas posséder le curriculum. Risque de cycle EDU-002 ↔ EDU-003 à traiter par identifiants et contrats.
