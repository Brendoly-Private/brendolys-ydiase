---
document_id: "YD-DOC-MS-LRN-001-CLS"
title: "YD-MS-LRN-001 — Learning Discovery — Baseline C2"
document_type: "microservice-phase-closure"
document_role: "Consigne la fermeture de phase documentaire de YD-MS-LRN-001 et les conditions, gates ou preuves restant à traiter avant les étapes ultérieures."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "evidence"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-LRN-001 — Learning Discovery — Baseline C2

> **Rôle du document**
> Consigne la fermeture de phase documentaire de YD-MS-LRN-001 et les conditions, gates ou preuves restant à traiter avant les étapes ultérieures.
> **Usage développement :** preuve de maturité ou de fermeture ; le profil canonique et les politiques référencées restent autoritatifs.

Statut : `DOCUMENTATION-BASELINE-C2 / LEARNING-DISCOVERY-SEMANTICS-CLOSED`
Nature : `MIXED`
Criticité : `C2`

## Politique normative
Voir `LEARNING_DISCOVERY_POLICY.md`.

## Invariants
- LearningResource, Program EDU, Marketplace offer et Skill acquis restent distincts ;
- LRN ne copie pas l'autorité EDU/MKT/SKL ;
- un gap peut guider la découverte mais LRN ne crée pas le gap ;
- suivre/acheter/terminer une ressource ne prouve pas automatiquement une compétence ;
- prérequis HARD/REQUIRED/PREFERRED/INFORMATIONAL restent explicites ;
- UNKNOWN n'est ni FAILED ni valeur inventée ;
- coût/durée/disponibilité exigent source/version/fraîcheur ;
- ranking learning organique isolé du sponsoring/commercial ;
- résultats personnalisés versionnés et explicables ;
- aucun LRN-002 physique sans nouveau cycle d'autorité démontré.

## Boucle métier désormais documentable
`Skill/Career Gap → Learning Discovery → Resource/Program option → apprentissage externe/à définir → Evidence/Assessment → SKL-002 update`.

La portion "apprentissage/progression autoritative" n'est pas attribuée à LRN-001 par défaut.

## Avant ACTIVE
- mappings gap ↔ outcomes/skills validés ;
- catalogue et droits d'usage réels ;
- fraîcheur EDU/MKT ;
- critères/seuils et fairness si personnalisation ;
- Privacy/IAM/IDOR ;
- SLO/RPO/RTO, restore et contrats physiques.

Statut final : `C2-BASELINE-ESTABLISHED — LEARNING-DISCOVERY-SEMANTICS-CLOSED / MAPPINGS-AND-PREPROD-EVIDENCE-PENDING`.
