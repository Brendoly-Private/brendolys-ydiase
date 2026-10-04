# YD-SVC-SPN-001 — Sponsored Placement Service

`domain: economie-produit` · `phase: P6` · `documentation: D1` · `implementation: not-started`

## Mission
Gérer placements sponsorisés avec séparation explicite des recommandations d’orientation.

## Frontière DDD
Ne modifie jamais les scores d’orientation, de matching ou d’intelligence.

## Dépendances
Content, Marketplace, Entitlements, Audit & Trace.

## Verdict DDD
`KEEP-SEPARATE`. Séparation économique nécessaire pour préserver l’intégrité des recommandations.

## Activation
Après politique d’étiquetage, ciblage et exclusions validée.