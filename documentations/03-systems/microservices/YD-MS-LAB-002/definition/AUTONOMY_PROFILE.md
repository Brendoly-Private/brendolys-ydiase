---
document_id: "YD-DOC-MS-LAB-002-AUT"
title: "YD-MS-LAB-002 — Labor Market Intelligence"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie et l’ownership de Labor Market Intelligence, avec autorité : indicateurs/séries/méthodologies publiés; signaux lab-001 restent source amont."
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

# YD-MS-LAB-002 — Labor Market Intelligence

> **Rôle du document**
> Définit l’autonomie et l’ownership de Labor Market Intelligence, avec autorité : indicateurs/séries/méthodologies publiés; signaux lab-001 restent source amont.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `C2-BASELINE / LABOR-INTELLIGENCE-SEMANTICS-CLOSED`

- Autorité : indicateurs/séries/méthodologies publiés; signaux LAB-001 restent source amont.
- C2, backup MIXED. I/M2M, lectures produit autorisées via surfaces gouvernées.
- Dépendances : LAB-001, CFG. Fournit datasets dérivés à Analytics/REC/produits.
- Panne : dernière édition datée reste exploitable; recalcul différé; fraîcheur toujours visible.
- Sécurité : méthodologie/version et provenance agrégée liées à chaque édition; pas de PII dans produits agrégés sauf justification distincte.
- Repo : `brendolys-ydiase-labor-intelligence`.
- Gate : méthodologies, seuils publication, SLO/RPO/RTO, restore, critères d’extraction Forecasting.

- Politique normative : `LABOR_INTELLIGENCE_POLICY.md`.
- Gates restant : méthodologies numériques, seuils de tension/couverture, backtesting Forecasting, SLO/RPO/RTO et restore.
