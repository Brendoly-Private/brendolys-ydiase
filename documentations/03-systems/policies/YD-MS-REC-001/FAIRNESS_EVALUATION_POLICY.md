# YD-MS-REC-001 — Fairness Evaluation Policy

Statut : `GOVERNANCE-BASELINE / K5-EVIDENCE-PENDING`

## Objet

Définir comment une policy de recommandation personnalisée est évaluée avant activation et lors de ses révisions, sans inventer de seuils numériques avant données représentatives.

## Principes

- l'évaluation porte séparément sur éligibilité, score, exposition, abstention et erreurs ;
- `UNKNOWN` reste distinct de `FAILED` ;
- les contextes pays, langue, territoire et populations pertinentes sont explicités ;
- les attributs sensibles/protégés ne servent pas au ranking sauf base légitime, finalité explicite et validation de gouvernance ;
- leur éventuel usage d'audit est séparé, minimisé, contrôlé et non réinjecté automatiquement dans le ranking ;
- aucune métrique unique ne suffit à conclure à l'équité.

## Protocole de validation

Avant activation d'une policy :
1. identifier population, contexte, finalité et sources ;
2. vérifier couverture et qualité des données ;
3. mesurer taux d'éligibilité, abstention, erreurs et exposition ;
4. rechercher les disparités injustifiées dans les segments autorisés à l'évaluation ;
5. documenter limites, inconnues et biais de mesure ;
6. comparer avec la policy de référence lorsque possible ;
7. faire approuver ou rejeter la version ;
8. conserver dataset/version, code/configuration de test, résultats et décision.

Les seuils numériques et datasets représentatifs restent `TBD-PREPROD` et doivent être approuvés avant ACTIVE.

## Dérive et rollback

Toute dérive significative de données, couverture, comportement ou disparité déclenche revue. Une policy doit pouvoir être désactivée ou revenir à une version précédemment approuvée sans réécrire les runs historiques.

## Preuves K5

K5 exige des résultats reproductibles sur données représentatives, versions des datasets/policies/modèles, critères PASS/FAIL approuvés, écarts documentés et décision de gouvernance traçable.
