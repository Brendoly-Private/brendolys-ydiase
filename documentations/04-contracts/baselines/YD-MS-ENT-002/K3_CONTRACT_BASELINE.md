---
document_id: "YD-DOC-CON-ENT-002-K3-BASELINE"
title: "YD-MS-ENT-002 — K3 Contract Baseline (proposition)"
document_type: "contract-baseline"
document_role: "Prépare la contractualisation K3 de YD-MS-ENT-002, sans attribuer K3 PASS."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
created_at: "2026-10-10"
last_reviewed_at: "2026-10-10"
tags:
  - "contracts"
---

# YD-MS-ENT-002 — Entrepreneurial Opportunity Intelligence — préparation K3

Statut : `K3-DRAFT / NOT-APPROVED / NOT-PASS`. Cette proposition n'enregistre **aucun** nouveau contrat dans le registre canonique.

## Autorité et données
Nature candidate : `DERIVED/MIXED` ; criticité candidate : `C2`.
Agrégats : EntrepreneurialOpportunityHypothesis, OpportunityEvidenceSet, OpportunityAssessmentSnapshot.
Sources gouvernées : LAB/DAT/KNW/CFG. Les données externes sont des références/snapshots sous version et finalité ; jamais des écritures directes dans une base externe.

## Interfaces logiques candidates (IDs à allouer après vérification du Contract Registry)
- **Entrées** : LAB/DAT/KNW/CFG. Le consommateur vérifie autorisation, provenance, version, pays, finalité et fraîcheur selon le cas.
- **Lecture/projection sortante** : hypothèse, evidence refs, version, confidence, freshness. Payload minimum proposé : `resource_ref`, `resource_version`, `status`, `effective_at`, `country_scope`, `source_refs` si applicable ; aucun champ personnel sans purpose/scope.
- **Événements candidats** : Hypothesis publiée/corrigée/expirée/retirée. Enveloppe proposée : `event_id`, `aggregate_ref`, `aggregate_version`, `occurred_at`, `event_type`, `contract_version`, `country_scope`, `trace_ref` ; publication, retrait, correction et révocation doivent être distinguables.
- **Commandes candidates** : créer ou modifier l'agrégat possédé, selon politique métier ; requièrent `request_ref` idempotent, `expected_version`, identité/scope du demandeur et résultat explicite. L'existence de chaque commande reste à confirmer pour YD-MS-ENT-002.

## Invariants contractuels
1. Seul YD-MS-ENT-002 peut modifier ses agrégats ; aucune base interservices partagée.
2. Un événement rejoué ne reproduit pas une action externe irréversible ; consommateur idempotent par `event_id` et version.
3. Un événement ancien ou hors ordre ne réactive pas une donnée retirée ; retrait/révocation prioritaires.
4. Toute sortie dérivée porte provenance, version de calcul, fraîcheur et possibilité d'invalidation ; les données non reconstructibles exigent un plan de restauration distinct.
5. Les règles pays sont contextualisées par CFG ; l'absence de configuration, permission ou preuve requise interdit une publication sensible.
6. Les lectures publiques sont distinctes des informations internes, confidentielles ou personnelles.

## Compatibilité et erreurs
- Version logique majeure en cas de suppression, renommage ou changement sémantique d'un champ requis ; ajout optionnel compatible sous réserve des consommateurs.
- Valeur inconnue : `UNKNOWN/UNSUPPORTED` ou refus contrôlé, jamais interprétation arbitraire.
- Erreurs logiques candidates : `UNAUTHORIZED`, `FORBIDDEN_PURPOSE`, `NOT_FOUND_OR_NOT_VISIBLE`, `VERSION_CONFLICT`, `SOURCE_STALE`, `COUNTRY_UNSUPPORTED`, `WITHDRAWN`, `DEPENDENCY_UNAVAILABLE`. Applicabilité et traitement doivent être validés par opération.
- Une projection possède snapshot, watermark et procédure de rattrapage/reconstruction avant exploitation.

## Exigences à relier et points bloquants
- Matrice exigences fonctionnelles/non fonctionnelles et critères d'acceptation propres à YD-MS-ENT-002 : **à rattacher et vérifier**.
- Liste des IDs existants et futurs dans `CONTRACT_REGISTRY.md`, producteurs, consommateurs et états ACTIVE-LOGICAL : **à arbitrer**.
- ADR de nature `DERIVED/MIXED`, modes synchrones/asynchrones, état autoritatif versus dérivé : **à valider**.
- Règles spécifiques de rétention, consentement, droits de source, territorialité, retrait et classification : **à finaliser**.
- Payloads spécifiques à chaque opération, cardinalités, validations, comportements de refus et compatibilité : **non finalisés**.
- Protocoles, schémas physiques, tests contractuels, IAM physique, RPO/RTO/SLO et restore/rebuild : **non attestés**.

## Verdict
`K3-NOT-PASS`. Le document est une **trame substantielle de contrat logique**, pas une baseline K3 approuvée. Les champs encore indéterminés bloquent explicitement la qualification K3 selon `K3_CONTRACT_GATE.md`.
