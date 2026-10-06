# YD-MS-KNW-001 — K3 Contract Baseline

Statut : `K3-CONTRACT-BASELINE / IMPLEMENTATION-PENDING`

## 1. Portée

Ce document ferme la connaissance contractuelle de KNW-001 sans prétendre qu'un contrat physique, du code ou un déploiement existe.

KNW-001 reste un read model DERIVED et reconstructible. Il ne devient jamais autorité d'un fait métier primaire.

## 2. Familles contractuelles

### Entrées autoritatives

KNW consomme des publications versionnées provenant des domaines autoritatifs, notamment Education et Skills. Chaque entrée doit porter au minimum :
- `source_domain` ;
- `source_ref` ;
- `source_version` ;
- `operation` ;
- `effective_at` ou temporalité applicable ;
- état de publication/visibilité applicable ;
- provenance/evidence refs lorsque disponibles ;
- replay/watermark permettant la reconstruction.

Opérations reconnues : `UPSERT`, `DELETE`, `WITHDRAW`, `REVOKE`.

Une entrée inconnue ou incompatible ne doit jamais être interprétée silencieusement.

### Sortie Search

Contrat logique existant : `YD-CTR-KNW-SRH-SEARCH-ENRICHMENT-v1`.

Il reste optionnel pour SRH et ne remplace aucune publication autoritative indexable.

### Sorties Knowledge

Les consommateurs peuvent lire des projections KNW uniquement avec leur classe sémantique et leur provenance. Une sortie minimale expose selon l'objet :
- `graph_version` ;
- `source_ref/source_version` ;
- `relation_type` ;
- `relation_class` ;
- refs de provenance ;
- `derivation_version` si dérivée ;
- `confidence` si applicable ;
- portée territoriale/temporelle ;
- état de fraîcheur.

## 3. Contrat de données

Objets possédés :
- `KnowledgeNodeProjection` ;
- `KnowledgeEdge` ;
- `SemanticAssertion` ;
- `GraphVersion`.

### KnowledgeNodeProjection

Doit conserver identité source, version source, domaine source, état de visibilité applicable, watermark et version de résolution si une résolution d'entité intervient.

### KnowledgeEdge / SemanticAssertion

Doit conserver sujet, relation, objet, classe de relation, provenance, versions sources, version de dérivation/règle/modèle, temporalité et qualité/confidence lorsque applicable.

### GraphVersion

Doit conserver les watermarks sources, versions de projection/règles, début/fin de construction, état d'intégrité et fraîcheur.

## 4. Invariants contractuels

- Aucune vérité métier primaire n'est créée par KNW.
- Une relation `INFERRED` ne devient pas `SOURCE-ASSERTED` sans publication par l'autorité compétente.
- Les IDs métier stables restent les références canoniques.
- Une similarité de nom ne suffit jamais pour fusionner deux entités.
- DELETE/WITHDRAW/REVOKE doivent invalider ou retirer les projections dépendantes.
- Un objet non publiable ne reste pas découvrable via un nœud orphelin.
- Une projection sans provenance suffisante ne peut pas être présentée comme relation fiable.
- Le graphe partagé n'intègre pas de PII par défaut.
- KNW ne sert jamais de fallback autoritatif.

## 5. Exigences traçables

| ID | Exigence | Source principale |
|---|---|---|
| KNW-REQ-001 | Construire uniquement une projection dérivée des autorités | KNOWLEDGE_GRAPH_PROJECTION_POLICY §1-2 |
| KNW-REQ-002 | Conserver provenance et versions pour chaque relation exposable | §4 |
| KNW-REQ-003 | Classer chaque relation selon sa sémantique | §3 |
| KNW-REQ-004 | Respecter versions, dates effectives et retraits | §6-7 |
| KNW-REQ-005 | Rendre FULL_REBUILD, PARTIAL_REBUILD et CATCH_UP possibles | §9 |
| KNW-REQ-006 | Préserver les frontières Privacy | §8 |
| KNW-REQ-007 | Maintenir GraphRAG relié aux sources | §11 |
| KNW-REQ-008 | Permettre à SRH de fonctionner sans KNW | KNW_TO_SEARCH_PROJECTION_CONTRACT §1, §6 |
| KNW-REQ-009 | Rejeter ou isoler un contrat entrant incompatible plutôt que l'interpréter silencieusement | K3 baseline |
| KNW-REQ-010 | Propager les retraits selon la sémantique de dépendance | KNOWLEDGE_GRAPH_PROJECTION_POLICY §7 |

## 6. Versionnement

- Tout contrat exposé possède un identifiant stable et une version majeure.
- Ajout optionnel rétrocompatible : version mineure documentaire ou schema compatible.
- Suppression, changement de sens, changement d'ownership ou champ obligatoire incompatible : nouvelle version majeure.
- Une `GraphVersion` ne remplace pas la version du contrat.
- Les versions de règle/modèle/ontology/schema sont conservées séparément des versions des sources.
- Un consommateur doit pouvoir identifier la version qu'il traite.

## 7. Compatibilité et dépréciation

- Aucun producteur ne retire une version consommée sans période de migration définie.
- Pendant une migration, deux versions peuvent coexister si leur sémantique reste non ambiguë.
- Un payload futur inconnu ne doit pas modifier silencieusement une projection existante.
- Les opérations de retrait ont priorité sur l'enrichissement et le recalcul.
- Une version non supportée est rejetée ou placée en quarantaine selon l'implémentation future.
- La durée de coexistence physique reste `TBD-PREPROD`.

## 8. Décisions structurelles nécessitant ADR

Les décisions suivantes sont considérées structurelles :
- KNW comme read model DERIVED, jamais autorité métier ;
- provenance obligatoire ;
- classification des relations ;
- reconstruction comme propriété fondamentale ;
- découplage KNW → SRH ;
- PII absente du graphe partagé par défaut.

Elles sont enregistrées dans `ADR-KNW-001-DERIVED-KNOWLEDGE-GRAPH.md`.

## 9. Limites de K3

K3 ne ferme pas :
- protocole physique ;
- format final Avro/JSON Schema/Protobuf ;
- broker ou datastore ;
- seuils numériques freshness/confidence ;
- rétention/replay physique ;
- RTO/SLO ;
- tests de reconstruction ;
- contrôles runtime.

Ces éléments appartiennent aux niveaux K4/K5 ou à l'implémentation lorsque applicable.

## 10. Verdict

La connaissance KNW-001 satisfait le gate K3 lorsque le catalogue relie cette baseline, le contrat Search, la politique de projection et l'ADR correspondant.
