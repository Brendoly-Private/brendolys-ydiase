---
document_id: "YD-DOC-SVC-LAB-001-DEF"
title: "YD-SVC-LAB-001 — Labor Signals Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-LAB-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-LAB-001 — Labor Signals Service

> **Rôle du document**
> Définit le service logique YD-SVC-LAB-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: marche-travail` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`LaborSignal`, `ObservedDemandSignal`, `DeclaredNeedSignal`, `InstitutionalSignal`, `EconomicSignal`, `SignalObservation`.

## Source autoritative
YD-SVC-LAB-001 pour les signaux normalisés YDIASE; la source externe reste attribuée via provenance.

## Données consommées
Raw acquisitions (DAT-002), provenance/quality, occupation/skill refs, employer refs, territory/config.

## Incohérences
Une offre publiée ne doit pas être assimilée automatiquement au marché réel; le type de signal doit rester explicite.
