# YD-SVC-AI-001 — AI Gateway Service

`domain: ai` · `phase: P2` · `documentation: D1` · `implementation: not-started`

## Mission
Contrôler l’accès aux modèles IA, politiques, quotas, modèles autorisés et contexte transmis.

## Frontière DDD
Ne devient jamais source de vérité métier. Ne possède pas les documents ou données utilisés pour contextualiser un modèle.

## Dépendances
Consent & Privacy, Audit & Trace, Retrieval & Grounding, AI Verification.

## Verdict DDD
`KEEP-SEPARATE`. Point de contrôle de sécurité et gouvernance IA.

## Activation
ADR, évaluation et politique Data obligatoires.