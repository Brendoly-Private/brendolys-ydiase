---
document_id: "YD-DOC-SVC-AUD-001-DEF"
title: "YD-SVC-AUD-001 — Audit & Trace Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-AUD-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-AUD-001 — Audit & Trace Service

> **Rôle du document**
> Définit le service logique YD-SVC-AUD-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: plateforme-gouvernance` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AuditEvent`, `AuditTrail`, `SensitiveActionRecord`, `AuditExport`.

## Source autoritative
YD-SVC-AUD-001 pour traces fonctionnelles et sensibles.

## Données consommées
Events/actions des services, identity refs, security context.

## Incohérences
À distinguer de logs techniques/observabilité. AUD porte preuve fonctionnelle et conformité, pas télémétrie générale.
