# YD-SVC-ADM-001 — Administration Service

`domain: plateforme-gouvernance` · `phase: P1` · `documentation: D1` · `implementation: not-started`

## Mission
Fournir les opérations administratives fonctionnelles autorisées de YDIASE.

## Frontière DDD
N’est pas propriétaire des données métier administrées. Toute action passe par les contrats du domaine concerné et laisse une trace.

## Dépendances
Identity & Access, Audit & Trace, services métier.

## Verdict DDD
`KEEP-AS-ADMIN-PLANE`. Peut être une couche d’orchestration plutôt qu’un microservice métier unique.

## Activation
Avec le pilote, selon moindre privilège.