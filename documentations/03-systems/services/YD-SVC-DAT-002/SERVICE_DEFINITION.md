---
document_id: "YD-DOC-SVC-DAT-002-DEF"
title: "YD-SVC-DAT-002 — Data Acquisition Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-DAT-002, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-DAT-002 — Data Acquisition Service

> **Rôle du document**
> Définit le service logique YD-SVC-DAT-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: data` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AcquisitionJob`, `IngestionBatch`, `RawRecordEnvelope`, `ConnectorConfiguration`, `SubmissionBatch`.

## Source autoritative
YD-SVC-DAT-002 pour acquisition et enveloppe brute immuable, jamais pour vérité métier publiée.

## Données consommées
Source registry, partner/ambassador submissions, connector inputs, country config.

## Incohérences
Aucune donnée brute ne doit être promue implicitement en fait validé.
