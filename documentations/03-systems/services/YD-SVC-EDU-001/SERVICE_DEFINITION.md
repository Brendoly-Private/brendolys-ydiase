---
document_id: "YD-DOC-SVC-EDU-001-DEF"
title: "YD-SVC-EDU-001 — Institution Catalog Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-EDU-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-EDU-001 — Institution Catalog Service

> **Rôle du document**
> Définit le service logique YD-SVC-EDU-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: education-institutions` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Institution`, `Campus`, `InstitutionStatus`, `InstitutionPresence`.

## Source autoritative
YD-SVC-EDU-001 après validation et publication YDIASE.

## Données consommées
Source records (DAT-002/003), taxonomies (DAT-005), country/territory (CFG-001), partner/institution claims (PRT-001/INS-001).

## Incohérences
INS-001 peut soumettre des changements mais ne possède jamais `Institution`.
