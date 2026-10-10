---
document_id: "YD-DOC-SVC-AI-003-DEF"
title: "YD-SVC-AI-003 — AI Verification Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-AI-003, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-AI-003 — AI Verification Service

> **Rôle du document**
> Définit le service logique YD-SVC-AI-003, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: ai` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AIVerificationCase`, `ClaimCheck`, `AIConfidenceAssessment`, `VerificationDecision`.

## Source autoritative
YD-SVC-AI-003 pour résultat de vérification IA.

## Données consommées
AI outputs, grounding bundles, provenance, domain truths, policy rules.

## Incohérences
Un verdict IA ne remplace pas une validation métier DAT-004 ou humaine lorsque celle-ci est requise.
