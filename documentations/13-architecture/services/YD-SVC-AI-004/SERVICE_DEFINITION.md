# YD-SVC-AI-004 — AI Orchestration Service

`domain: ai` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AIWorkflow`, `AITask`, `AIWorkflowRun`, `AIExecutionPlan`.

## Source autoritative
YD-SVC-AI-004 pour orchestration.

## Données consommées
AI Gateway, retrieval, verification, domain tool contracts, access/consent.

## Incohérences
Ne doit pas contourner AI Gateway ni appeler directement des données interdites par CNS/entitlements.
