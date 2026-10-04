# YD-SVC-EDU-002 — Program Catalog Service

`domain: education-institutions` · `phase: P1` · `documentation: D1` · `implementation: not-started`

## Mission
Porter filières, formations, programmes, versions, rattachements et états de publication.

## Frontière DDD
Propriétaire candidat de `Program` et `ProgramVersion`. Référence Institution, Qualification et Curriculum sans les posséder.

## Dépendances
Institution Catalog, Qualification Framework, Curriculum & Module, Data Provenance.

## Verdict DDD
`KEEP-SEPARATE`. Historisation et cycle de publication propres.

## Activation
Avec la cartographie Education du pilote.