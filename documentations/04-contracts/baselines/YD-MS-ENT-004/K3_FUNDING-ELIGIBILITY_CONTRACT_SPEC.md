---
document_id: "YD-DOC-CON-ENT-FUNDING-ELIGIBILITY-SPEC-V1"
title: "YD-CTR-ENT-FUNDING-ELIGIBILITY-v1 — proposition de contrat logique"
document_type: "contract-specification"
document_role: "Spécifie une interface logique candidate Entrepreneurship en attente d'approbation."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
created_at: "2026-10-11"
last_reviewed_at: "2026-10-11"
tags:
  - "contracts"
---

# YD-CTR-ENT-FUNDING-ELIGIBILITY-v1 — proposition de contrat logique

**Statut : PROPOSED / NOT-REGISTERED / K3-NOT-PASS.** La présente spécification n'est pas un contrat ACTIVE-LOGICAL.

## Parties et autorité
- Producteur/owner : YD-MS-ENT-004.
- Consommateurs candidats : authorized requester only. Chaque accès nécessite finalité et droits vérifiés.
- Type candidat : API. Criticité contractuelle candidate : K1. Privacy candidate : VERY-SENSITIVE.
- Invariant spécifique : Indicative eligibility not award.

## Payload logique candidat
Champs et types proposés : `opportunity_ref:string, rule_version:string, applicant_context_ref:string, assessment:string, evaluated_at:datetime, expires_at:datetime, disclaimer:string`.
Champs métiers candidats requis : `opportunity_ref; rule_version; applicant_context_ref; assessment` ; autres champs conditionnels selon opération. Tous les types, nullabilités, contraintes et cardinalités restent à approuver.
Enveloppe commune : `contract_id`, `contract_version`, `resource_ref`, `resource_version`, `status`, `country_scope`, `effective_at`, `source_refs` si applicable. Pour événement : `event_id`, `occurred_at`, `trace_ref`. Pour commande : `request_ref`, `expected_version`, `actor_scope`.

## Sémantique, erreurs et retrait
Opérations/états candidats : assess; forbidden_purpose; stale_rule; incomplete_evidence.
- Écriture uniquement sur agrégat du producteur ; contrôle d'accès et finalité avant lecture personnalisée.
- Répétition : `event_id` / `request_ref` idempotents ; les versions antérieures ne restaurent jamais un état retiré.
- `WITHDRAW` retire la publication ; `REVOKE` retire le droit d'accès et invalide les projections concernées ; `DELETE` suit politique de conservation et audit applicable. Les délais et droits restent à définir.
- Projection : snapshot + watermark + catch-up ; refus contrôlé si source, permission ou version requise indisponible.
- Erreurs logiques communes : `UNAUTHORIZED`, `FORBIDDEN_PURPOSE`, `NOT_FOUND_OR_NOT_VISIBLE`, `VERSION_CONFLICT`, `SOURCE_STALE`, `COUNTRY_UNSUPPORTED`, `WITHDRAWN`, `DEPENDENCY_UNAVAILABLE`. Applicabilité par opération non encore ratifiée.

## Versionnement et compatibilité
- Version logique `v1` candidate. Ajout optionnel sous compatibilité prouvée ; suppression/renommage/changement de sens d'un requis => nouvelle majeure.
- Enum inconnue : `UNKNOWN/UNSUPPORTED` ou refus, jamais interprétation implicite.
- Migration/dépréciation et fenêtre de coexistence à approuver avant mise en service.

## Conditions de promotion au registre
1. Confirmer ownership, consommateurs, base légale/finalité, classification Privacy et politique pays.
2. Ratifier types, champs requis, contraintes, états, erreurs, replay et suppression pour chaque opération.
3. Relier les exigences et ADR, notamment séparation AUTH/DERIVED et provenance.
4. Vérifier le respect des contrats transversaux CFG/CNS/AUD et la source autoritative.
5. Faire revue humaine, puis enregistrer dans `documentations/04-contracts/indexes/CONTRACT_REGISTRY.md` avec statut approuvé.

**Verdict : K3-NOT-PASS.** Aucun protocole, schéma physique ou preuve d'exécution n'est prétendu.


## Traçabilité métier et critères de revue — 2026-10-11

Référence candidate : `documentations/02-domains/entrepreneurship/EXIGENCES_METIER_K3.md` (DRAFT, exigences non enregistrées dans le référentiel canonique).

- Exigences candidates associées : `ENT4-REQ-002`, `ENT4-REQ-003`.
- Champs de contrôle à rattacher aux opérations : `assessment, rule_version, applicant_context_ref, disclaimer`.
- Scénarios de vérification à formaliser : CNS fail-closed, no lender decision.
- Exigences transversales à vérifier : `YD-REQ-GOV-001`, `YD-REQ-GOV-002` si données personnelles, `YD-REQ-DATA-001`, `YD-REQ-IAM-003`, `YD-REQ-CTR-001`, `YD-REQ-CTY-001`.
- Preuve manquante : validation des exigences métier, décision Privacy/CNS applicable, validation des contraintes champ par champ et tests contractuels ; **aucune preuve d'exécution**.

**Verdict inchangé : PROPOSED / NOT-REGISTERED / K3-NOT-PASS.**
