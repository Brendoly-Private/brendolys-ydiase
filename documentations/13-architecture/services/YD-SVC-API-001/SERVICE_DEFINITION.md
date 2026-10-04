# YD-SVC-API-001 — External API Management Service

`domain: economie-produit` · `phase: P7` · `documentation: D1` · `implementation: not-started`

## Mission
Gérer produits API externes, clients, droits, quotas, versions et exposition gouvernée.

## Frontière DDD
Ne possède pas les données exposées. Applique les politiques définies par les domaines sources.

## Dépendances
Entitlements, Audit & Trace, Data Product, services sources.

## Verdict DDD
`KEEP-SEPARATE`. Surface externe et gouvernance de contrats propres.

## Activation
Après premier produit API approuvé.