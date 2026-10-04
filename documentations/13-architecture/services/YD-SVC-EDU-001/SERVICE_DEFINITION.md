# YD-SVC-EDU-001 — Institution Catalog Service

`domain: education-institutions` · `phase: P1` · `documentation: D1` · `implementation: not-started`

## Mission
Porter établissements, campus, types, statut, localisation et versions validées.

## Frontière DDD
Propriétaire candidat de `Institution` et `Campus`. Ne possède ni programmes, ni curricula, ni relation de partenariat.

## Dépendances
Country Configuration, Data Provenance, Data Quality.

## Verdict DDD
`KEEP-SEPARATE`. Référentiel central réutilisé par plusieurs domaines.

## Activation
Après modèle institutionnel et sources Burkina validés.