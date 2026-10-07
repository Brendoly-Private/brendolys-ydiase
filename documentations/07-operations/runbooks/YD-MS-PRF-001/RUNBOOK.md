---
document_id: "YD-DOC-OPS-PRF-001-RUNBOOK"
title: "YD-MS-PRF-001 — Runbook"
document_type: "operational-runbook"
document_role: "Définit la procédure opérationnelle applicable à YD-MS-PRF-001."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "operations"
---

# YD-MS-PRF-001 — Runbook

> **Rôle du document**
> Définit la procédure opérationnelle applicable à YD-MS-PRF-001.
> **Usage développement :** référence opérationnelle obligatoire pour l’implémentation et l’exploitation concernées.

Statut : RUNBOOK-BASELINE / IMPLEMENTATION-PENDING
Nature : AUTH
Criticité : C1

## Incidents couverts
Perte datastore, corruption logique, suppression accidentelle, indisponibilité d'une dépendance, erreur de décision Privacy, accès suspect, échec de projection et restauration.

## Principes
PRF-001 restaure depuis sa propre chaîne de sauvegarde. PRF-002 et les consommateurs ne sont jamais des sources de reconstruction. Les opérations indépendantes de PRF-002 restent disponibles lorsque possible. Une décision Privacy obligatoire non vérifiable reste fail-closed.

## Séquence de restauration
1. déclarer l'incident et figer les mutations si l'intégrité est incertaine ;
2. identifier le dernier point autoritatif exploitable ;
3. restaurer dans un environnement contrôlé ;
4. vérifier subject IDs, versions, données du profil courant et intégrité ;
5. réappliquer restrictions/suppressions Privacy postérieures au point restauré ;
6. vérifier autorisations et secrets nécessaires ;
7. republier/réconcilier les projections de manière idempotente ;
8. mesurer perte et durée ;
9. obtenir le verdict de reprise ;
10. rouvrir les mutations et surveiller la convergence.

## Interdictions
Pas de reconstruction depuis PRF-002, REC, ORI, CAR ou caches. Pas de retour NORMAL avant validation d'intégrité et Privacy. Pas de restauration écrasant silencieusement une version plus récente sans décision explicite.

## Preuves attendues
Horodatage, version/commit, environnement, point de restauration, durée, perte mesurée, contrôles d'intégrité, contrôles Privacy, replay/réconciliation, anomalies, verdict et reviewer.

Ce runbook devient preuve K5 uniquement lorsqu'une exécution traçable est enregistrée.
