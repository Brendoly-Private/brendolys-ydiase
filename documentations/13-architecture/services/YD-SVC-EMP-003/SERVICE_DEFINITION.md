# YD-SVC-EMP-003 — Employer Workspace Service

`domain: partenaires-ecosysteme` · `phase: P5` · `documentation: D1` · `implementation: not-started`

## Mission
Fournir aux employeurs un espace de gestion des opportunités, campagnes et produits autorisés.

## Frontière DDD
Orchestre les services B2B sans devenir propriétaire des opportunités, candidatures ou profils.

## Dépendances
Employer, Opportunity, Talent & Recruitment, Billing, Identity.

## Verdict DDD
`KEEP-AS-BFF-CANDIDATE`. Peut devenir couche d’expérience plutôt que microservice métier.

## Activation
Après besoins B2B et contrats interservices validés.