---
document_id: "YD-DOC-SVC-EMP-003-DEF"
title: "YD-SVC-EMP-003 — Employer Workspace Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-EMP-003, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-EMP-003 — Employer Workspace Service

> **Rôle du document**
> Définit le service logique YD-SVC-EMP-003, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: partenaires-ecosysteme` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`EmployerWorkspace`, `EmployerMembership`, `EmployerWorkspacePreference`.

## Source autoritative
YD-SVC-EMP-003 pour workspace; EMP/OPP/REC restent autoritatifs sur objets métier.

## Données consommées
Employer, opportunities, campaigns, applications, intelligence products, access/entitlements.

## Incohérences
Doit rester façade métier/BFF et ne pas répliquer la propriété des domaines sous-jacents.
