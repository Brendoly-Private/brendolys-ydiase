---
document_id: "YD-DOC-MS-CAR-002-AUT"
title: "YD-MS-CAR-002 — Career Path & Transition"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie Career Path & Transition, ses trajectoires persistées, snapshots d’entrée et critères d’extraction."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
---

# YD-MS-CAR-002 — Career Path & Transition

> **Rôle du document**
> Définit l’autonomie Career Path & Transition, ses trajectoires persistées, snapshots d’entrée et critères d’extraction.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de la frontière concernée.

Statut : `autonomy-profile-draft`

- Logique : CAR-002 + CAR-003; extraction de Transition si dataset/modèle/SLO/équipe divergent.
- Autorité : trajectoires persistées et transitions utilisateur; inputs externes restent projections.
- C2, backup MIXED. C/I/M2M.
- Dépendances : CAR-001, PRF, SKL-002, CNS.
- Panne : résultat partiel ou indisponible explicitement signalé; aucune donnée inventée; snapshot d’entrée versionné.
- Sécurité : données personnelles minimisées, explications et hypothèses conservées avec le résultat.
- Repo : `brendolys-ydiase-career-path-transition`.
- Gate : critères d’extraction CAR-003, SLO/RPO/RTO, rétention snapshots, restore et contrats.