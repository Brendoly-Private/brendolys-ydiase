# Politique de changement et d'impact

Statut : `ACTIVE`

## Principe

Toute modification normative évalue ses effets descendants avant activation.

## Chaîne d'impact

`vision → domaine → capacité → exigence/règle → bounded context → frontière autonome → donnée → API/événement/projection → sécurité → exploitation → vérification`

## Changement majeur

Sont notamment majeurs : ajout/retrait d'une capacité, changement d'owner, changement de source autoritative, fusion/scission de frontière, changement incompatible de contrat, nouvelle catégorie de donnée personnelle, nouveau pays, nouvelle finalité, changement de criticité ou changement de modèle économique affectant les droits d'accès.

## Analyse obligatoire

Documenter : origine, motif, objets touchés, compatibilité, migration, risques, données historiques, consommateurs, contrats, tests, rollback documentaire/technique si applicable et décision d'entrée en vigueur.

## Gates

Un changement ne passe pas `ACTIVE` tant qu'un impact critique connu reste non traité. Un point physique sans effet sur la sémantique peut rester `ADR-REQUIRED` ou `TBD-PREPROD`.

## Réévaluation D3

Une modification de 01 à 12 qui affecte les frontières, ownerships, autorités, dépendances ou contrats déclenche une revue ciblée de D3. Elle ne force pas une reprise complète si la matrice de traçabilité montre un périmètre limité.