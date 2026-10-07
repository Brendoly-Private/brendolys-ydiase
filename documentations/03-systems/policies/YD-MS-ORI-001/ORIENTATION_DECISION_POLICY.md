---
document_id: "YD-DOC-POL-ORI-001-ORIENTATION-DECISION"
title: "YD-MS-ORI-001 — Orientation & Decision Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de orientation decision pour YD-MS-ORI-001."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "policy"
---

# YD-MS-ORI-001 — Orientation & Decision Policy

> **Rôle du document**
> Établit les règles normatives de orientation decision pour YD-MS-ORI-001.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `DECISION-BASELINE / IMPLEMENTATION-PENDING`
Portée : ORI-001 + ORI-002 logique

## Principe
Orientation organise un processus de décision. Elle ne décide pas silencieusement à la place du sujet et ne transforme pas une recommandation en vérité.

## Cycle OrientationCase
États minimaux : `DRAFT`, `INFORMATION-GATHERING`, `READY-FOR-COMPARISON`, `COMPARING`, `DECISION-PENDING`, `DECIDED`, `REOPENED`, `CLOSED`.

Les transitions sont auditables et versionnées.

## Objectifs et contraintes
OrientationObjective exprime ce que le dossier cherche à atteindre. OrientationConstraintSet contient uniquement les contraintes nécessaires et autorisées pour ce dossier.

Les préférences générales restent PRF-001. Une contrainte spécifique au dossier peut être copiée comme snapshot versionné pour reproductibilité, sans devenir la nouvelle vérité PRF.

## Comparaison
ComparisonCase/Set compare des options référencées/versionnées. DecisionCriterion distingue au minimum :
- `HARD-CONSTRAINT` ;
- `REQUIRED` ;
- `PREFERENCE` ;
- `INFORMATIONAL`.

Une option violant une HARD-CONSTRAINT n'est pas rendue première par un score agrégé sans signalement explicite.

`UNKNOWN` n'est pas `FAILED`.

## Scorecard
DecisionScorecard documente la comparaison selon critères/pondérations versionnés. Elle ne remplace pas le ranking REC et ne devient pas vérité des sources.

Les pondérations numériques restent validables/configurables selon policy ; aucune préférence continentale universelle n'est supposée.

## Recommendation
ORI demande/consomme un RecommendationRun par contrat non circulaire. Le résultat REC est référencé avec sa version/date/evidence snapshot. Si REC est indisponible, ORI peut conserver le dossier et les données déjà acquises mais n'invente pas un nouveau ranking.

## DecisionRecord
OrientationDecisionRecord enregistre une décision explicitement prise/confirmée selon workflow autorisé. Il conserve : options considérées, option(s) retenue(s) ou absence de choix, critères/snapshots, recommendation refs utilisées, explications, acteur/subject confirmation, timestamps et version.

Le système distingue clairement :
- suggestion système ;
- comparaison ;
- décision utilisateur/acteur autorisé.

## Réouverture
Une décision peut être réouverte si objectifs, contraintes, données source ou contexte changent. L'ancien DecisionRecord reste historique ; une nouvelle version/cycle est créé.

## Explicabilité
Le dossier doit permettre d'expliquer : données utilisées, critères, contraintes bloquantes, inconnues, recommandations consultées, hypothèses et raison enregistrée du choix.

Un LLM peut reformuler ces éléments mais ne crée pas une justification absente.

## IA et autonomie humaine
L'IA ne peut pas seule confirmer OrientationDecisionRecord, masquer une alternative pour cause non gouvernée, ni transformer un signal probabiliste en obligation.

## Gates
DEFINED : cycle dossier, objectifs/contraintes, comparaison, hard constraints, UNKNOWN, scorecard, séparation REC, DecisionRecord, réouverture, explicabilité et rôle IA.

TBD : pondérations réelles, workflow mineurs/représentation, Privacy/rétention, règles pays, BIA/RPO/RTO/restore, IAM/IDOR et contrats physiques.

Statut final : `ORIENTATION-DECISION-SEMANTICS-CLOSED / VALIDATION-PREPROD-PENDING`.
