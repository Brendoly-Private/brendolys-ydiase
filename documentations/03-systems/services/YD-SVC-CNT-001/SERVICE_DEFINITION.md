---
document_id: "YD-DOC-SVC-CNT-001-DEF"
title: "YD-SVC-CNT-001 — Content Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-CNT-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-CNT-001 — Content Service

> **Rôle du document**
> Définit le service logique YD-SVC-CNT-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: contenu-communaute-learning` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`ContentItem`, `ContentVersion`, `Publication`, `ContentAssetRef`.

## Source autoritative
YD-SVC-CNT-001.

## Données consommées
Author/Profile refs, taxonomy, moderation state, provenance pour contenu externe.

## Incohérences
Les fichiers binaires peuvent vivre en object storage mais CNT-001 reste owner des métadonnées métier.
