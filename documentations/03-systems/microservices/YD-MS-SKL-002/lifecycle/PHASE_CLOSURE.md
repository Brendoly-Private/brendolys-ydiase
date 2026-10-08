---
document_id: "YD-DOC-MS-SKL-002-CLS"
title: "YD-MS-SKL-002 — User Skills Profile — Baseline C1"
document_type: "microservice-phase-closure"
document_role: "Consigne la fermeture de phase documentaire de YD-MS-SKL-002 et les travaux ou preuves restant différés."
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
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-SKL-002 — User Skills Profile — Baseline C1

> **Rôle du document**
> Consigne la fermeture de phase documentaire de YD-MS-SKL-002 et les travaux ou preuves restant différés.
> **Usage développement :** preuve de maturité ou de fermeture ; le profil canonique et les politiques référencées restent autoritatifs.

Statut : `DOCUMENTATION-BASELINE-C1 / SEMANTICS-DEFINED`
Nature : `AUTH`
Criticité : `C1`
Classification : profilage individuel sensible

## Autorité
SKL-002 possède UserSkill, SkillEvidence, SkillAssessmentState, SkillHistory et les versions de l'état individuel.

Il ne possède ni Skill canonique, ni AssessmentResult, ni EducationRecord/ExperienceRecord, ni identité, ni décision Privacy.

## Invariants
- contrôle objet par sujet ;
- support interne strictement autorisé et audité ;
- networks sans accès par défaut ;
- projections minimisées par finalité ;
- toute compétence individuelle conserve SkillRef/version, provenance/evidence, méthode, fraîcheur et état de confiance applicables ;
- une correction de source ne doit pas produire une réécriture opaque de l'historique ;
- IA/inférence ne devient jamais silencieusement une vérité individuelle autoritative ;
- datastore, secrets, workload identity, backup et restore propres.

## Dépendances
Identity, PRF-001, PRF-002, SKL-001, ASM-001 et CNS-001.

CNS est fail-closed lorsque la finalité exige une décision vérifiable. Une panne d'une source de preuve n'autorise pas l'invention ou la reconstruction de l'état UserSkill.

## Récupération
SKL-002 doit restaurer son autorité depuis sa propre chaîne de recovery. PRF-002, ASM-001 et SKL-001 ne sont jamais des backups de UserSkill/SkillHistory.

Les références de preuve peuvent rester non résolues après restore jusqu'à réconciliation.

## Sémantique de dérivation
La politique normative est définie dans `SKILL_STATE_DERIVATION_POLICY.md`. Elle ferme le modèle de proficiency, la séparation niveau/confiance/fraîcheur, les preuves, contradictions, corrections/révocations, historique append-only, inférences et reproductibilité.

Restent bloquants avant ACTIVE :
- coefficients/seuils validés des politiques de dérivation ;
- durées de fraîcheur validées par famille/type ;
- finalités Privacy et rétention ;
- contrôles d'accès horizontal ;
- validations métier/psychométriques applicables.

## Gates C1 avant production
- BIA ;
- RPO/RTO/SLO ;
- backup/restore policy ;
- restore indépendant testé ;
- tests IAM/IDOR/horizontal access ;
- audit accès sensibles ;
- Privacy/DPIA si applicable ;
- runbook incident/DR lié à l'implémentation.

Contrairement à PRF-002, ces documents C1 détaillés ne sont pas fabriqués prématurément : ils seront produits lorsque les règles de dérivation et l'architecture physique seront suffisamment stables pour générer des preuves réelles.

Statut : `C1-BASELINE-ESTABLISHED — SEMANTICS-CLOSED / VALIDATION-PRIVACY-PREPROD-PENDING`.
