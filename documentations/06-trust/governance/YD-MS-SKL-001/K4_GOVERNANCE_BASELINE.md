---
document_id: "YD-DOC-TRU-SKL-001-K4-GOVERNANCE-BASELINE"
title: "YD-MS-SKL-001 — K4 Governance Baseline"
document_type: "governance-baseline"
document_role: "Établit une règle ou baseline normative de gouvernance, confidentialité ou sécurité."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "trust"
created_at: "2026-10-06"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-SKL-001 — K4 Governance Baseline

> **Rôle du document**
> Établit une règle ou baseline normative de gouvernance, confidentialité ou sécurité.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `K4-PASS / GOVERNANCE-BASELINE-CLOSED / K5-EVIDENCE-PENDING`
Nature : `AUTH`
Criticité : `C2`

## 1. Classification

SKL-001 possède des référentiels métier autoritatifs, principalement non personnels.

- `PUBLIC` : compétences, concepts, relations et taxonomies explicitement publiables.
- `INTERNAL` : versions de travail, métadonnées de gouvernance, états de workflow et paramètres internes.
- `CONFIDENTIAL` : evidence non publique, propositions de mapping, sources contractuellement restreintes et éléments de revue.
- `SENSITIVE` : provenance ou contenu source dont la diffusion pourrait exposer une information protégée.
- Les profils individuels et `UserSkill` ne relèvent pas de l'ownership SKL-001.

La classification de la source prévaut lorsqu'elle est plus restrictive. Une projection SKL ne réduit jamais la classification de sa source par défaut.

## 2. Sécurité

- authentification service-à-service pour mutations et intégrations ;
- autorisation séparée entre lecture publique, lecture interne, proposition, revue et publication canonique ;
- aucune source EDU/CAR/DAT ne peut publier directement une mutation canonique ;
- une IA peut proposer, jamais publier seule ;
- provenance, version et identité de l'acteur/processus de gouvernance sont obligatoires pour toute mutation canonique ;
- secrets et credentials restent hors payload métier ;
- journalisation des créations, changements de statut, mappings, relations, publications, retraits et restaurations ;
- les mécanismes IAM physiques restent `TBD-IMPLEMENTATION` et devront être vérifiés à K5/PREPROD.

## 3. Privacy et rétention

SKL-001 n'est pas l'autorité des profils individuels. Les données personnelles ne doivent pas être copiées dans le référentiel canonique pour justifier une compétence ou un mapping.

Lorsqu'une evidence source contient des données personnelles ou restreintes, SKL conserve uniquement les références/provenances nécessaires et autorisées. Minimisation, finalité, classification source et droits de retrait s'appliquent.

Les durées numériques de rétention des evidence, journaux de gouvernance et versions restent `TBD-PREPROD`. La méthode de fermeture consiste à les fixer par classe de donnée, obligations pays/source, besoin d'audit et stratégie de recovery avant activation.

## 4. Criticité et objectifs opérationnels

Criticité : `C2`.

Le store SKL est autoritatif et doit disposer d'un backup/restore indépendant. En panne, une dernière taxonomie versionnée peut rester lisible uniquement si son état et sa fraîcheur sont explicites ; les nouvelles mutations ou mappings nécessitant une autorité indisponible sont bloqués.

À mesurer avant ACTIVE :
- disponibilité lecture et mutation ;
- RPO/RTO ;
- fraîcheur des publications/projections ;
- délai de validation des propositions ;
- propagation des retraits et changements de version ;
- durée et taux de succès des restaurations.

Les valeurs numériques restent `TBD-PREPROD`.

## 5. Observabilité

### Logs
Mutations canoniques, propositions, décisions de revue, acteur/processus, versions avant/après, provenance, publication/retrait, erreurs de compatibilité, opérations de backup/restore.

### Métriques
Taux de mutation, propositions en attente, rejets, mappings sans provenance valide, conflits de version, âge des propositions, latence de publication, erreurs de projection, état des backups et résultats de restore.

### Alertes
Mutation non autorisée, publication sans provenance/version, tentative de publication autonome IA, conflit de version, backlog de gouvernance, projection incompatible, échec backup/restore et corruption/incohérence taxonomique.

## 6. Backup et recovery

SKL-001 est `AUTH` : EDU, CAR, DAT, caches ou projections consommateurs ne peuvent pas reconstruire l'autorité SKL.

La stratégie exige :
- backups versionnés du store autoritatif ;
- conservation cohérente des métadonnées de gouvernance et de provenance ;
- procédure de restore indépendante ;
- validation d'intégrité après restauration ;
- réconciliation des projections sortantes après restore ;
- test de restore reproductible avant production.

RPO, RTO, rétention des backups, technologie et cadence de test restent `TBD-PREPROD`.

## 7. Procédure opérationnelle

Le runbook canonique est `07-operations/runbooks/YD-MS-SKL-001/RUNBOOK.md`.

Il couvre au minimum : mutation non autorisée, provenance absente, conflit/version incompatible, corruption taxonomique, publication erronée, indisponibilité du store autoritatif, restore et reprise des projections.

## 8. Ownership

Rôles gouvernés :
- Skills Knowledge Business Owner ;
- Taxonomy Governance Owner ;
- Technical Owner ;
- Data Governance Owner ;
- Security/Privacy Reviewer ;
- owners des sources lorsqu'une evidence externe est contestée.

Les identités nominatives sont gérées dans le registre organisationnel afin d'éviter de figer des personnes dans cette baseline.

## 9. TBD-PREPROD

À fermer avant activation :
- RPO/RTO et disponibilité cible ;
- rétention des versions, evidence, logs et backups ;
- mécanismes IAM physiques ;
- cadence et critères de restore test ;
- seuils d'alerting et backlog de gouvernance ;
- capacité et performance ;
- délais de propagation/dépréciation contractuelle.

## 10. Évaluation du gate K4

| Critère K4 | État | Preuve principale |
|---|---|---|
| dataClassification | PASS | §1 |
| securityControls | PASS | §2 |
| privacyAndRetentionWhenApplicable | PASS | §3 ; paramètres numériques gouvernés en PREPROD |
| sloOrCriticality | PASS | §4 |
| observability | PASS | §5 |
| backupRecoveryWhenStateful | PASS | §6 + lifecycle SKL |
| runbookOrOperationalProcedure | PASS | §7 + runbook canonique |
| namedOwners | PASS | §8 |

### Verdict

`YD-MS-SKL-001` satisfait le gate documentaire **K4 — Gouverné**.

Ce verdict ne signifie ni restore testé, ni PREPROD validée, ni production. Les preuves exécutées appartiennent à K5 et aux gates d'implémentation/PREPROD.

## 11. Gate K5

K5 exigera au minimum : validation automatisée applicable, contract tests, vérification des contrôles d'autorisation, tests de mutation/version/provenance, test backup/restore, vérification d'intégrité après restore, preuves observables et zéro gap critique.
