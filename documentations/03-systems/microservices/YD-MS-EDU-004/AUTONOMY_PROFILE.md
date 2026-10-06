# YD-MS-EDU-004 — Qualification Framework

Statut : `autonomy-profile-draft`

- Autorité : qualifications, niveaux, équivalences, prérequis et versions par pays.
- Criticité C2, backup AUTH.
- IAM : I mutation, C lecture, M2M. N uniquement si rôle futur explicitement autorisé.
- Dépendances : CFG et DAT-005. Fournit projections à Program, Profile et Career.
- Panne : dernière version valide reste disponible; nouveaux mappings/équivalences bloqués si référentiel pays absent.
- Sécurité : provenance obligatoire des équivalences, audit et historisation; aucune équivalence générée par IA comme vérité.
- Repo : `brendolys-ydiase-qualification-framework`; datastore privé.
- Gate : Country Framework Burkina, règles de validation, RPO/RTO/SLO, restore et contrats.