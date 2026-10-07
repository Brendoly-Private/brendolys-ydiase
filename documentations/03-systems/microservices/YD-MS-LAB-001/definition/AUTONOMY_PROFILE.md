---
document_id: "YD-DOC-MS-LAB-001-AUT"
title: "YD-MS-LAB-001 — Labor Signals"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie et l’ownership de Labor Signals, avec autorité : signaux marché normalisés publiés; raw/provenance restent dat."
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
---

# YD-MS-LAB-001 — Labor Signals

> **Rôle du document**
> Définit l’autonomie et l’ownership de Labor Signals, avec autorité : signaux marché normalisés publiés; raw/provenance restent dat.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `C2-BASELINE / LABOR-SIGNAL-SEMANTICS-CLOSED`

- Autorité : signaux marché normalisés publiés; raw/provenance restent DAT.
- C2, backup AUTH. I/M2M, pas d’écriture client.
- Dépendances : DAT-003/004, CFG, références CAR/SKL.
- Panne : ingestion différée/quarantaine; aucun signal publié sans preuve/qualité minimale.
- Sécurité : source/provenance/territoire/observedAt obligatoires; distinction observation et estimation.
- Repo : `brendolys-ydiase-labor-signals`.
- Gate : seuil qualité, politique expiration, SLO/RPO/RTO, restore et contrats.

- Politique normative : `LABOR_SIGNAL_POLICY.md`.
- Gates restant : seuils qualité/fraîcheur par classe, sources réelles, SLO/RPO/RTO, restore et contrats.
