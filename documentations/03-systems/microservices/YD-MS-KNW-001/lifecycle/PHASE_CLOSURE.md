# YD-MS-KNW-001 — Knowledge Graph — Baseline C2

Statut : `DOCUMENTATION-BASELINE-C2 / KNOWLEDGE-GRAPH-SEMANTICS-CLOSED`
Classification : `DERIVED`
Rebuild state : `REBUILD-UNVERIFIED`

## Politiques normatives
- `KNOWLEDGE_GRAPH_PROJECTION_POLICY.md`
- `KNW_TO_SEARCH_PROJECTION_CONTRACT.md`

## Invariants
- aucune vérité métier primaire ;
- nœuds liés aux IDs/versions des owners ;
- relations classées SOURCE-ASSERTED / DETERMINISTIC-DERIVED / INFERRED / CURATED-GRAPH ;
- provenance obligatoire et inférence explicitement distinguée ;
- entity resolution versionnée, aucune fusion sur simple similarité ;
- corrections/retraits/révocations propagés ;
- PII absente du graphe partagé par défaut ;
- FULL/PARTIAL/CATCH_UP reconstructibles ;
- KNW n'est jamais fallback autoritatif ;
- GraphRAG conserve les sources/provenances ;
- SRH peut utiliser KNW comme enrichment mais pas comme source primaire obligatoire.

## Avant REBUILDABLE/ACTIVE
- enregistrer contrats physiques et versions ;
- prouver replay/snapshot source compatible ;
- finaliser ontology/schema versions ;
- définir seuils freshness/confidence ;
- exécuter FULL_REBUILD et comparer convergence ;
- tester DELETE/REVOKE/out-of-order/entity resolution ;
- mesurer RTO/SLO ;
- valider Privacy/access controls.

Statut final : `C2-BASELINE-ESTABLISHED — KNOWLEDGE-GRAPH-SEMANTICS-CLOSED / FULL-REBUILD-AND-PREPROD-EVIDENCE-PENDING`.
