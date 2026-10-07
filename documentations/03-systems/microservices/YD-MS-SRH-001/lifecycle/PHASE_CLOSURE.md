---
document_id: "YD-DOC-MS-SRH-001-CLS"
title: "YD-MS-SRH-001 — Search & Discovery — Baseline C2"
document_type: "microservice-phase-closure"
document_role: "Consigne la fermeture de phase documentaire de YD-MS-SRH-001 et les travaux ou preuves restant différés."
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

# YD-MS-SRH-001 — Search & Discovery — Baseline C2

> **Rôle du document**
> Consigne la fermeture de phase documentaire de YD-MS-SRH-001 et les travaux ou preuves restant différés.
> **Usage développement :** preuve de maturité ou de fermeture ; le profil canonique et les politiques référencées restent autoritatifs.

Statut : `DOCUMENTATION-BASELINE-C2 / SEARCH-DISCOVERY-SEMANTICS-CLOSED`
Classification : `DERIVED`
Rebuild state : `REBUILD-UNVERIFIED`

## Politiques normatives
- `SEARCH_DISCOVERY_POLICY.md`
- `SOURCE_PROJECTION_BASELINE.md`
- dépendance : `../YD-MS-KNW-001/KNW_TO_SEARCH_PROJECTION_CONTRACT.md`

## Invariants
- SRH possède index/configuration, jamais les objets métier ;
- documents indexés conservent source/version/publication/freshness ;
- retrait/révocation/expiration priment sur ranking et enrichment ;
- ranking Search ≠ Recommendation REC ≠ Matching OPP ≠ décision ORI ;
- sponsoring/paiement n'influence pas le ranking organique ;
- langue et territoire sont explicites et versionnés ;
- accès restreint vérifié à la requête, PII minimisée ;
- KNW est enrichment optionnel, jamais dépendance synchrone obligatoire ;
- FULL/PARTIAL/CATCH_UP reconstructibles et idempotents ;
- index stale ne valide aucune commande métier sensible.

## Avant REBUILDABLE/ACTIVE
- matérialiser/enregistrer les contrats physiques v1 ;
- prouver snapshot/replay et rétention compatibles pour EDU/CAR/OPP/CNT/LRN ;
- finaliser analyzers/tokenizers multilingues ;
- valider ranking/quality metrics ;
- définir SLO freshness et retrait ;
- tester Privacy/IAM/tenant/IDOR ;
- exécuter FULL_REBUILD, suppressions/revocations/out-of-order et convergence ;
- mesurer RTO/SLO et publier le rapport.

Statut final : `C2-BASELINE-ESTABLISHED — SEARCH-DISCOVERY-SEMANTICS-CLOSED / FULL-REBUILD-AND-PREPROD-EVIDENCE-PENDING`.
