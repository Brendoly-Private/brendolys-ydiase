# YD-MS-SKL-002 — User Skills Profile — Baseline C1

Statut : `DOCUMENTATION-BASELINE-C1 / IMPLEMENTATION-GATES-OPEN`
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

## Gates bloquants avant implémentation/ACTIVE
- modèle de proficiency/niveau versionné ;
- règles de dérivation, expiration, correction et invalidation ;
- traitement de confiance/fraîcheur/provenance ;
- finalités Privacy et rétention ;
- politique d'inférence et validation ;
- contrôles d'accès horizontal.

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

Statut : `C1-BASELINE-ESTABLISHED — DERIVATION/PRIVACY GATES BLOCK IMPLEMENTATION`.
