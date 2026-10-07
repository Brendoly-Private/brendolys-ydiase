---
document_id: "YD-DOC-SVC-EDU-002-DEF"
title: "YD-SVC-EDU-002 — Program Catalog Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-EDU-002, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-EDU-002 — Program Catalog Service

> **Rôle du document**
> Définit le service logique YD-SVC-EDU-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: education-institutions` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Program`, `ProgramVersion`, `ProgramOffering`, `AdmissionRuleSet`.

## Source autoritative
YD-SVC-EDU-002.

## Données consommées
Institution/Campus (EDU-001), Qualification refs (EDU-004), Curriculum refs (EDU-003), provenance/quality (DAT-003/004), country config (CFG-001).

## Incohérences
Le programme ne doit pas posséder le curriculum. Risque de cycle EDU-002 ↔ EDU-003 à traiter par identifiants et contrats.
