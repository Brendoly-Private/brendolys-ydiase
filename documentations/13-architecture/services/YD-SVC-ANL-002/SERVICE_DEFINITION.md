# YD-SVC-ANL-002 — Institution Intelligence Service

`domain: analytics` · `phase: P6` · `documentation: D1` · `implementation: not-started`

## Mission
Produire analyses et indicateurs destinés aux établissements selon leurs droits.

## Frontière DDD
Produit des vues analytiques B2B. Ne modifie pas les catalogues Education.

## Dépendances
Analytics, Institution Catalog, Labor Market Intelligence, Billing/Entitlements.

## Verdict DDD
`KEEP-PRODUCT-BOUNDARY`. Peut partager le moteur Analytics tout en gardant contrats et droits propres.

## Activation
Après définition du produit Institution et règles de confidentialité.