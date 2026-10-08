---
document_id: "YD-DOC-SVC-DAT-003-DEF"
title: "YD-SVC-DAT-003 — Data Provenance Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-DAT-003, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-DAT-003 — Data Provenance Service

> **Rôle du document**
> Définit le service logique YD-SVC-DAT-003, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: data` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`ProvenanceRecord`, `AssertionLineage`, `EvidenceRecord`, `TransformationLineage`.

## Source autoritative
YD-SVC-DAT-003 pour provenance et lignée.

## Données consommées
Raw records, domain publication IDs, validation decisions, source registry.

## Incohérences
Ne doit pas devenir un stockage maître des objets métier; il conserve preuves et liens.
