# YD-SVC-BIL-002 — Billing Service

`domain: economie-produit` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`BillingAccount`, `Invoice`, `PaymentRecord`, `Transaction`, `CreditNote`.

## Source autoritative
YD-SVC-BIL-002 pour comptabilité applicative YDIASE; prestataire de paiement reste source externe de son opération.

## Données consommées
Subscription, customer refs, payment-provider events, country/currency config.

## Incohérences
À D3, séparer clairement transaction fournisseur, paiement rapproché et écriture comptable applicative.
