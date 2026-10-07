---
document_id: "YD-DOC-MS-SRH-001-AUT"
title: "YD-MS-SRH-001 — Search & Discovery"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-SRH-001."
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

# YD-MS-SRH-001 — Search & Discovery

> **Rôle du document**
> Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-SRH-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `C2-BASELINE / SEARCH-DISCOVERY-SEMANTICS-CLOSED`

- Classification : `DERIVED`, criticité C2. État actuel : `REBUILD-UNVERIFIED` jusqu’au premier FULL_REBUILD réussi.
- Autorité : index uniquement; aucune autorité sur EDU, CAR, OPP, CNT ou LRN.
- Sources de reconstruction : projections versionnées de EDU, CAR, OPP, CNT et LRN. Les contrats/versions exacts et leurs rétentions seront enregistrés au Contract Registry; ils constituent un gate préproduction.
- Checkpoint/watermark : position par flux/partition source obligatoire. Un timestamp local seul est interdit. Le mécanisme physique reste ADR-REQUIRED.
- Replay : idempotent; doublons, événements hors ordre, suppressions, retraits d’opportunités, dépublication de contenu et révocations applicables doivent converger vers l’état source.
- Reconstruction : `FULL_REBUILD` de tous les index; `PARTIAL_REBUILD` par type d’objet/partition; `CATCH_UP` depuis checkpoint valide.
- Fraîcheur : états `FRESH`, `STALE-ACCEPTABLE`, `EXPIRED`, `UNKNOWN`; seuils numériques TBD-PREPROD. Les résultats EXPIRED/UNKNOWN ne sont pas présentés comme actuels.
- Intégrité : contrôle de cardinalité, versions, trous, doublons, objets supprimés et références orphelines après rebuild.
- Panne : recherche partielle ou indisponibilité contrôlée; aucun résultat Search ne vaut validation métier.
- Sécurité : indexation minimale, suppression/révocation propagée, aucun secret ni PII inutile dans l’index.
- Scaling : lectures élevées et indexation asynchrone; budget distinct pour rebuild/catch-up.
- IAM : C/N/I/M2M selon surface. Repo : `brendolys-ydiase-search-discovery`.
- DR/test : destruction contrôlée de l’index + FULL_REBUILD obligatoire avant production; conserver durée, fraîcheur finale, positions source et anomalies.
- Gates : contrats/versions et rétention des sources; watermark; FULL_REBUILD réussi; statut `REBUILDABLE`; seuils de fraîcheur; RTO/SLO; politique suppression.

- Politiques normatives : `SEARCH_DISCOVERY_POLICY.md` et `SOURCE_PROJECTION_BASELINE.md`.
- Contrats sources : EDU/CAR/OPP/CNT/LRN SEARCHABLE v1 ; KNW Search Enrichment v1 optionnel.
- Ranking Search distinct de REC-001, OPP-002 et ORI ; sponsoring interdit dans le rang organique.
- Priorité : revoke/privacy > delete/withdraw/unpublish/expire > correction > upsert > KNW enrichment.
- Gates restant : schémas/analyzers physiques, coefficients/quality metrics, freshness/removal SLO, access/query retention, FULL_REBUILD réussi, RTO/SLO et tests sécurité.
