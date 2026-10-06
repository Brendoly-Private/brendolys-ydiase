# YD-SVC-DAT-002 — Data Acquisition Service

`domain: data` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AcquisitionJob`, `IngestionBatch`, `RawRecordEnvelope`, `ConnectorConfiguration`, `SubmissionBatch`.

## Source autoritative
YD-SVC-DAT-002 pour acquisition et enveloppe brute immuable, jamais pour vérité métier publiée.

## Données consommées
Source registry, partner/ambassador submissions, connector inputs, country config.

## Incohérences
Aucune donnée brute ne doit être promue implicitement en fait validé.
