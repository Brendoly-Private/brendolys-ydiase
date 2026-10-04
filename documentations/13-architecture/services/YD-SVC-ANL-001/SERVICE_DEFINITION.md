# YD-SVC-ANL-001 — Analytics Service

`domain: analytics` · `phase: P3` · `documentation: D1` · `implementation: not-started`

## Mission
Produire agrégations, indicateurs internes et mesures gouvernées à partir de données autorisées.

## Frontière DDD
Ne possède pas les faits métier sources. Ses jeux analytiques sont dérivés et reproductibles.

## Dépendances
Data Quality, domaines sources, Audit & Trace.

## Verdict DDD
`KEEP-SEPARATE`. Charge analytique distincte des transactions.

## Activation
Après définitions d’indicateurs et politiques d’accès validées.