---
document_id: "YD-DOC-ADR-ADR-LRN-001-DISCOVERY-AUTHORITY-BOUNDARY"
title: "ADR-LRN-001 — Discovery Authority Boundary"
document_type: "architecture-decision-record"
document_role: "Consigne une décision d’architecture et ses conséquences applicables."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "decisions"
created_at: "2026-10-06"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# ADR-LRN-001 — Discovery Authority Boundary

> **Rôle du document**
> Consigne une décision d’architecture et ses conséquences applicables.
> **Usage développement :** référence obligatoire pour les choix d’architecture concernés.

Statut : `ACCEPTED / DOCUMENTARY-BASELINE`

## Contexte

YDIASE doit relier les écarts de compétences à des options d'apprentissage sans dupliquer les autorités Education, Skills, Marketplace et Recommendation.

## Décision

LRN-001 possède `LearningResource`, `LearningOfferingRef` et `LearningRecommendationSet`.

LRN-001 ne possède pas les programmes académiques EDU, les compétences ou niveaux individuels SKL, les objets commerciaux MKT, ni un moteur générique REC.

Une référence externe conserve son autorité source. Une progression, complétion, évaluation ou certification autoritative exige une nouvelle revue de frontière avant création d'un composant physique distinct.

Le ranking learning organique reste indépendant du sponsoring et des intérêts commerciaux.

## Conséquences

- les intégrations restent contractuelles et versionnées
- les projections locales ne deviennent pas autorités
- les corrections des sources invalident ou datent les résultats dérivés
- aucun `LRN-002` n'est présumé nécessaire
- une extension vers LMS/assessment exige une décision explicite

## Alternatives rejetées

- copier programmes et offres dans LRN comme données autoritatives
- faire de LRN un second moteur générique REC
- considérer achat ou complétion comme preuve automatique de compétence
- créer immédiatement un LRN-002 sans cycle d'autorité autonome
