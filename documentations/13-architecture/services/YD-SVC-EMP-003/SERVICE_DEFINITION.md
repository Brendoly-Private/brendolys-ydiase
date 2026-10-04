# YD-SVC-EMP-003 — Employer Workspace Service

`domain: partenaires-ecosysteme` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`EmployerWorkspace`, `EmployerMembership`, `EmployerWorkspacePreference`.

## Source autoritative
YD-SVC-EMP-003 pour workspace; EMP/OPP/REC restent autoritatifs sur objets métier.

## Données consommées
Employer, opportunities, campaigns, applications, intelligence products, access/entitlements.

## Incohérences
Doit rester façade métier/BFF et ne pas répliquer la propriété des domaines sous-jacents.
