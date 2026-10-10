---
document_id: "YD-DOC-MS-INT-001-AUT"
title: "YD-MS-INT-001 — Intelligence Product"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie Intelligence et ses produits dérivés sans transférer l’autorité des données et signaux sources."
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
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-INT-001 — Intelligence Product

> **Rôle du document**
> Définit l’autonomie Intelligence et ses produits dérivés sans transférer l’autorité des données et signaux sources.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Autorité : briefs/éditions de produit intelligence, evidence refs et règles d’accès; faits sources restent amont.
- C1, backup AUTH. C organisations autorisées, I, M2M.
- Dépendances : ANL, LAB, KNW, BIL.
- Panne : dernière édition autorisée et datée; nouvelle édition suspendue si evidence sous seuil.
- Sécurité : evidence/provenance, entitlement, confidentialité produit, validation humaine selon classe.
- Repo : `brendolys-ydiase-intelligence-product`.
- Gate : workflow éditorial/validation, licence, SLO/RPO/RTO, restore.