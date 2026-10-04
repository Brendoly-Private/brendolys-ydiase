# YD-SVC-CAR-004 — Career Simulation Service

`domain: metiers-carrieres` · `phase: P3` · `documentation: D1` · `implementation: not-started`

## Mission
Simuler des scénarios professionnels à partir d’hypothèses explicites.

## Frontière DDD
Produit des simulations non autoritatives. Ne modifie ni profil, ni marché, ni référentiels.

## Dépendances
Career Path, Career Transition, Labor Market Intelligence.

## Verdict DDD
`MERGE-CANDIDATE` avec Career Path au début. Isolation future si calcul, charge ou cycle de publication le demandent.

## Activation
Après règles de simulation et avertissements d’incertitude validés.