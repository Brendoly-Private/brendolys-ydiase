---
document_id: "YD-DOC-SVC-SRH-001-DEF"
title: "YD-SVC-SRH-001 — Search & Discovery Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-SRH-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-SRH-001 — Search & Discovery Service

> **Rôle du document**
> Définit le service logique YD-SVC-SRH-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: plateforme` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`SearchIndexDefinition`, `SearchDocumentProjection`, `SearchQuerySession` si persistée.

## Source autoritative
SRH-001 uniquement pour configuration et index de recherche; les domaines restent autoritatifs pour les documents projetés.

## Données consommées
Institutions, programs, modules, occupations, opportunities, content, learning, états de publication.

## Incohérences
Un index n’est jamais une source métier. Toute réindexation doit pouvoir repartir des sources autoritatives.
