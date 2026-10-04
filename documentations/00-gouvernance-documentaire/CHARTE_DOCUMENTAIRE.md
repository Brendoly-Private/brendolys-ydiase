# Charte documentaire

## Identifiants

Les préfixes autorisés incluent `YD-DOC`, `YD-REQ`, `YD-ADR`, `YD-RISK`, `YD-HYP`, `YD-SRC`, `YD-CAP`, `YD-DOM`, `YD-SVC`, `YD-EVT` et `YD-API`. Un identifiant n’est jamais réutilisé.

L’ajout d’une nouvelle famille d’identifiants doit être documenté avant son usage généralisé.

## Traçabilité

Chaque exigence critique doit pouvoir être reliée selon la chaîne applicable :

`vision → domaine → capacité → exigence → règle métier → bounded context → service candidat → contrat → vérification`.

Tous les maillons ne sont pas obligatoires dès la création d’un élément. Les liens deviennent obligatoires à mesure que la maturité documentaire progresse. Un lien normatif porte une date et un responsable lorsqu’il est enregistré dans un registre prévu à cet effet.

## Services cibles

- Tout service inscrit dans `13-architecture/SERVICE_MAP.md` possède une fiche documentaire.
- La fiche existe même lorsque le service est futur, non développé, non déployé ou inactif.
- L’identification d’un service exige au minimum un domaine, une raison d’existence, une responsabilité principale, une frontière initiale et une phase cible ou une décision `TBD` gouvernée.
- Les contrats détaillés ne sont pas nécessaires pour identifier un service candidat.
- Le passage vers D2, D3 et les niveaux suivants ajoute progressivement données, dépendances, contrats, sécurité et exigences opérationnelles.
- Un `TBD` doit exprimer une question réelle non résolue. Il ne sert pas à masquer une contradiction connue.

## Séparation des statuts

Le statut documentaire d’un service ne doit jamais être utilisé comme statut d’implémentation, de déploiement ou d’activation.

Les quatre dimensions sont suivies séparément :

- maturité documentaire
- implémentation
- déploiement
- activation

## Revue et succession

Un propriétaire et un suppléant sont requis pour les documents normatifs lorsqu’ils atteignent le statut `ACTIVE`. Un document obsolète devient `DEPRECATED`, `RETIRED` ou `SUPERSEDED`. Le dernier statut exige un successeur explicite.

## Règle de prudence

La documentation ne doit pas inventer une API, un événement, un seuil de performance, une technologie, une obligation réglementaire ou une dépendance uniquement pour remplir un modèle. Lorsqu’une décision manque, le document conserve le point comme `TBD`, hypothèse ou question ouverte avec sa condition de résolution.
