# YD-SVC-BIL-001 — Subscription & Entitlement Service

`domain: economie-produit` · `phase: P5` · `documentation: D1` · `implementation: not-started`

## Mission
Porter plans, droits fonctionnels, quotas et périodes d’accès.

## Frontière DDD
Propriétaire candidat de `Subscription` et `Entitlement`. Ne traite pas lui-même les paiements.

## Dépendances
Identity, Billing, produits commerciaux.

## Verdict DDD
`KEEP-SEPARATE`. Les droits d’accès doivent rester indépendants du fournisseur de paiement.

## Activation
Après catalogue d’offres et règles de droits validés.