---
document_id: "YD-DOC-MS-LRN-001-AUT"
title: "YD-MS-LRN-001 — Learning Discovery"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie et l’ownership de Learning Discovery, avec autorité : ressources learning propres et règles de découverte; program et offres marketplace restent externes."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-LRN-001 — Learning Discovery

> **Rôle du document**
> Définit l’autonomie et l’ownership de Learning Discovery, avec autorité : ressources learning propres et règles de découverte; program et offres marketplace restent externes.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `C2-BASELINE / LEARNING-DISCOVERY-SEMANTICS-CLOSED`

- Autorité : ressources learning propres et règles de découverte; Program et offres Marketplace restent externes.
- C2, backup MIXED. C/N/I/M2M.
- Dépendances : EDU, SKL, MKT.
- Panne : ressources propres valides restent visibles; offre commerciale indisponible est masquée.
- Sécurité : droits d’usage des ressources, provenance, séparation contenu pédagogique/offre commerciale.
- Repo : `brendolys-ydiase-learning-discovery`.
- Gate : modèle ressource, droits, freshness marketplace, SLO/RPO/RTO, restore.

- Politique normative : `LEARNING_DISCOVERY_POLICY.md`.
- Frontière : aucun `LRN-002` physique n'est requis tant qu'un cycle autoritatif Learning Delivery/Progress/Assessment distinct n'est pas démontré.
- Gates restant : taxonomie/mappings réels, droits d'usage, freshness EDU/MKT, fairness si ranking personnalisé, IAM/IDOR, rétention, SLO/RPO/RTO, restore et contrats.
