---
document_id: "YD-DOC-SVC-KNW-001-DEF"
title: "YD-SVC-KNW-001 — Knowledge Graph Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-KNW-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-KNW-001 — Knowledge Graph Service

> **Rôle du document**
> Définit le service logique YD-SVC-KNW-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: knowledge` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`KnowledgeNodeProjection`, `KnowledgeEdge`, `SemanticAssertion`, `GraphVersion`.

## Source autoritative
YD-SVC-KNW-001 pour relations sémantiques propres au graphe; domaines restent autoritatifs sur leurs entités.

## Données consommées
Education, skills, careers, labor, opportunities, taxonomies, provenance/quality.

## Incohérences
`KnowledgeNodeProjection` est une projection. Le graphe ne doit jamais devenir owner de `Institution`, `Program`, `Skill`, `Occupation` ou `Opportunity`.
