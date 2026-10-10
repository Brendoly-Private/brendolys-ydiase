---
document_id: "YD-DOC-SVC-BIL-002-DEF"
title: "YD-SVC-BIL-002 — Billing Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-BIL-002, son périmètre, ses responsabilités et ses dépendances documentées."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "service"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-SVC-BIL-002 — Billing Service

> **Rôle du document**
> Définit le service logique YD-SVC-BIL-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: economie-produit` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`BillingAccount`, `Invoice`, `PaymentRecord`, `Transaction`, `CreditNote`.

## Source autoritative
YD-SVC-BIL-002 pour comptabilité applicative YDIASE; prestataire de paiement reste source externe de son opération.

## Données consommées
Subscription, customer refs, payment-provider events, country/currency config.

## Incohérences
À D3, séparer clairement transaction fournisseur, paiement rapproché et écriture comptable applicative.
