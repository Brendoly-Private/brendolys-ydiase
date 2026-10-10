---
document_id: "YD-DOC-SYS-ARC-ENT-K3-OWNERSHIP-ARBITRAGE"
title: "Entrepreneurship — Arbitrages préparatoires K3"
document_type: "architecture-review"
document_role: "Trace les arbitrages proposés et les points de validation des contrats Entrepreneurship."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
created_at: "2026-10-10"
last_reviewed_at: "2026-10-10"
tags:
  - "systems"
  - "architecture"
---

# Entrepreneurship — Arbitrages préparatoires K3

Statut : `PROPOSED / NOT-APPROVED / K3-NOT-PASS`.

## Références autoritatives
- `documentations/02-domains/entrepreneurship/FRONTIERES_ET_DEPENDANCES.md`
- `documentations/03-systems/architecture/target/ENTREPRENEURSHIP_DEPENDENCY_OWNERSHIP_MAP.md`
- `documentations/03-systems/architecture/reviews/ENTREPRENEURSHIP_DDD_REVIEW.md`
- `documentations/04-contracts/indexes/CONTRACT_REGISTRY.md`
- `documentations/_meta/maturity/gates/K3_CONTRACT_GATE.md`

Ce document propose des précisions sans supplanter les sources canoniques. Les IDs de contrats ci-dessous sont **proposés, non enregistrés dans le Contract Registry**, et ne peuvent pas être utilisés comme contrats ACTIVE-LOGICAL.

## Arbitrages proposés

| Frontière | État autoritatif propre | État dérivé / projeté | Décision proposée et justification |
|---|---|---|---|
| ENT-001 | Venture et son cycle de vie | références PRF/SKL autorisées | AUTH : identité projet séparée de l'identité personne |
| ENT-002 | éventuels paramètres/annotations éditoriales validés, à confirmer | hypothèses, jeux de preuves et assessments recalculables | DERIVED par défaut ; MIXED seulement si état métier irréconstructible réellement identifié et gouverné |
| ENT-003 | programmes, offres et ressources édités/validés par ENT | SupportOrganizationProjection issue de PRT | AUTH pour catalogue ENT ; projection non autoritative sur les partenaires |
| ENT-004 | fiches de catalogue et règles publiées/validées dans ENT | EligibilitySnapshot et décision externe référencée | AUTH/MIXED : l'autorité porte sur la publication YDIASE, jamais sur l'octroi de financement |
| ENT-005 | TeamNeed et paramètres de visibilité propres au projet, sous autorisation | FounderMatchRun, scores et explications recalculables | MIXED : état métier conservé, calcul dérivé soumis à révocation |
| ENT-006 | plans, hypothèses, expérimentations, jalons et résultats du projet | ProgressSnapshot recalculable | AUTH : progression distincte de l'identité Venture |

## Invariants interservices à contractualiser

1. Chaque ressource publiée porte owner, ID stable, version, statut, contexte pays et source/provenance applicable.
2. Toute commande d'écriture est contrôlée par scope et version d'agrégat ; répétition idempotente ; conflit explicite.
3. Toute projection doit gérer création, correction, retrait, suppression/révocation, événements désordonnés et rattrapage versionné.
4. ENT-002 n'invente pas des vérités économiques ; ENT-004 ne décide pas du financement ; ENT-005 n'expose pas les personnes sans visibilité/consentement.
5. Le pays pilote Burkina Faso n'autorise pas de règles globales implicites ; CFG gouverne la configuration territoriale.
6. Les dépendances PRF/SKL/CNS/PRT/LAB/DAT/KNW restent propriétaires de leurs données ; aucun accès direct aux bases.

## Décisions encore requises pour K3

- Valider ou rejeter les qualifications proposées, surtout l'état non reconstructible de ENT-002 et ENT-005.
- Identifier pour chaque contrat logique les producteurs, consommateurs, payloads minimaux, opérations/événements, erreurs, retrait, temporalité et versions, et enregistrer les IDs canoniques dans le Contract Registry.
- Fixer les politiques de visibilité, conservation, source/licence, et exigences de compatibilité par type de donnée.
- Rattacher les décisions structurelles non triviales à un ADR approuvé ; aucun `UNKNOWN` ne peut être traité comme PASS.
- Vérifier les exigences et les dépendances contre les baselines de domaines et les normes de gouvernance.

## Verdict
`K3-PREPARATION-ONLY`. Aucun changement d'ownership canonique ni statut K3 PASS n'est décidé par cette revue.
