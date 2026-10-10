---
document_id: "YD-DOC-SVC-EMP-002-DEF"
title: "YD-SVC-EMP-002 — Talent & Recruitment Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-EMP-002, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-EMP-002 — Talent & Recruitment Service

> **Rôle du document**
> Définit le service logique YD-SVC-EMP-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: opportunites-recrutement` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`TalentPool`, `RecruitmentCampaign`, `CandidateSelection`, `RecruitmentPipeline`.

## Source autoritative
YD-SVC-EMP-002.

## Données consommées
Employer, opportunities/applications, permitted profile/skill projections, matching results, consent.

## Incohérences
Les profils candidats restent PRF/SKL; ce service ne doit stocker que projections autorisées et états de recrutement.
