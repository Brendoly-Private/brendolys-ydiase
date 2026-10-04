# Architecture logique

Les domaines publient des contrats explicites. Les systèmes opérationnels possèdent leurs données ; les projections de recherche, le graphe, le lakehouse et les caches consomment des copies gouvernées. Kafka, Flink, Spark, GPU, mesh et bases spécialisées sont des options soumises à ADR, coût, risque et seuil mesurable.

Un service candidat doit référencer domaine, capacité, exigences, propriétaire, consommateurs, contrats, données autoritatives, SLA, retrait et migration.

