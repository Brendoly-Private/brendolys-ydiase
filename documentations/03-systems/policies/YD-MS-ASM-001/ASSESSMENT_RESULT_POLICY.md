---
document_id: "YD-DOC-POL-ASM-001-ASSESSMENT-RESULT"
title: "YD-MS-ASM-001 — Assessment Result Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de assessment result pour YD-MS-ASM-001."
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

# YD-MS-ASM-001 — Assessment Result Policy

> **Rôle du document**
> Établit les règles normatives de assessment result pour YD-MS-ASM-001.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `DECISION-BASELINE / IMPLEMENTATION-PENDING`

## Principe
Un AssessmentResult est le résultat d'une AssessmentDefinition versionnée appliquée à une session donnée. Il est contextualisé, daté, explicable et révisable selon la méthodologie. Il n'est ni un diagnostic universel, ni une compétence acquise, ni une identité permanente du sujet.

## AssessmentDefinition
Toute définition publiée conserve au minimum : purpose, dimensions mesurées, population/contexte applicables, scoring method version, interprétation, conditions de validité, limites, provenance/auteur, langue/localisation, Country Framework applicable et état de validation.

Une modification substantielle de questions, échelle, scoring ou interprétation crée une nouvelle version.

## Session et réponses
AssessmentSession lie sujet, definition_version, purpose autorisé, contexte et timestamps. AssessmentResponse appartient à la session. Reprise de session uniquement selon règles explicites ; aucune réponse manquante n'est inventée.

## Résultat
AssessmentResult conserve : definition_version, scoring_method_version, dimensions/scores autorisés, confidence/quality state, validity state/window, computed_at, input/session ref et explanation codes.

États de validité minimaux : `VALID`, `LIMITED`, `STALE`, `INVALIDATED`, `NOT-ASSESSABLE`.

La confiance/qualité est distincte du score mesuré.

## Interprétation
Une dimension n'est interprétée que dans les limites de sa méthodologie. Un score n'est pas automatiquement comparable entre deux versions/méthodes/contexts incompatibles.

ASM ne transforme jamais automatiquement un résultat en UserSkill. SKL-002 applique sa propre politique de dérivation.

## Correction
Une correction de méthode, réponse ou calcul n'écrase pas silencieusement le résultat historique. L'ancienne version est reliée à la correction/invalidation ; un nouveau résultat/version est produit et la cause est auditée.

## IA
Un LLM peut expliquer un résultat structuré validé. Il ne peut ni inventer un score, ni modifier la méthode, ni produire seul un diagnostic/trait psychologique autoritatif.

## Gates
DEFINED : version méthodologique, séparation score/confiance/validité, correction non destructive, comparabilité contrôlée, frontière UserSkill, rôle IA.

TBD : instruments/méthodes réels, validation scientifique/psychométrique applicable, seuils, règles mineurs, Privacy/rétention, BIA/RPO/RTO/restore et tests sécurité.

Statut final : `ASSESSMENT-SEMANTICS-CLOSED / METHODS-REQUIRE-VALIDATION`.
