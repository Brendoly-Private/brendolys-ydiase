---
document_id: "YD-DOC-SVC-OPP-002-DEF"
title: "YD-SVC-OPP-002 — Opportunity Matching Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-OPP-002, son périmètre, ses responsabilités et ses dépendances documentées."
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
---

# YD-SVC-OPP-002 — Opportunity Matching Service

> **Rôle du document**
> Définit le service logique YD-SVC-OPP-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: opportunites-recrutement` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`OpportunityMatchRun`, `OpportunityMatch`, `MatchExplanation`.

## Source autoritative
YD-SVC-OPP-002 pour le résultat de matching.

## Données consommées
Opportunities, profile/skills/experience, occupations, consent, recommendation policies.

## Incohérences
Chevauchement potentiel avec REC-001. OPP-002 reste spécialisé opportunité-candidat; REC-001 reste recommandation générique.
