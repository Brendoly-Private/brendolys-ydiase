---
document_id: "YD-DOC-FND-INV-001"
title: "R1 — Architecture, Contracts & Decisions Inventory"
document_type: "migration-inventory-view"
document_role: "Inventorie et classe les documents d’architecture, contrats, décisions, ownership et recovery pour guider leur restructuration."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "view"
canonical: false
development_usage: "informational"
owners:
  - "Documentation Governance"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "foundation"
  - "documentation-migration"
---

# R1 — Architecture, Contracts & Decisions Inventory

> **Rôle du document**
> Inventorie et classe les documents d’architecture, contrats, décisions, ownership et recovery pour guider leur restructuration.
> **Usage développement :** vue d’inventaire et d’orientation ; elle ne crée pas de vérité normative.

Statut : `ACTIVE-R1`

## Vue système
- ARCHITECTURE_CIBLE.md → ARCHITECTURE-TARGET → system-architecture/overview
- ARCHITECTURE_LOGIQUE.md → ARCHITECTURE-DESIGN → system-architecture/overview
- 13-architecture/README.md → INDEX → system-architecture

## DDD / reviews
- DDD_REVIEW.md → REVIEW
- MICROSERVICE_BOUNDARY_REVIEW.md → REVIEW+BOUNDARY-DECISION-BASELINE
- SENSITIVE_MERGER_REVIEW.md → REVIEW
- TRANSVERSAL_ARCHITECTURE_REVIEW_48.md → REVIEW

Destination : system-architecture/ddd|reviews. R2 doit séparer propositions historiques et décisions encore actives.

## Ownership / autonomie / dépendances
- DATA_OWNERSHIP_MATRIX.md → MATRIX
- DEPENDENCY_MAP.md → ARCHITECTURE-MAP
- AUTONOMY_PROFILE_REGISTER.md → REGISTRY canonique d'index
- AUTONOMY_CLOSURE_MATRIX.md → VALIDATION-MATRIX
- MICROSERVICE_AUTONOMY_STANDARD.md → STANDARD

## Contrats
- CONTRACT_REGISTRY.md → CONTRACT-REGISTRY
- CONTRACT_V1_VALIDATION_MATRIX.md → VALIDATION-MATRIX
- EVENT_MAP.md → EVENT-CATALOG/MAP

Destination conceptuelle : contracts/{registry,events,compatibility,validation}.

## Décisions
- ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md → DECISION/ADR
- ADR-PRF002-RPO-RTO.md → DECISION/ADR
- D3_BLOCKING_CLOSURE_DECISIONS.md → DECISION-SET

Destination : decisions/architecture.

## Recovery dérivé
- DERIVED_RECOVERY_REGISTER.md → REGISTRY
- politiques rebuild/projection locales → restent proches des frontières
- preuves FULL_REBUILD → evidence/rebuild

Règle : le registre transverse référence les règles locales ; il ne les duplique pas.
