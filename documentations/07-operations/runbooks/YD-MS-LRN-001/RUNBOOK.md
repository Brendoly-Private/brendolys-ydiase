---
document_id: "YD-DOC-OPS-LRN-001-RUNBOOK"
title: "YD-MS-LRN-001 — Runbook"
document_type: "operational-runbook"
document_role: "Définit la procédure opérationnelle applicable à YD-MS-LRN-001."
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

# YD-MS-LRN-001 — Runbook

> **Rôle du document**
> Définit la procédure opérationnelle applicable à YD-MS-LRN-001.
> **Usage développement :** référence opérationnelle obligatoire pour l’implémentation et l’exploitation concernées.

Statut : `OPERATIONAL-PROCEDURE-BASELINE / IMPLEMENTATION-PENDING`

## Triage

Identifier : ressource ou RecommendationSet affecté, versions LRN/policy, références EDU/SKL/MKT, fraîcheur, droits d'usage, provenance, finalité Privacy et consommateurs impactés.

## Incidents

### Offre EDU/MKT périmée ou indisponible
Masquer l'offre comme actuelle/achetable lorsque sa disponibilité n'est plus vérifiable. Ne pas supprimer une LearningResource encore valide. Conserver source, version et état de fraîcheur.

### Droits d'usage absents, expirés ou contestés
Suspendre l'exposition ou l'usage concerné. Conserver la référence de droit/provenance, escalader au Content/Learning Owner et ne reprendre qu'après décision gouvernée.

### Mapping gap-learning erroné
Invalider le mapping concerné sans réécrire silencieusement les RecommendationSet historiques. Produire une nouvelle version, identifier les résultats devenus stale et recalculer lorsque applicable.

### Donnée critique UNKNOWN ou stale
Ne jamais convertir `UNKNOWN` en `FAILED` ou en valeur inventée. Appliquer statut conditionnel, masquage ou abstention selon policy.

### Influence commerciale suspectée
Comparer le résultat organique avec et sans données commerciales. Paiement, commission, sponsoring ou statut partenaire ne doivent modifier ni éligibilité ni rang organique. Suspendre la policy/version si cet invariant échoue.

### Privacy/finalité non vérifiable
Bloquer la personnalisation ou utiliser uniquement un mode non personnalisé explicitement autorisé. Minimiser les données conservées dans l'evidence snapshot.

### LRN indisponible
Les autorités EDU, SKL et MKT restent indépendantes. Aucun cache/projection LRN ne devient leur source autoritative. Les consommateurs appliquent leur mode dégradé documenté.

## Backup / Restore

Restaurer les ressources LRN autoritatives, mappings, policies et résultats persistants applicables, puis vérifier versions, provenance, droits d'usage et références externes. Réconcilier ensuite les projections/résultats devenus stale.

RPO/RTO, technologie, cadence et rétention restent `TBD-PREPROD`.

## Escalade

Learning/Product Owner arbitre les règles métier. Technical Owner pilote l'incident technique. Content/Data Governance intervient sur provenance, mappings et droits. Security/Privacy Reviewer intervient sur accès, finalité et données protégées. Les owners EDU/SKL/MKT arbitrent leurs propres vérités.

Les identités nominatives et astreintes restent dans le registre organisationnel.
