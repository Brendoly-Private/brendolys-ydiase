# YD-SVC-SKL-001 — Skills Knowledge Service

`domain: competences-connaissances` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Skill`, `KnowledgeConcept`, `SkillRelation`, `SkillTaxonomyMapping`.

## Source autoritative
YD-SVC-SKL-001.

## Données consommées
Taxonomies (DAT-005), curricula/modules (EDU-003), occupations (CAR-001), provenance (DAT-003).

## Incohérences
Ne doit jamais posséder `UserSkill`. Risque de boucle sémantique avec CAR-001 à limiter par références stables.
