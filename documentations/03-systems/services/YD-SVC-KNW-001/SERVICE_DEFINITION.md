# YD-SVC-KNW-001 — Knowledge Graph Service

`domain: knowledge` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`KnowledgeNodeProjection`, `KnowledgeEdge`, `SemanticAssertion`, `GraphVersion`.

## Source autoritative
YD-SVC-KNW-001 pour relations sémantiques propres au graphe; domaines restent autoritatifs sur leurs entités.

## Données consommées
Education, skills, careers, labor, opportunities, taxonomies, provenance/quality.

## Incohérences
`KnowledgeNodeProjection` est une projection. Le graphe ne doit jamais devenir owner de `Institution`, `Program`, `Skill`, `Occupation` ou `Opportunity`.
