# YD-SVC-OPP-002 — Opportunity Matching Service

`domain: opportunites-recrutement` · `phase: P4` · `documentation: D1` · `implementation: not-started`

## Mission
Calculer la correspondance entre profils, compétences et opportunités avec explication.

## Frontière DDD
Ne possède ni profils ni opportunités. Les scores sont des résultats calculés versionnés.

## Dépendances
Opportunity, User Skills Profile, Profile, Skills Knowledge.

## Verdict DDD
`KEEP-LOGICAL`. Peut partager une plateforme de calcul avec Recommendation sans partager son ownership métier.

## Activation
Après métriques de qualité et règles anti-discrimination validées.