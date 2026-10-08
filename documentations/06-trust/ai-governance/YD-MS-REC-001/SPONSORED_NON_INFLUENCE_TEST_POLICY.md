---
document_id: "YD-DOC-TRU-REC-001-SPONSORED-NON-INFLUENCE-TEST-POLICY"
title: "REC-001 — Sponsored Non-Influence Test Policy"
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

# REC-001 — Sponsored Non-Influence Test Policy

> **Rôle du document**
> Établit une règle normative de gouvernance, confiance ou données applicable au périmètre concerné.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-TEST-BASELINE / PREPROD-EXECUTION-PENDING`

## Invariant
À entrées métier, policy et modèle identiques, ajouter, retirer ou modifier une campagne SPN ne doit changer aucun résultat organique REC.

## Oracle de comparaison
Deux runs A/B sont comparables si subject/context, purpose, candidate inventory, evidence snapshot métier, policy/model versions, seed/determinism controls applicables et temps logique sont identiques. Les sorties organiques doivent être identiques : eligibility, exclusions, scoring components, organic_score, organic_rank, tie-break result, uncertainty et explanation facts.

Les identifiants techniques, timestamps d'exécution et traces non sémantiques peuvent différer.

## Tests obligatoires

| ID | Mutation SPN | Résultat organique attendu |
|---|---|---|
| SPN-NI-001 | aucune campagne → campagne active | invariance totale |
| SPN-NI-002 | budget 0 → budget élevé | invariance totale |
| SPN-NI-003 | enchère/prix modifié | invariance totale |
| SPN-NI-004 | partenaire non sponsor → sponsor | invariance totale |
| SPN-NI-005 | sponsor A → sponsor B | invariance totale |
| SPN-NI-006 | campagne suspendue/réactivée | invariance totale |
| SPN-NI-007 | plusieurs sponsors concurrents | invariance totale |
| SPN-NI-008 | sponsor aussi candidat organique | score/rang organiques inchangés |
| SPN-NI-009 | insertion UI sponsor avant rang 1 | organic_rank inchangé |
| SPN-NI-010 | suppression de tous placements sponsorisés | organique inchangé |
| SPN-NI-011 | panne/timeout SPN | REC organique continue ou suit sa propre policy ; jamais reranking commercial |
| SPN-NI-012 | payload SPN tente score/weight/rank | champ rejeté/ignoré + audit |
| SPN-NI-013 | config commerciale tente d'entrer dans RecommendationPolicy | validation/CI refuse |
| SPN-NI-014 | explication sponsorisée tente imitation organique | présentation refuse la confusion et conserve label sponsorisé |

## Tests d'architecture
- aucun budget, bid, commission, campaign_ref ou sponsored status dans les features du scoring organique ;
- aucune permission SPN d'écriture sur datastore/API de score REC ;
- aucune RecommendationPolicyVersion modifiable par identité SPN ;
- contrats interservices n'exposent pas de commande `boostOrganicRank` ou équivalent ;
- observabilité sépare métriques organiques et sponsorisées.

## Test de propriété
Pour un ensemble de scénarios générés, toute mutation exclusivement commerciale doit satisfaire :
`OrganicResult(inputs_business, policy, model, spn_state_A) = OrganicResult(inputs_business, policy, model, spn_state_B)`.

Si le modèle est non déterministe, comparaison sous contrôles reproductibles approuvés ou tolérance portant uniquement sur stochasticité intrinsèque démontrée, jamais sur l'état SPN.

## Preuves préproduction
Chaque test conserve versions, fixtures, hashes/snapshots d'entrée, sorties comparées, diff, identité d'exécution, timestamp et résultat PASS/FAIL.

Tout changement touchant REC scoring/ranking, SPN, BIL/MKT commercial ou composition UI relance la suite pertinente.

## Gate
Un seul FAIL de non-influence est `RELEASE-BLOCKING`. Aucune dérogation commerciale ne peut le convertir en non-bloquant.

Statut final : `SPONSORED-NON-INFLUENCE-TESTS-DEFINED / EXECUTION-PENDING`.
