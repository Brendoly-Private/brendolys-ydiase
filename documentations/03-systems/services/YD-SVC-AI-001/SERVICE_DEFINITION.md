---
document_id: "YD-DOC-SVC-AI-001-DEF"
title: "YD-SVC-AI-001 — AI Gateway Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-AI-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-AI-001 — AI Gateway Service

> **Rôle du document**
> Définit le service logique YD-SVC-AI-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: ai` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AIRequest`, `AIExecutionPolicy`, `AIUsageRecord`.

## Source autoritative
YD-SVC-AI-001 est autoritatif pour les requêtes IA gouvernées, politiques d’exécution IA et traces fonctionnelles d’usage IA.

## Données consommées
Identity/access, consent, entitlements, modèles approuvés depuis YD-SVC-MLP-001, audit policies, country/configuration constraints.

## Frontière
AI Gateway contrôle l’accès et l’exécution. Il ne possède plus le registre des modèles, leurs versions, évaluations, promotions ou retraits.

## Incohérences
La frontière Model Registry/MLOps est extraite avant D3 dans `YD-SVC-MLP-001`. Les contrats Gateway → MLOps et Orchestration → MLOps seront détaillés en D3.
