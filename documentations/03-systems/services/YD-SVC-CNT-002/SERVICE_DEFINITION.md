---
document_id: "YD-DOC-SVC-CNT-002-DEF"
title: "YD-SVC-CNT-002 — Feed Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-CNT-002, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-CNT-002 — Feed Service

> **Rôle du document**
> Définit le service logique YD-SVC-CNT-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: contenu-communaute-learning` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`FeedDefinition`, `FeedCandidateSet`, `FeedRankingRun`, `UserFeedState`.

## Source autoritative
YD-SVC-CNT-002 pour état et ranking du feed.

## Données consommées
Content, user preferences, community relations, learning/opportunities, recommendation signals, moderation.

## Incohérences
Ne doit pas devenir un second Recommendation Service. Son ranking reste limité au feed.
