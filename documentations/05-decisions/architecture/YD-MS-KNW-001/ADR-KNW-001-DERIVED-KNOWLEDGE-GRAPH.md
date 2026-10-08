---
document_id: "YD-DOC-ADR-ADR-KNW-001-DERIVED-KNOWLEDGE-GRAPH"
title: "ADR-KNW-001 — Knowledge Graph dérivé et reconstructible"
document_type: "architecture-decision-record"
document_role: "Consigne une décision d’architecture et ses conséquences applicables."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "decisions"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# ADR-KNW-001 — Knowledge Graph dérivé et reconstructible

> **Rôle du document**
> Consigne une décision d’architecture et ses conséquences applicables.
> **Usage développement :** référence obligatoire pour les choix d’architecture concernés.

Statut : `ACCEPTED`

## Contexte

YDIASE relie plusieurs autorités métier. Un graphe transversal facilite les relations sémantiques, la recherche enrichie, les analyses et le grounding IA. Donner au graphe la propriété des faits sources créerait toutefois une seconde vérité métier et rendrait les domaines dépendants d'une projection reconstruite.

## Décision

KNW-001 est un composant `DERIVED`.

Il possède uniquement :
- `KnowledgeNodeProjection` ;
- `KnowledgeEdge` ;
- `SemanticAssertion` ;
- `GraphVersion`.

Les autorités métier conservent leurs objets canoniques.

Toute projection KNW conserve source, version, provenance et temporalité applicables.

Toute relation porte une classe parmi `SOURCE-ASSERTED`, `DETERMINISTIC-DERIVED`, `INFERRED`, `CURATED-GRAPH`.

KNW doit pouvoir être reconstruit depuis ses sources et mécanismes de replay/snapshot compatibles.

SRH peut consommer KNW comme enrichissement optionnel. Une panne KNW ne doit pas rendre impossible l'indexation ou la recherche de la vérité publiée par les domaines sources.

Le graphe partagé exclut les données personnelles par défaut. Toute projection personnelle demande une décision Privacy et un contrôle d'accès propres.

## Conséquences

Positives :
- ownership métier non ambigu ;
- reconstruction possible ;
- provenance exploitable par humain et IA ;
- isolation d'une panne KNW ;
- possibilité de faire évoluer les mécanismes de graphe sans réattribuer les autorités métier.

Contraintes :
- gestion explicite des versions et watermarks ;
- propagation des retraits ;
- coût de reconstruction ;
- nécessité de tests de convergence ;
- les consommateurs doivent distinguer fait source et inférence.

## Alternatives rejetées

### KNW comme source canonique globale
Rejetée : duplique l'ownership et concentre trop d'autorité.

### Dépendance synchrone obligatoire à KNW
Rejetée : propage une indisponibilité transversale aux consommateurs.

### Graphe sans provenance détaillée
Rejetée : empêche l'explication, la correction fiable et l'analyse d'impact.

## Références

- `KNOWLEDGE_GRAPH_PROJECTION_POLICY.md`
- `KNW_TO_SEARCH_PROJECTION_CONTRACT.md`
- `K3_CONTRACT_BASELINE.md`
- `PHASE_CLOSURE.md`
