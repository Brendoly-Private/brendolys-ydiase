# YD-MS-SKL-001 — Skills Knowledge

Statut : `autonomy-profile-draft`

- Autorité : skills, concepts de connaissance, taxonomie et relations sémantiques.
- C2, backup AUTH. I mutation, C lecture, M2M.
- Dépendances : DAT-005; reçoit evidence EDU/CAR sans leur céder son ownership.
- Panne : dernière taxonomie versionnée; nouveaux mappings inconnus bloqués.
- Sécurité : provenance et version obligatoires; IA peut proposer, jamais publier seule un Skill canonique.
- Scaling : lectures/projections nombreuses; cache reconstruisible séparé du store autoritatif.
- Repo : `brendolys-ydiase-skills-knowledge`.
- Gate : gouvernance taxonomique, workflow validation, SLO/RPO/RTO, restore et contrats.