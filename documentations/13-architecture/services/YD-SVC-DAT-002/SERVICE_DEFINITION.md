# YD-SVC-DAT-002 — Data Acquisition Service

`domain: data` · `phase: P1` · `documentation: D1` · `implementation: not-started`

## Mission
Recevoir les données issues de fichiers, terrain, partenaires et connecteurs autorisés.

## Frontière DDD
Possède l’état d’ingestion et les artefacts bruts gouvernés, pas la vérité métier publiée.

## Dépendances
Data Source Registry, Data Provenance, Data Quality.

## Verdict DDD
`KEEP-SEPARATE`. Connecteurs et charge d’ingestion divergent des domaines métier.

## Activation
Après source enregistrée et droits d’usage vérifiés.