---
document_id: "YD-DOC-SVC-REC-001-DEF"
title: "YD-SVC-REC-001 — Recommendation Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-REC-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-REC-001 — Recommendation Service

> **Rôle du document**
> Définit le service logique YD-SVC-REC-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: orientation-recommandation` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`RecommendationRun`, `RecommendationSet`, `RecommendationItem`, `RecommendationExplanation`, `RecommendationEvidenceSnapshot`.

## Source autoritative
YD-SVC-REC-001 pour le résultat calculé et son explication.

## Données consommées
Profile, skills, assessments, programs, occupations, labor signals/intelligence, opportunities, knowledge graph, policy/config.

## Incohérences
Ne doit jamais être source de vérité des données d’entrée. Sponsored Placement ne peut modifier ses scores.
