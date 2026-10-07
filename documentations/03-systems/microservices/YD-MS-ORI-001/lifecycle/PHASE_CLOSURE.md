---
document_id: "YD-DOC-MS-ORI-001-CLS"
title: "YD-MS-ORI-001 — Baseline C1"
document_type: "microservice-phase-closure"
document_role: "Consigne la fermeture de phase documentaire de YD-MS-ORI-001 et les travaux ou preuves restant différés."
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
---

# YD-MS-ORI-001 — Baseline C1

> **Rôle du document**
> Consigne la fermeture de phase documentaire de YD-MS-ORI-001 et les travaux ou preuves restant différés.
> **Usage développement :** preuve de maturité ou de fermeture ; le profil canonique et les politiques référencées restent autoritatifs.

Statut : `DOCUMENTATION-BASELINE-C1 / SEMANTICS-DEFINED`
Nature : `AUTH`
Criticité : `C1`

## Autorité
ORI-001 porte ORI-001 + ORI-002. Il possède dossier, objectifs/contraintes spécifiques, comparaisons et décisions enregistrées ; REC reste distinct.

## Politique normative
Voir `ORIENTATION_DECISION_POLICY.md`.

## Invariants C1
- données de profilage minimisées et finalisées ;
- contrôle objet/horizontal obligatoire ;
- support interne explicitement autorisé et audité ;
- CNS fail-closed lorsque la finalité exige une décision Privacy vérifiable ;
- historique/versionnement non destructif ;
- services sources/consommateurs ne sont jamais des backups ;
- backup/restore propre au microservice.

## Avant ACTIVE
- méthodes/pondérations métier réellement validées selon le service ;
- règles mineurs/représentation ;
- Privacy/rétention ;
- IAM physique et tests IDOR ;
- BIA, RPO/RTO/SLO ;
- backup/restore policy et restore test ;
- contrats physiques ;
- audit et runbooks liés à l'implémentation.

Statut final : `C1-BASELINE-ESTABLISHED — ORIENTATION-SEMANTICS-CLOSED / VALIDATION-PRIVACY-PREPROD-PENDING`.
