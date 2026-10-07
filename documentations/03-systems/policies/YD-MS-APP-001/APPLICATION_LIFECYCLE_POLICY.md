---
document_id: "YD-DOC-POL-APP-001-APPLICATION-LIFECYCLE"
title: "YD-MS-APP-001 — Application Lifecycle Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de application lifecycle pour YD-MS-APP-001."
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

# YD-MS-APP-001 — Application Lifecycle Policy

> **Rôle du document**
> Établit les règles normatives de application lifecycle pour YD-MS-APP-001.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / PREPROD-PENDING`
Nature : `AUTH`
Criticité : `C1`

## 1. Autorité
APP-001 seul possède Application, ApplicationStatusHistory, ApplicationSubmission et CandidateResponse. EMP-002 peut demander une transition autorisée mais ne maintient jamais un statut concurrent.

## 2. Création
Avant création, APP revalide synchroniquement auprès d'OPP-001 que l'opportunité/version accepte encore les candidatures et vérifie les décisions CNS requises.

Un MatchRef ou RecommendationRef peut être conservé comme contexte, jamais comme autorisation de candidater.

## 3. Machine d'état
Baseline :
`DRAFT` → `SUBMITTED` → `RECEIVED` → `UNDER-REVIEW`.

Transitions possibles selon policy : `SHORTLISTED`, `INTERVIEW`, `OFFERED`, `ACCEPTED`, `REJECTED`, `WITHDRAWN`, `CANCELLED`, `CLOSED`.

Les transitions exactes par type de recrutement sont versionnées. Aucun saut d'état non autorisé.

## 4. Historique
Chaque transition conserve from/to, actor/ref, reason code, command/idempotency ref, occurred_at, policy version et audit ref. L'historique est non destructif.

## 5. Autorités
- candidat : soumission, réponses et retrait selon policy ;
- recruteur/EMP-002 : commandes de sélection selon permissions ;
- APP : validation et application de la transition ;
- workspace : aucune écriture directe DB.

## 6. Idempotence/concurrence
Toute commande sensible est idempotente. Une version attendue/contrôle de concurrence empêche deux décisions incompatibles d'écraser l'état.

## 7. Données
Une candidature contient uniquement le snapshot/projections nécessaires à cette candidature. PRF/SKL restent sources maîtres ; les changements ultérieurs ne réécrivent pas silencieusement le dossier soumis.

## 8. Opportunity changes
Retrait/expiration après SUBMITTED n'efface pas la candidature. La policy définit son effet et l'état explicite. Avant SUBMITTED, une opportunité fermée bloque la nouvelle soumission.

## 9. Privacy/rétention
Finalité recrutement explicite, accès par objet/tenant, minimisation, rétention et subject-rights via CNS/policies pays. Les décisions historiques nécessaires restent gouvernées ; aucune rétention infinie par défaut.

## 10. Décision
Un MatchScore/RecommendationScore n'est jamais une décision de recrutement. Toute décision humaine/automatisée applicable doit être identifiée et gouvernée séparément.

Statut final : `APPLICATION-LIFECYCLE-SEMANTICS-CLOSED / COUNTRY-RETENTION-AND-PREPROD-PENDING`.
