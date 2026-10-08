---
document_id: "YD-DOC-POL-KNW-001-KNOWLEDGE-GRAPH-PROJECTION"
title: "YD-MS-KNW-001 — Knowledge Graph Projection Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de knowledge graph projection pour YD-MS-KNW-001."
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
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-KNW-001 — Knowledge Graph Projection Policy

> **Rôle du document**
> Établit les règles normatives de knowledge graph projection pour YD-MS-KNW-001.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / REBUILD-EVIDENCE-PENDING`
Classification : `DERIVED`
Criticité : `C2`

## 1. Mission

KNW-001 construit une vue relationnelle dérivée des autorités YDIASE afin de permettre navigation sémantique, raisonnement relationnel borné, retrieval et analyses.

Le graphe est un **read model reconstructible**. Il n'est jamais la source primaire d'une Institution, Program, Skill, Occupation, LaborSignal, Opportunity ou autre objet métier.

## 2. Objets

KNW possède uniquement ses artefacts dérivés :
- `KnowledgeNodeProjection` ;
- `KnowledgeEdge` ;
- `SemanticAssertion` ;
- `GraphVersion`.

Chaque nœud projeté conserve `source_domain`, `source_ref`, `source_version`, état source/publication applicable et watermark.

## 3. Classes de relations

Toute relation est classée :
- `SOURCE-ASSERTED` : explicitement publiée par une autorité métier ;
- `DETERMINISTIC-DERIVED` : calculée par une règle déterministe versionnée ;
- `INFERRED` : produite par algorithme/modèle/règle probabiliste ;
- `CURATED-GRAPH` : relation sémantique propre au graphe, gouvernée et sourcée.

Une relation `INFERRED` ne devient jamais `SOURCE-ASSERTED` sans validation/publication par l'autorité compétente.

## 4. Provenance

Chaque edge/assertion conserve au minimum :
- source refs/versions ;
- provenance/evidence refs DAT lorsque pertinentes ;
- derivation/rule/model version ;
- produced_at ;
- graph_version ;
- confidence/quality lorsque applicable ;
- territory/temporal scope ;
- validity/freshness.

Une relation sans provenance suffisante pour sa classe n'est pas exposée comme relation fiable.

## 5. Identité des nœuds

Les IDs métier stables des domaines sont référencés, jamais remplacés par un identifiant graphe présenté comme canonique.

Le merge/entity resolution conserve les refs sources et une `resolution_version`. Une similarité de noms ne suffit jamais à fusionner deux entités.

## 6. Temporalité

Le graphe respecte effective dates, versions et retraits sources. Une nouvelle version ne réécrit pas silencieusement l'historique.

Les requêtes "courantes" excluent les projections expirées/retirées selon policy ; les requêtes historiques indiquent la version temporelle utilisée.

## 7. Suppression et révocation

DELETE, WITHDRAW, REVOKE ou restriction source se propagent au sous-graphe concerné. Une relation dépendant d'un nœud retiré est supprimée, invalidée ou rendue non exposable selon sa sémantique.

Aucun nœud orphelin ne doit continuer à rendre découvrable un objet qui n'est plus publiable.

## 8. Privacy

PII minimisée. Les données personnelles ne sont pas intégrées au graphe général simplement parce qu'elles existent dans PRF/SKL.

Toute projection personnelle exige finalité, autorisation CNS, segmentation d'accès et politique de suppression/reconstruction. Par défaut, le graphe de connaissance partagé privilégie les connaissances non personnelles.

## 9. Rebuild

Modes : `FULL_REBUILD`, `PARTIAL_REBUILD`, `CATCH_UP`.

Chaque GraphVersion conserve source watermarks, projection/rule versions, started/completed_at, integrity report et freshness.

Un FULL_REBUILD doit converger vers le même état logique que replay/catch-up pour un même snapshot source, hors métadonnées techniques non déterministes.

## 10. Panne

Une version précédente peut être servie uniquement si son état est `FRESH` ou `STALE-ACCEPTABLE` pour l'usage concerné. `EXPIRED` ou `UNKNOWN` ne sont jamais présentés comme actuels.

Le graphe ne devient jamais fallback autoritatif lorsqu'un domaine source est indisponible.

## 11. IA / GraphRAG

AI-002 peut utiliser KNW pour grounding/navigation, mais chaque fait retourné doit rester relié à ses sources/provenances.

Une inférence LLM ne peut écrire directement une relation autoritative. Toute proposition d'enrichissement passe par une classe `INFERRED`/workflow de validation.

## 12. Gates

`DEFINED` : derived-only, classes de relations, provenance, identity resolution, temporalité, deletion/revocation, Privacy, rebuild/convergence, freshness, GraphRAG boundary.

`TBD-PREPROD` : contrats physiques, ontology/schema versions, seuils de confidence, retention/replay, FULL_REBUILD mesuré, RTO/SLO, tests d'intégrité et d'accès.

Statut final : `KNOWLEDGE-GRAPH-SEMANTICS-CLOSED / FULL-REBUILD-AND-PREPROD-EVIDENCE-PENDING`.
