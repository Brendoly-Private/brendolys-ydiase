# YD-SVC-EDU-003 — Curriculum & Module Service

`domain: education-institutions` · `phase: P1` · `documentation: D1` · `implementation: not-started`

## Mission
Gérer curricula, modules, unités d’enseignement, relations et versions dans le temps.

## Frontière DDD
Propriétaire candidat de `Curriculum`, `Module`, `TeachingUnit` et leurs versions. Program Catalog référence les curricula sans les posséder.

## Dépendances
Program Catalog, Institution Catalog, Data Provenance.

## Verdict DDD
`KEEP-SEPARATE`. Historisation et granularité justifient une frontière propre.

## Activation
Après taxonomie minimale et règles de version validées.