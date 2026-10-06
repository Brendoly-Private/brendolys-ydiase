# YDIASE Knowledge Gate — K4 Gouverné

Statut : `BASELINE / PILOT`

## Objet

K4 signifie qu'une entité K3 possède les règles de gouvernance, sécurité, conformité et exploitation nécessaires pour préparer une implémentation exploitable sans laisser les responsabilités critiques implicites.

K4 ne signifie ni préproduction validée ni production.

## Critères obligatoires

1. `dataClassification` — les données et objets manipulés sont classifiés, avec traitement attendu selon leur sensibilité.
2. `securityControls` — contrôles d'accès, authentification service-à-service, intégrité, secrets, isolation et journalisation applicables sont définis.
3. `privacyAndRetentionWhenApplicable` — finalités, minimisation, rétention, suppression, droits et contraintes territoriales/personnelles sont définis ou `N/A` avec justification.
4. `sloOrCriticality` — criticité et objectifs opérationnels nécessaires sont définis au niveau adapté à la phase. Les valeurs numériques peuvent rester `TBD-PREPROD` si leur méthode de fixation et leur gate sont documentés.
5. `observability` — logs, métriques, traces, signaux métier, alertes et corrélation nécessaires sont définis.
6. `backupRecoveryWhenStateful` — stratégie de sauvegarde, restauration, reconstruction et responsabilités est définie pour tout état non reconstructible.
7. `runbookOrOperationalProcedure` — incidents principaux, modes dégradés, reprise, rollback et escalade disposent d'une procédure exploitable.
8. `namedOwners` — owner métier/technique et responsabilités de revue sont identifiables par rôle ou registre gouverné.

## Règles

- `UNKNOWN` bloque K4.
- `PARTIAL` bloque K4.
- `N/A` exige une justification vérifiable.
- Une criticité sans stratégie de reprise ne satisfait pas K4 pour un service stateful.
- Un document générique de sécurité ne suffit pas s'il ne peut pas être relié au composant.
- K4 peut être atteint avant code si les contrôles sont spécifiés et testables, mais K5 exigera les preuves d'exécution correspondantes.
- Les valeurs numériques dépendantes de charge ou préproduction peuvent rester ouvertes si le mécanisme de décision, le responsable et le gate de fermeture sont définis.

## Sortie attendue

Pour chaque microservice :
- matrice de classification ;
- baseline sécurité/conformité ;
- baseline exploitation/résilience ;
- owner matrix ;
- liste explicite des paramètres `TBD-PREPROD` ;
- critères qui permettront K5.

## Pilote

Le premier pilote K4 porte sur `YD-MS-KNW-001`, puis `YD-MS-SKL-001`, `YD-MS-REC-001` et `YD-MS-LRN-001` après fermeture K3.
