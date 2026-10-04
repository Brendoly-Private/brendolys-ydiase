# YD-SVC-PRF-002 — Education & Experience Profile Service

`domain: identite-profils` · `phase: P2` · `documentation: D1` · `implementation: not-started`

## Mission
Porter l’historique éducatif, professionnel et les acquis déclarés d’une personne.

## Frontière DDD
Propriétaire candidat de `EducationHistory` et `ExperienceHistory`. Consomme établissements, programmes, qualifications et employeurs.

## Exclusions
Ne valide pas les référentiels externes et ne possède pas le catalogue Education.

## Verdict DDD
`REVIEW-SPLIT`. Peut rester avec Profile au pilote puis être isolé si volume, confidentialité ou cycle de vie divergent.

## Activation
Après modèle d’historique et règles de preuve validés.