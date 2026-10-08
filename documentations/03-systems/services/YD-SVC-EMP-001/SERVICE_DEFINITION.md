---
document_id: "YD-DOC-SVC-EMP-001-DEF"
title: "YD-SVC-EMP-001 — Employer Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-EMP-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-EMP-001 — Employer Service

> **Rôle du document**
> Définit le service logique YD-SVC-EMP-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: opportunites-recrutement` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Employer`, `EmployerPresence`, `EmployerVerification`, `EmployerProfile`.

## Source autoritative
YD-SVC-EMP-001.

## Données consommées
Identity/account refs, partner data, country/territory, provenance/quality.

## Incohérences
Employer Workspace et Talent & Recruitment ne doivent pas dupliquer `Employer`.
