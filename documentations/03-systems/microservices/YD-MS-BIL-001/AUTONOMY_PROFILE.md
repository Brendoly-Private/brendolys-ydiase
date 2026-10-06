# YD-MS-BIL-001 — Subscription & Entitlement

Statut : `autonomy-profile-draft`

- Autorité : plans, abonnements, entitlements et quotas commerciaux; pas transactions financières.
- C1, backup AUTH. C clients/organisations, I, M2M.
- Dépendances : BIL-002 pour état financier, catalogues produits.
- Panne : révocation prioritaire; dernier entitlement seulement selon politique bornée; accès sensible fail-closed.
- Sécurité : tenant isolation, audit grants/revokes, séparation finance/entitlement.
- Repo : `brendolys-ydiase-subscription-entitlement`.
- Gate : modèle plans/quotas, règles grace period, SLO/RPO/RTO, restore.