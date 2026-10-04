# YD-SVC-AI-001 — AI Gateway Service

`domain: ai` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AIRequest`, `AIExecutionPolicy`, `AIUsageRecord`.

## Source autoritative
YD-SVC-AI-001 est autoritatif pour les requêtes IA gouvernées, politiques d’exécution IA et traces fonctionnelles d’usage IA.

## Données consommées
Identity/access, consent, entitlements, modèles approuvés depuis YD-SVC-MLP-001, audit policies, country/configuration constraints.

## Frontière
AI Gateway contrôle l’accès et l’exécution. Il ne possède plus le registre des modèles, leurs versions, évaluations, promotions ou retraits.

## Incohérences
La frontière Model Registry/MLOps est extraite avant D3 dans `YD-SVC-MLP-001`. Les contrats Gateway → MLOps et Orchestration → MLOps seront détaillés en D3.
