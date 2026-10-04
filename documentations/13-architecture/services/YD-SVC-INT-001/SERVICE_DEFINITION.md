# YD-SVC-INT-001 — Intelligence Product Service

`domain: economie-produit` · `phase: P7` · `documentation: D1` · `implementation: not-started`

## Mission
Composer observatoires, indicateurs et produits d’intelligence destinés aux organisations.

## Frontière DDD
Consomme Analytics et Labor Market Intelligence. Ne modifie pas les sources et conserve la provenance des résultats.

## Dépendances
Analytics, Labor Market Intelligence, Data Product, Entitlements.

## Verdict DDD
`KEEP-PRODUCT-BOUNDARY`. Peut partager l’infrastructure analytique sans perdre sa frontière commerciale.

## Activation
Après définition d’un produit B2B précis et de ses droits.