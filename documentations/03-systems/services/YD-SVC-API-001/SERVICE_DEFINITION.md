---
document_id: "YD-DOC-SVC-API-001-DEF"
title: "YD-SVC-API-001 — External API Management Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-API-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-API-001 — External API Management Service

> **Rôle du document**
> Définit le service logique YD-SVC-API-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: economie-produit` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`APIProduct`, `APIClient`, `APISubscription`, `APIQuotaPolicy`, `APIUsageRecord`.

## Source autoritative
YD-SVC-API-001.

## Données consommées
Entitlements, identity/access, exposed domain contracts, billing, audit.

## Incohérences
Une API publique n’est pas owner des données qu’elle expose. API entitlement et BIL entitlement doivent avoir une règle de priorité unique en D3.
