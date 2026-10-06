# YD-MS-REC-001 — Sponsored Non-Influence Test Policy

Statut : `GOVERNANCE-BASELINE / K5-EXECUTION-PENDING`

## Objet

Prouver que SPN-001 et toute donnée commerciale restent incapables de modifier l'éligibilité, le score, le rang, les pondérations, exclusions ou explications organiques de REC-001.

## Invariant

À entrées métier identiques et policy/model versions identiques, modifier budget, enchère, commission, statut partenaire, campagne ou placement sponsorisé doit laisser le résultat organique inchangé.

## Suite minimale de tests

- exécuter un run de référence sans contexte sponsor ;
- rejouer avec variations des données SPN/commerciales ;
- comparer candidats éligibles, `organic_score`, `organic_rank`, exclusions, composantes et explications ;
- vérifier qu'aucune donnée SPN n'entre dans l'evidence snapshot organique comme facteur de ranking ;
- vérifier qu'une insertion sponsorisée UI ne renumérote pas `organic_rank` ;
- vérifier les contrôles d'accès empêchant SPN d'écrire les objets/policies organiques REC.

Toute différence organique causée par une donnée commerciale est un échec critique.

## Preuves K5

Conserver versions du code/policy, fixtures/datasets, résultats de comparaison, traces d'accès et verdict. La suite doit être automatisable et exécutée avant ACTIVE puis lors des changements affectant REC/SPN.
