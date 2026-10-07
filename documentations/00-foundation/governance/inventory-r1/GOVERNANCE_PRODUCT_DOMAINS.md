---
document_id: "YD-DOC-FND-INV-006"
title: "R1 — Governance, Product & Domains Inventory"
document_type: "governance-product-domain-inventory"
document_role: "Inventorie la gouvernance, les fondations produit et les domaines métier pour préparer leur migration structurelle."
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

# R1 — Governance, Product & Domains Inventory

> **Rôle du document**
> Inventorie la gouvernance, les fondations produit et les domaines métier pour préparer leur migration structurelle.
> **Usage développement :** vue d’inventaire et d’orientation ; elle ne crée pas de vérité normative.

Statut : `ACTIVE-R1`

## Gouvernance
| Objet/famille | Type | Disposition | Destination | Preuve |
|---|---|---|---|---|
| README racine | README/INDEX | REFERENCE | knowledge-index/START_HERE | P-SEARCHED |
| REGISTRE_DOCUMENTAIRE.md | REGISTRY historique/partiel | REVIEW | governance/registries | P-FETCHED |
| CHARTE_DOCUMENTAIRE.md | CONSTITUTION | GROUP | governance/constitution | P-SEARCHED |
| NIVEAUX_AUTORITE.md | STANDARD | GROUP | governance/constitution | P-SEARCHED |
| CONVENTION_IDENTIFIANTS.md | STANDARD | GROUP | governance/conventions | P-SEARCHED |
| CYCLE_VIE_DOCUMENTAIRE.md | STANDARD | GROUP | governance/constitution | P-SEARCHED |
| POLITIQUE_*.md | POLICY | GROUP | governance/policies | P-SEARCHED |
| REGISTRE_*.md | REGISTRY | GROUP/REVIEW | governance/registries | P-SEARCHED |
| AUTORITATIVE_SOURCE_REGISTRY.md | REGISTRY normatif ownership | KEEP→MOVE | governance/registries | P-FETCHED |
| MATRICE_TRACABILITE.md | MATRIX | MOVE | governance/traceability | P-SEARCHED |
| templates/* | TEMPLATE | KEEP | governance/templates | P-SEARCHED |

## Fondations produit
| Famille | Type | Destination |
|---|---|---|
| VISION_* / CHARTE_FONDATRICE | PRODUCT-VISION | product/vision |
| PROBLEMES_ET_BESOINS | PRODUCT-DISCOVERY | product/problems-needs |
| PROPOSITION_VALEUR | PRODUCT-STRATEGY | product/value |
| SEGMENTS_UTILISATEURS / PARTIES_PRENANTES | ACTOR-MODEL | product/actors-segments |
| CARTE_DOMAINES | DOMAIN-CATALOG | domains + knowledge-index |
| CAPACITES_PRODUIT | CAPABILITY-CATALOG | product/capabilities + knowledge-index |
| PERIMETRE_PRODUIT | PRODUCT-SCOPE | product/scope |
| MODELE_ECONOMIQUE | PRODUCT-ECONOMICS | product/value-economics |
| CRITERES_SUCCES | PRODUCT-METRICS | product/success |
| HORIZONS_PRODUIT / PILOTE_BURKINA | PRODUCT-HORIZON | product/horizons + delivery |
| PRINCIPES_PRODUIT / DOCTRINE_PERENNITE | PRODUCT-POLICY | product/principles |
| HYPOTHESES_ET_INCONNUES | REGISTER | governance/registries + product reference |

## Domaines métier
Les 10 domaines définis par CARTE_DOMAINES restent les racines métier. Leur faible profondeur ne justifie aucune fusion.

Types locaux attendus lorsqu'ils existent :
- README → INDEX
- MODELE_DOMAINE → DOMAIN-MODEL
- REGLES_METIER → DOMAIN-POLICY
- FRONTIERES_ET_DEPENDANCES → DOMAIN-INTERACTION
- CAPACITES_ET_TRACABILITE → CAPABILITY/TRACEABILITY
- GATES_ET_INCONNUES → VALIDATION/OPEN-QUESTIONS
- documents de temporalité/provenance/visibilité → DOMAIN-POLICY ou DOMAIN-MODEL selon contenu.

Identity (02) est déjà assez riche pour GROUP en sous-dossiers model/rules/capabilities/interactions/validation.
Les autres domaines restent KEEP jusqu'à croissance réelle.

R2 devra résoudre les documents multi-vues par référence, pas par duplication.
