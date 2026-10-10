---
document_id: "YD-DOC-SVC-EDU-003-DEF"
title: "YD-SVC-EDU-003 — Curriculum & Module Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-EDU-003, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-EDU-003 — Curriculum & Module Service

> **Rôle du document**
> Définit le service logique YD-SVC-EDU-003, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: education-institutions` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Curriculum`, `CurriculumVersion`, `Module`, `TeachingUnit`, `ModuleSequence`.

## Source autoritative
YD-SVC-EDU-003.

## Données consommées
ProgramRef (EDU-002), Skill/Knowledge refs (SKL-001), provenance/quality (DAT-003/004).

## Incohérences
Risque de cycle logique avec EDU-002. `Program` reste EDU-002 et `Curriculum` reste EDU-003.
