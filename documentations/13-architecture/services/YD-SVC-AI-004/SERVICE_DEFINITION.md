# YD-SVC-AI-004 — AI Orchestration Service

`domain: ai` · `phase: P6` · `documentation: D1` · `implementation: not-started`

## Mission
Orchestrer modèles, outils et tâches IA autorisées selon politiques et contexte.

## Frontière DDD
Ne possède aucune vérité métier. Coordonne des capacités IA sous contrôle du Gateway.

## Dépendances
AI Gateway, Retrieval & Grounding, AI Verification, Audit & Trace.

## Verdict DDD
`KEEP-FUTURE`. Ne pas isoler avant plusieurs modèles ou workflows nécessitant une orchestration propre.

## Activation
ADR obligatoire avec besoin mesuré.