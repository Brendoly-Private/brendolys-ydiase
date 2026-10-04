# YD-MS-EDU-003 — Curriculum & Module

Statut : `autonomy-profile-draft`

- Autorité : curricula, modules, versions, mappings pédagogiques.
- Criticité C2, backup AUTH. Version publiée conservée et restaurable.
- IAM : I/N gestion autorisée, C lecture, M2M.
- Dépendances : EDU-002 et SKL-001. Publication exige Program valide; Skill inconnu ne devient jamais canonique ici.
- Contrats : CurriculumPublished et CurriculumSkillEvidence; aucun accès DB de Program/Skills.
- Panne : brouillon possible; publication bloquée sans Program valide; dernière version publiée reste lisible.
- Sécurité : provenance, historique, séparation brouillon/publication, audit des changements structurants.
- Repo : `brendolys-ydiase-curriculum-module`; datastore/migrations/backup propres.
- Gate : SLO/RPO/RTO, workflow publication, tailles/versioning modules, restore et contrats.