# YDIASE — Architecture cible Data & IA

Statut : TARGET-PLATFORM-BASELINE / NORMATIVE

## Data plane
Source Registry → Acquisition → Provenance → Quality/Validation → Event/Batch/Stream processing → zones analytiques gouvernées → Search/Knowledge/Analytics/ML.

Le stockage opérationnel reste privé à chaque owner métier. Le plan Data ne devient pas une base partagée.

Capacités : ingestion multi-source, event streaming logique, batch/stream processing, lakehouse analytique logique, catalog/lineage, qualité, rétention/suppression, Search projections, Knowledge Graph DERIVED, Analytics/forecasting, datasets/features versionnés et observabilité des pipelines.

## AI plane
AI Gateway → autorisation/policy → Retrieval & Grounding → orchestration/modèle/outils → AI Verification → service demandeur.

Capacités : model lifecycle/versioning, évaluation, rollback, grounding sourcé, tool governance, safety, métriques qualité/robustesse/fairness lorsque applicable, latence/coût, drift et audit compatible Privacy.

## Entrepreneuriat
Les usages IA entrepreneuriaux consomment uniquement des projections autorisées PRF/SKL/ASM/LAB/ENT/EDU/LRN/PRT. Une sortie sépare fait, signal, hypothèse, inconnue, fraîcheur et confiance. Elle ne garantit pas marché, rentabilité, financement ou conformité.

## Hyperscale
Les plans OLTP, streaming, analytique, Search, Knowledge et IA sont isolables. Partitionnement, parallélisme, autoscaling, quotas et backpressure sont dimensionnés à partir des Capacity Profiles et des flux agrégés.

## Recovery
Search/Knowledge/Analytics et autres projections sont reconstruisibles. Les données AUTH sont restaurées par leurs owners. Pipelines : replay idempotent, checkpoint/restart, quarantine et réconciliation.

## Choix physiques
Broker, stream engine, lakehouse, object store, search, graph store, vector store, feature store, orchestrateur et model serving sont décidés par ADR après benchmark capacité/coût/souveraineté/exploitabilité.
