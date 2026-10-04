# YD-SVC-OPP-001 — Opportunity Service

`domain: opportunites-recrutement` · `phase: P4` · `documentation: D1` · `implementation: not-started`

## Mission
Porter les opportunités publiées ou collectées : emploi, stage, programme et catégories autorisées.

## Frontière DDD
Propriétaire candidat de `Opportunity` et de ses versions. L’employeur reste possédé par Employer Service.

## Dépendances
Employer, Data Provenance, Country Configuration.

## Verdict DDD
`KEEP-SEPARATE`. Cycle de publication et expiration propres.

## Activation
Après modèle de provenance, validité et retrait défini.