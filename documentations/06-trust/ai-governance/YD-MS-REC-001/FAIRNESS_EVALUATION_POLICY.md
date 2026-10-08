---
document_id: "YD-DOC-TRU-REC-001-FAIRNESS-EVALUATION-POLICY"
title: "REC-001 — Fairness Evaluation Policy"
document_type: "trust-policy"
document_role: "Établit une règle normative de gouvernance, confiance ou données applicable au périmètre concerné."
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

# REC-001 — Fairness Evaluation Policy

> **Rôle du document**
> Établit une règle normative de gouvernance, confiance ou données applicable au périmètre concerné.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-METRICS-BASELINE / THRESHOLDS-VALIDATION-PENDING`

## Objet
Mesurer les disparités du système sans supposer qu'une égalité brute de résultats est toujours l'objectif correct. Toute métrique est interprétée avec éligibilité, contexte, qualité des données et finalité.

Les attributs nécessaires à l'audit d'équité sont isolés du ranking, minimisés, protégés et utilisés seulement sous gouvernance applicable.

## Unités d'évaluation
Les analyses sont segmentées au minimum lorsque pertinent par recommendation_type, policy/model version, pays/territoire, langue, type de parcours et qualité/couverture des données. Les comparaisons non comparables sont interdites.

## Métriques normatives

### Couverture
- `CandidateCoverageRate` : part de l'inventaire attendu effectivement évaluable.
- `EvidenceCoverageRate` : part des signaux requis disponibles/valides.
- `UnknownCriticalRate` : fréquence des données critiques UNKNOWN.

### Éligibilité et abstention
- `EligibilityRate` par cohorte comparable.
- `AbstentionRate` et répartition des reason codes.
- `FalseExclusionRate` lorsqu'un ground truth gouverné existe.

### Qualité du ranking
- métriques de pertinence/ranking adaptées au use case et au ground truth disponible ;
- `TopKExposureRate` : exposition dans top-K ;
- `MeanOrganicRank` sur candidats comparables ;
- stabilité du ranking lors de perturbations non pertinentes.

### Calibration et incertitude
Lorsque REC produit confiance/probabilité : erreur de calibration par cohortes comparables. Sinon, contrôler la distribution des états d'incertitude et `NOT-ASSESSABLE`.

### Explicabilité
- `ExplanationCoverageRate` ;
- taux d'explications avec provenance/version complète ;
- taux d'inconnues critiques explicitement signalées.

## Analyse des écarts
Pour chaque métrique, produire valeurs par cohorte, valeur de référence, écart absolu/relatif si statistiquement et métier pertinent, taille d'échantillon et intervalle/incertitude.

Un écart n'est ni automatiquement discrimination ni automatiquement acceptable. Il déclenche analyse causale : données manquantes, qualité, règles d'éligibilité, représentativité, contexte réel, modèle/policy ou défaut système.

## Interdictions
- optimiser artificiellement une métrique d'équité en falsifiant pertinence ou éligibilité ;
- masquer UNKNOWN pour améliorer un KPI ;
- utiliser un attribut protégé comme proxy commercial ;
- conclure sur de très petits échantillons sans signaler l'incertitude ;
- agréger des pays/contextes incompatibles pour cacher une disparité ;
- utiliser les données d'audit d'équité pour personnaliser le ranking sans autorisation distincte.

## Seuils et décision
Les seuils numériques ne sont pas universels et ne sont pas inventés dans cette baseline. Chaque `RecommendationPolicyVersion` activée référence une `FairnessEvaluationProfile` avec métriques applicables, cohortes, minimum sample size, seuils/warning limits, protocole statistique, approbateurs et rollback criteria.

États : `PASS`, `PASS-WITH-MONITORING`, `REVIEW-REQUIRED`, `BLOCKED`, `NOT-ASSESSABLE`.

Un `BLOCKED` empêche promotion. `NOT-ASSESSABLE` sur une dimension critique exige justification et décision de gouvernance ; il n'est pas transformé en PASS.

## Lifecycle
Évaluation obligatoire avant promotion d'une nouvelle policy/model version, après changement majeur de données/features et périodiquement en production selon criticité. Dérive significative déclenche revue et éventuellement rollback.

## Preuves
Conserver dataset/version ou référence gouvernée, période, policy/model version, définition des cohortes, calculs, tailles d'échantillon, incertitude, anomalies, décision et approbations. Ne pas exposer de données personnelles brutes dans le rapport.

## Gate
Avant `ACTIVE`, YDIASE doit fixer les seuils réels par use case et démontrer la suite sur des données représentatives autorisées.

Statut final : `FAIRNESS-METRICS-DEFINED / NUMERIC-THRESHOLDS-AND-EVIDENCE-PENDING`.
