---
document_id: "YD-DOC-OPS-SKL-001-RUNBOOK"
title: "YD-MS-SKL-001 — Runbook"
document_type: "operational-runbook"
document_role: "Définit la procédure opérationnelle applicable à YD-MS-SKL-001."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "operations"
created_at: "2026-10-06"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-SKL-001 — Runbook

> **Rôle du document**
> Définit la procédure opérationnelle applicable à YD-MS-SKL-001.
> **Usage développement :** référence opérationnelle obligatoire pour l’implémentation et l’exploitation concernées.

Statut : `OPERATIONAL-PROCEDURE-BASELINE / IMPLEMENTATION-PENDING`

## Triage

Identifier : objet SKL affecté, version, type de mutation, provenance, acteur/processus, source evidence éventuelle, consommateurs impactés et dernière version canonique saine.

## Incidents

### Mutation non autorisée
1. bloquer ou suspendre la mutation ;
2. conserver la trace d'audit ;
3. identifier acteur, source, version et objets impactés ;
4. restaurer l'état canonique valide si nécessaire ;
5. vérifier les projections déjà publiées et propager la correction.

### Provenance absente ou invalide
Ne pas publier la proposition ou le mapping comme canonique. Isoler l'objet, conserver la référence reçue et demander une provenance conforme avant reprise.

### Conflit de version ou contrat incompatible
Refuser l'interprétation silencieuse. Placer l'entrée en revue/quarantaine, conserver versions source/contrat et reprendre uniquement après résolution explicite.

### Corruption ou incohérence taxonomique
Suspendre les mutations concernées. Identifier la dernière version cohérente, contrôler relations/mappings affectés, restaurer ou corriger par workflow gouverné puis republier une nouvelle version.

### Publication canonique erronée
Ne pas réécrire silencieusement l'historique. Invalider/retirer la version fautive selon sa sémantique, produire une version corrigée et propager l'état aux consommateurs.

### Store autoritatif indisponible
Servir uniquement la dernière version explicitement valide lorsque le mode dégradé l'autorise. Bloquer les mutations qui exigent l'autorité. Aucun cache ou consommateur ne devient autorité de secours.

## Backup / Restore

Ordre : geler les mutations si nécessaire → identifier backup/version cible → restaurer store et métadonnées de gouvernance → vérifier intégrité/version/provenance → réconcilier événements/projections sortantes → contrôler consommateurs critiques → rouvrir les mutations.

Le restore doit être testé avant production. RPO/RTO, cadence et technologie restent `TBD-PREPROD`.

## Escalade

Technical Owner pilote l'incident technique. Taxonomy Governance Owner arbitre les mutations canoniques. Data Governance intervient sur provenance/qualité. Security/Privacy Reviewer intervient en cas d'accès indu ou de donnée protégée. L'owner de la source participe lorsqu'une evidence externe est contestée.

Les coordonnées nominatives et astreintes restent dans le registre organisationnel opérationnel.
