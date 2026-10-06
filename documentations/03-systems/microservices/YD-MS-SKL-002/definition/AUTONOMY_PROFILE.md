# YD-MS-SKL-002 — User Skills Profile

Statut : `autonomy-profile-draft`

- Autorité : compétences individuelles, niveaux, preuves et versions.
- C1, backup AUTH, PII/profilage sensible.
- IAM : C propriétaire, I support strict, M2M. N sans accès par défaut.
- Dépendances : PRF, SKL-001, CNS, Identity.
- Panne : lecture bornée possible; écriture/évaluation sensible suspendue si identité ou privacy requise non vérifiable.
- Sécurité : contrôle objet par sujet, minimisation des projections, audit accès, rétention par finalité.
- Repo : `brendolys-ydiase-user-skills-profile`; datastore/secrets/workload identity propres.
- Gate : DPIA/privacy si applicable, scopes, SLO/RPO/RTO, rétention, restore et tests d’accès horizontal.