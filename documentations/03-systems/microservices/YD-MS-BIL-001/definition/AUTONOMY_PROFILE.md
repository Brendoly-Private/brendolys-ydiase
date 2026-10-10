---
document_id: "YD-DOC-AUTO-0CB32FD837E891FB"
title: "AUTONOMY PROFILE"
document_type: "documentation-reference"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
product: "BRENDOLYS YDIASE"
document_role: "Autonomie et ownership."
authority_level: "canonical-source"
development_usage: "mandatory-reference"
---

# YD-MS-BIL-001 — Subscription & Entitlement

Statut : `autonomy-profile-draft`

- Autorité : plans, abonnements, entitlements et quotas commerciaux; pas transactions financières.
- C1, backup AUTH. C clients/organisations, I, M2M.
- Dépendances : BIL-002 pour état financier, catalogues produits.
- Panne : révocation prioritaire; dernier entitlement seulement selon politique bornée; accès sensible fail-closed.
- Sécurité : tenant isolation, audit grants/revokes, séparation finance/entitlement.
- Repo : `brendolys-ydiase-subscription-entitlement`.
- Gate : modèle plans/quotas, règles grace period, SLO/RPO/RTO, restore.