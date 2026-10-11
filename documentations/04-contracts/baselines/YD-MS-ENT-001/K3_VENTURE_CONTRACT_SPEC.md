---
document_id: "YD-DOC-CON-ENT-VENTURE-SPEC-V1"
title: "YD-CTR-ENT-VENTURE-v1 — proposition de contrat logique"
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

# YD-CTR-ENT-VENTURE-v1 — proposition de contrat logique

**Statut : PROPOSED / NOT-REGISTERED / K3-NOT-PASS.** La présente spécification n'est pas un contrat ACTIVE-LOGICAL.

## Parties et autorité
- Producteur/owner : YD-MS-ENT-001.
- Consommateurs candidats : ENT-005/ENT-006/ORI autorisés. Chaque accès nécessite finalité et droits vérifiés.
- Type candidat : HYBRID. Criticité contractuelle candidate : K1. Privacy candidate : SENSITIVE.
- Invariant spécifique : Venture identity and visibility.

## Payload logique candidat
Champs et types proposés : `venture_ref:string, stage:string, state:string, resource_version:int, visibility_scope:string`.
Champs métiers candidats requis : `venture_ref; stage/state; visibility_scope` ; autres champs conditionnels selon opération. Tous les types, nullabilités, contraintes et cardinalités restent à approuver.
Enveloppe commune : `contract_id`, `contract_version`, `resource_ref`, `resource_version`, `status`, `country_scope`, `effective_at`, `source_refs` si applicable. Pour événement : `event_id`, `occurred_at`, `trace_ref`. Pour commande : `request_ref`, `expected_version`, `actor_scope`.

## Sémantique, erreurs et retrait
Opérations/états candidats : create/update/withdraw; version_conflict; not_visible.
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

- Exigences candidates associées : `ENT1-REQ-001`, `ENT1-REQ-002`, `ENT1-REQ-003`.
- Champs de contrôle à rattacher aux opérations : `VentureRef, resource_version, visibility_scope`.
- Scénarios de vérification à formaliser : version conflict, withdrawal, object authorization.
- Exigences transversales à vérifier : `YD-REQ-GOV-001`, `YD-REQ-GOV-002` si données personnelles, `YD-REQ-DATA-001`, `YD-REQ-IAM-003`, `YD-REQ-CTR-001`, `YD-REQ-CTY-001`.
- Preuve manquante : validation des exigences métier, décision Privacy/CNS applicable, validation des contraintes champ par champ et tests contractuels ; **aucune preuve d'exécution**.

**Verdict inchangé : PROPOSED / NOT-REGISTERED / K3-NOT-PASS.**


## Proposition détaillée des opérations v1 — revue d'approbation

Les opérations ci-dessous sont des **commandes et lectures logiques candidates** ; elles n'imposent ni HTTP, ni gRPC, ni broker. Les noms, valeurs et cardinalités restent soumis à l'approbation des owners.

| Opération candidate | Entrée requise proposée | Sortie / effet | Refus explicites |
|---|---|---|---|
| CreateVenture | request_ref, actor_scope, country_scope, initial_visibility, purpose_ref si personnel | venture_ref nouveau, resource_version=1, état initial, effective_at | UNAUTHORIZED, FORBIDDEN_PURPOSE, COUNTRY_UNSUPPORTED, VALIDATION_FAILED |
| GetVenture | venture_ref, actor_scope, purpose_ref si personnel | projection filtrée par visibilité, resource_version | NOT_FOUND_OR_NOT_VISIBLE, FORBIDDEN_PURPOSE, WITHDRAWN |
| ChangeVentureStage | venture_ref, expected_version, request_ref, actor_scope, stage cible | nouvel état/version ou conflit sans mutation | VERSION_CONFLICT, INVALID_TRANSITION, UNAUTHORIZED |
| UpdateVentureVisibility | venture_ref, expected_version, request_ref, actor_scope, visibility_scope | nouvelle version et invalidation des projections exposées | VERSION_CONFLICT, UNAUTHORIZED, FORBIDDEN_PURPOSE |
| WithdrawVenture | venture_ref, expected_version, request_ref, actor_scope, reason_code | état retiré, nouvelle version, notification logique de retrait | VERSION_CONFLICT, UNAUTHORIZED, ALREADY_WITHDRAWN |

### Contrat de données candidat — cardinalités

| Champ | Type logique | Cardinalité candidate | Autorité | Contraintes et visibilité |
|---|---|---|---|---|
| venture_ref | opaque string | 1 | ENT-001 | stable, non réutilisable, non dérivé d'un identifiant PRF |
| resource_version | positive integer | 1 | ENT-001 | strictement croissante par agrégat |
| stage | controlled enum | 1 | ENT-001 | liste de valeurs et transitions **à ratifier** |
| state | controlled enum | 1 | ENT-001 | état retiré non réactivé par replay ancien |
| visibility_scope | governed enum/ref | 1 | ENT-001 sous contraintes CNS | accès filtré par objet et finalité |
| country_scope | country code/ref | 1..n | CFG pour activation ; ENT pour portée de Venture | aucune activation pays implicite |
| team_refs | opaque external refs | 0..n | ENT-001 pour liens ; PRF pour identité des personnes | aucune donnée personnelle brute par défaut |
| purpose_ref | governed reference | 1 si traitement personnel | CNS | validité, restrictions et décision contrôlées |
| effective_at | datetime UTC | 1 | ENT-001 | date d'effet métier, distincte de occurred_at |

### Enveloppe des événements candidats

`VentureCreated`, `VentureStageChanged`, `VentureVisibilityChanged`, `VentureWithdrawn` : `event_id`, `venture_ref`, `aggregate_version`, `event_type`, `occurred_at`, `effective_at`, `country_scope`, `contract_version`, `trace_ref`. Les champs d'identité des personnes ne sont pas diffusés par défaut. Un événement de visibilité/retrait exige une invalidation des vues concernées ; les consommateurs appliquent version et idempotence.

### Exemples de vérification documentaire et de tests futurs

1. Deux `CreateVenture` avec le même `request_ref` ne produisent qu'un seul Venture ; avec des références distinctes, un même acteur autorisé peut gérer deux Ventures.
2. `ChangeVentureStage` avec une version périmée refuse sans altérer l'agrégat.
3. Un consommateur ORI non autorisé ne reçoit ni `team_refs` ni détails du Venture ; l'existence même peut être masquée.
4. Après `WithdrawVenture`, un événement `VentureCreated` ancien rejoué ne restaure pas la visibilité.
5. Sans décision CNS obligatoire vérifiable ou sans configuration pays valide, le traitement personnel concerné échoue fermé.

### Questions de validation avant promotion

- Qui peut créer, modifier, partager ou retirer un Venture (rôles et délégation), et quels états métier `stage/state` sont permis ?
- `country_scope` est-il multi-pays dès v1 ou un pays primaire avec extensions explicites ?
- Quelles catégories de `team_refs` sont autorisées et selon quelle finalité CNS ?
- Quelles règles de conservation et de suppression s'appliquent à l'historique des Ventures et aux références externes ?
- Quels consommateurs précis reçoivent quels événements, selon quelle politique de projection et de retrait ?

**Statut : proposition détaillée à arbitrer ; aucune réponse ni approbation n'est supposée. K3-NOT-PASS.**
