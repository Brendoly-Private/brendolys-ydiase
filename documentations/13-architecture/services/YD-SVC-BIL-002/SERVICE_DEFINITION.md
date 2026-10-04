# YD-SVC-BIL-002 — Billing Service

`domain: economie-produit` · `phase: P5` · `documentation: D1` · `implementation: not-started`

## Mission
Porter factures, états de paiement, rapprochements et références de transaction.

## Frontière DDD
Ne stocke pas de secrets de paiement hors besoin validé. Les prestataires externes restent isolés derrière des contrats.

## Dépendances
Subscription & Entitlement, Audit & Trace, Country Configuration.

## Verdict DDD
`KEEP-SEPARATE`. Risque financier et intégrations propres.

## Activation
Après modèle financier, fiscal et prestataire validés par pays.