# YD-SVC-SKL-002 — User Skills Profile Service

`domain: competences-connaissances` · `phase: P2` · `documentation: D1` · `implementation: not-started`

## Mission
Porter les compétences attribuées à une personne, leur niveau, preuve, origine et historique.

## Frontière DDD
Propriétaire candidat de `UserSkill` et `SkillEvidence`. Consomme le référentiel Skills Knowledge.

## Exclusions
Ne crée pas la taxonomie des compétences et ne calcule pas seul les recommandations.

## Verdict DDD
`KEEP-SEPARATE`. Données personnelles et cycle de vie distincts du référentiel public.

## Activation
Après modèle de preuve et consentement validés.