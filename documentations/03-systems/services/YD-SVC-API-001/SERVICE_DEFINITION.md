# YD-SVC-API-001 — External API Management Service

`domain: economie-produit` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`APIProduct`, `APIClient`, `APISubscription`, `APIQuotaPolicy`, `APIUsageRecord`.

## Source autoritative
YD-SVC-API-001.

## Données consommées
Entitlements, identity/access, exposed domain contracts, billing, audit.

## Incohérences
Une API publique n’est pas owner des données qu’elle expose. API entitlement et BIL entitlement doivent avoir une règle de priorité unique en D3.
