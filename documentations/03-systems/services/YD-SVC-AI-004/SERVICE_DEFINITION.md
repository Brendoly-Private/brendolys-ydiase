---
document_id: "YD-DOC-SVC-AI-004-DEF"
title: "YD-SVC-AI-004 — AI Orchestration Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-AI-004, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-AI-004 — AI Orchestration Service

> **Rôle du document**
> Définit le service logique YD-SVC-AI-004, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: ai` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AIWorkflow`, `AITask`, `AIWorkflowRun`, `AIExecutionPlan`.

## Source autoritative
YD-SVC-AI-004 pour orchestration.

## Données consommées
AI Gateway, retrieval, verification, domain tool contracts, access/consent.

## Incohérences
Ne doit pas contourner AI Gateway ni appeler directement des données interdites par CNS/entitlements.
