---
document_id: "YD-DOC-CON-ENT-FOUNDER-MATCH-SPEC-V1"
title: "YD-CTR-ENT-FOUNDER-MATCH-v1 — proposition de contrat logique"
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

# YD-CTR-ENT-FOUNDER-MATCH-v1 — proposition de contrat logique

**Statut : PROPOSED / NOT-REGISTERED / K3-NOT-PASS.** La présente spécification n'est pas un contrat ACTIVE-LOGICAL.

## Parties et autorité
- Producteur/owner : YD-MS-ENT-005.
- Consommateurs candidats : consenting founder/requester. Chaque accès nécessite finalité et droits vérifiés.
- Type candidat : HYBRID. Criticité contractuelle candidate : K1. Privacy candidate : VERY-SENSITIVE.
- Invariant spécifique : No PRF/SKL writes, no automatic contact disclosure.

## Payload logique candidat
Champs et types proposés : `match_ref:string, need_ref:string, explanation:string, evidence_version:string, consent_scope:string, expires_at:datetime, resource_version:int`.
Champs métiers candidats requis : `match_ref; need_ref; evidence_version; consent_scope; expires_at` ; autres champs conditionnels selon opération. Tous les types, nullabilités, contraintes et cardinalités restent à approuver.
Enveloppe commune : `contract_id`, `contract_version`, `resource_ref`, `resource_version`, `status`, `country_scope`, `effective_at`, `source_refs` si applicable. Pour événement : `event_id`, `occurred_at`, `trace_ref`. Pour commande : `request_ref`, `expected_version`, `actor_scope`.

## Sémantique, erreurs et retrait
Opérations/états candidats : compute/expire/revoke; consent_revoked; stale_evidence.
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
