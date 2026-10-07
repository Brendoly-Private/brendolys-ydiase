---
document_id: "YD-DOC-SVC-AI-002-DEF"
title: "YD-SVC-AI-002 — Retrieval & Grounding Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-AI-002, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-AI-002 — Retrieval & Grounding Service

> **Rôle du document**
> Définit le service logique YD-SVC-AI-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: ai` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`RetrievalCorpusDefinition`, `GroundingIndex`, `RetrievalRun`, `GroundingBundle`.

## Source autoritative
YD-SVC-AI-002 pour index et bundles; sources métier restent autoritatives.

## Données consommées
Knowledge graph, search projections, validated domain data, provenance/quality, access policy.

## Incohérences
Risque de duplication avec SRH-001. SRH sert la recherche produit; AI-002 sert le grounding contrôlé. Mutualisation technique possible sans fusion métier.
