# YD-SVC-LAB-001 — Labor Signals Service

`domain: marche-travail` · `phase: P3` · `documentation: D1` · `implementation: not-started`

## Mission
Porter les observations du marché : offres, besoins déclarés, enquêtes, signaux institutionnels, économiques et informels selon leur nature.

## Frontière DDD
Propriétaire candidat de `LaborSignal` et de son type. Une observation ne devient jamais seule une vérité sur le marché.

## Dépendances
Data Acquisition, Data Provenance, Data Quality, Country Configuration.

## Verdict DDD
`KEEP-SEPARATE`. C’est la frontière entre observation et analyse.

## Activation
Après typologie des signaux et provenance validées.