# YD-SVC-ADM-001 — Administration Service

`domain: plateforme-gouvernance` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AdminCase`, `AdministrativeActionRequest`, `OperationalOverride`.

## Source autoritative
YD-SVC-ADM-001 pour workflow administratif; jamais pour objets administrés.

## Données consommées
Domain admin contracts, identity/access, audit, moderation, configuration.

## Incohérences
Un override doit être audité et ne doit pas contourner les invariants du domaine cible.
