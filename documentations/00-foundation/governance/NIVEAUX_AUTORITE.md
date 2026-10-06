# Niveaux d'autorité documentaire

Statut : `ACTIVE`

## Principe

L'autorité dépend du sujet. Un document technique n'est pas supérieur à un document métier parce qu'il est plus détaillé.

## Ordre par responsabilité

1. intention fondatrice et décisions humaines explicitement gelées
2. fondations produit validées
3. domaines métier, règles et exigences validées
4. politiques transversales data, sécurité, conformité et exploitation
5. décisions d'architecture approuvées
6. contrats API, événements et données approuvés
7. spécifications de composants et procédures
8. documents dérivés, projections et vues de travail

## Règle d'autorité locale

La source autoritative d'un fait reste le document ou registre propriétaire de ce fait. Une copie, projection, Event Map ou Dependency Map ne devient jamais autoritative par duplication.

## Conflit entre niveaux

Le document de niveau inférieur est suspendu sur le point conflictuel. Il ne corrige pas silencieusement le niveau supérieur. Le conflit suit `POLITIQUE_CONTRADICTIONS.md`.

## Architecture

Les 51 frontières D3 sont des décisions d'architecture candidates stabilisées. Elles restent soumises aux fondations produit et aux domaines métier. Une future correction métier peut donc déclencher leur réévaluation sans effacer leur historique.

## IA

Une sortie IA, un résumé ou une recommandation générée ne constitue jamais une source normative par elle-même.