---
document_id: "YD-DOC-SYS-ARC-000"
title: "Architecture — BRENDOLYS YDIASE"
document_type: "architecture-navigation"
document_role: "Oriente la lecture de l’architecture et distingue services logiques, frontières physiques, plateforme, contrats et exploitation."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "view"
canonical: false
development_usage: "informational"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "architecture"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# Architecture — BRENDOLYS YDIASE

> **Rôle du document**
> Oriente la lecture de l’architecture et distingue services logiques, frontières physiques, plateforme, contrats et exploitation.
> **Usage développement :** document d’orientation ou d’historique ; il ne crée pas de vérité normative courante.

Ce dossier sépare explicitement architecture logique, frontières physiques, contrats et exploitation. Les ADR gouvernent les choix technologiques et les changements de frontière.

## Ordre de lecture architecture

1. `ARCHITECTURE_CIBLE.md`
2. `SERVICE_MAP.md` — catalogue des services logiques
3. `DDD_REVIEW.md`
4. `DATA_OWNERSHIP_MATRIX.md`
5. `DEPENDENCY_MAP.md`
6. `EVENT_MAP.md`
7. `MICROSERVICE_BOUNDARY_REVIEW.md` — passage service logique → frontière physique
8. `SENSITIVE_MERGER_REVIEW.md`
9. `ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md` — séparation physique Profile/History
10. `MICROSERVICE_AUTONOMY_STANDARD.md`
11. `AUTONOMY_PROFILE_REGISTER.md`
12. `AUTONOMY_CLOSURE_MATRIX.md`
13. `../../04-contracts/indexes/CONTRACT_REGISTRY.md` — registre contractuel canonique actif

## Couches documentaires

- `services/` : fiches des services logiques DDD. Elles restent valides même lorsqu’un service est fusionné physiquement.
- `microservices/` : profils des 48 frontières métier physiques `YD-MS-*`.
- `platform-components/` : profils des 4 composants autonomes `YD-PLT-*`.
- BRENDOLYS Identity : dépendance IAM externe, non possédée par YDIASE.

Cible autonome actuelle : **58 frontières candidates = 54 microservices métier + 4 composants plateforme**, dont six frontières Entrepreneurship documentées en `DRAFT`. La baseline antérieure comptait 52 frontières.

## Règle

Un domaine métier, un service logique, un microservice physique, un composant de plateforme et une ressource d’infrastructure sont cinq concepts différents. Aucun document ne doit les utiliser comme synonymes.