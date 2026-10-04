# YD-MS-ASM-001 — Assessment

Statut : `autonomy-profile-draft`

- Autorité : sessions, réponses, résultats, validité et confidence des évaluations.
- C1, backup AUTH; données de profilage sensibles.
- IAM : C sujet, I support autorisé, M2M.
- Dépendances : Identity, CNS, CFG; publie AssessmentCompleted vers ORI/REC.
- Panne : reprise de session selon règles; calcul/stockage sensible suspendu si privacy requise non vérifiable.
- Sécurité : contrôle objet strict, audit, minimisation, version de méthodologie liée au résultat.
- Repo : `brendolys-ydiase-assessment`.
- Gate : méthodologies, rétention, règles mineurs, scopes, SLO/RPO/RTO, restore et tests sécurité.