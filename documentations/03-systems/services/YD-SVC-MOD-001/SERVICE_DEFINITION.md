---
document_id: "YD-DOC-SVC-MOD-001-DEF"
title: "YD-SVC-MOD-001 — Moderation Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-MOD-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-MOD-001 — Moderation Service

> **Rôle du document**
> Définit le service logique YD-SVC-MOD-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: plateforme-gouvernance` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`ModerationPolicy`, `ModerationPolicyVersion`, `ModerationCase`, `ModerationDecision`, `PolicyViolation`, `Appeal`.

## Source autoritative
YD-SVC-MOD-001 est autoritatif pour la politique opérationnelle de modération, ses versions, les dossiers, décisions, violations et recours.

## Données consommées
Content/community/marketplace/sponsored objects, identity refs, country/legal constraints depuis CFG-001 et décisions de conformité applicables, audit depuis AUD-001.

## Frontière de gouvernance
La gouvernance documentaire approuve et trace les décisions de politique. CFG-001 fournit les paramètres pays. MOD-001 traduit les règles approuvées en politique de modération versionnée et exécutable. Aucun autre service ne maintient une copie normative concurrente.

## Incohérences
Ownership de `ModerationPolicy` résolu en D2. Les workflows de recours et contrats avec les domaines modérés seront définis en D3.
