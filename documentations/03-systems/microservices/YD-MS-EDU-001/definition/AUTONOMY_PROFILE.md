# YD-MS-EDU-001 — Institution Catalog

Statut : `autonomy-profile-draft`

- Logique : EDU-001. Autorité sur institutions, campus, statuts et versions.
- Criticité candidate : C2. Backup : AUTH, chiffré, restauration indépendante testée.
- IAM : `brendolys-internal`, `brendolys-networks` pour contributions autorisées, `brendolys-customers` en lecture. M2M dédié.
- Exposition : EDGE lecture, INT écriture/intégration. DNS public direct interdit hors edge.
- Dépendances : CFG, Data validation, Partner/Institution workflows. Aucun accès DB externe.
- Panne : dernière version publiée lisible. Création/publication bloquée si pays, source ou validation obligatoire est inconnue.
- Sécurité : provenance des modifications, séparation contributeur/validateur, audit des mutations sensibles.
- Scaling : lecture catalogue dominante, cache/projections possibles sans transférer l’autorité.
- Repo candidat : `brendolys-ydiase-institution-catalog`. Datastore, migrations, secrets, workload identity et pipeline propres.
- Gate production : RPO/RTO/SLO, scopes, workflow de validation, rétention, restore test et contrats physiques.