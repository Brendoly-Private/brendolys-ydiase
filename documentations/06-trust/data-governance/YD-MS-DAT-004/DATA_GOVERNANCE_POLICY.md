---
document_id: "YD-DOC-TRU-DAT-004-DATA-GOVERNANCE-POLICY"
title: "DAT-004 — Quality & Validation Decision Policy"
document_type: "trust-policy"
document_role: "Établit une règle ou baseline normative de gouvernance applicable au périmètre concerné."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "trust"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# DAT-004 — Quality & Validation Decision Policy

> **Rôle du document**
> Établit une règle ou baseline normative de gouvernance applicable au périmètre concerné.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / THRESHOLDS-PENDING`

## Principe
**Qualité, validation et vérité métier sont distinctes.** DAT-004 décide si une donnée satisfait une politique de validation ; le domaine métier décide de sa publication/usage selon son contrat.

## Objets
QualityAssessment, ValidationCase, Anomaly, CorroborationCase, ValidationDecision.

## Dimensions
Selon classe : complétude, conformité schema, cohérence, fraîcheur, exactitude vérifiable, unicité, plausibilité, provenance, corroboration et intégrité.

Les seuils numériques sont versionnés par DataClassValidationPolicy et restent à valider.

## Décision
États minimaux : `PASS`, `PASS-WITH-WARNINGS`, `REVIEW-REQUIRED`, `FAIL`, `NOT-ASSESSABLE`.
`NOT-ASSESSABLE` n'est jamais PASS.

Une ValidationDecision conserve policy/rule versions, input/provenance refs, résultats, anomalies, overrides, approbations et timestamps.

## Corroboration
Plusieurs sources ne deviennent pas automatiquement vérité par majorité. Indépendance, qualité, fraîcheur et autorité des sources sont prises en compte selon policy.

## Override
Tout override manuel est motivé, scoped, temporaire si pertinent, attribuable et audité. Aucun override ne peut effacer le résultat initial.

## Promotion
FAIL ou REVIEW-REQUIRED bloque promotion automatique lorsque la classe l'exige. Un domaine ne peut masquer l'état de validation reçu.

Statut final : `QUALITY-VALIDATION-SEMANTICS-CLOSED / NUMERIC-THRESHOLDS-PREPROD-PENDING`.
