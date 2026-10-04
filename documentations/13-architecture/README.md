# Architecture — BRENDOLYS YDIASE

Ce dossier sépare désormais explicitement architecture logique, frontières physiques, contrats et exploitation. Les ADR gouvernent les choix technologiques.

## Ordre de lecture architecture

1. `ARCHITECTURE_CIBLE.md`
2. `SERVICE_MAP.md` — catalogue des services logiques
3. `DDD_REVIEW.md`
4. `DATA_OWNERSHIP_MATRIX.md`
5. `DEPENDENCY_MAP.md`
6. `EVENT_MAP.md`
7. `MICROSERVICE_BOUNDARY_REVIEW.md` — passage service logique → frontière physique
8. `SENSITIVE_MERGER_REVIEW.md`
9. `MICROSERVICE_AUTONOMY_STANDARD.md`
10. futur `CONTRACT_REGISTRY.md`

## Couches documentaires

- `services/` : fiches des services logiques DDD. Elles restent valides même lorsqu’un service est fusionné physiquement.
- `microservices/` : profils des 47 frontières métier physiques `YD-MS-*`.
- `platform-components/` : profils des composants autonomes `YD-PLT-*`.
- BRENDOLYS Identity : dépendance IAM externe, non possédée par YDIASE.

## Règle

Un domaine métier, un service logique, un microservice physique, un composant de plateforme et une ressource d’infrastructure sont cinq concepts différents. Aucun document ne doit les utiliser comme synonymes.
