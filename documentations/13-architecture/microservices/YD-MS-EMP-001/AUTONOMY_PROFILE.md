# YD-MS-EMP-001 — Employer

Statut : `C2-BASELINE / EMPLOYER-SEMANTICS-CLOSED`

- Autorité : employeurs, vérification et statut organisationnel.
- C2, backup AUTH. C organisations, I, M2M.
- Dépendances : PRT, CFG, validation Data selon source.
- Panne : lecture possible; mutation/validation sensible bloquée si preuve requise indisponible.
- Sécurité : isolation organisation, preuve de représentation, audit vérification et changement de statut.
- Repo : `brendolys-ydiase-employer`.
- Gate : modèle organisation/tenant, vérification, scopes, SLO/RPO/RTO, restore.

- Politique normative : `EMPLOYER_VERIFICATION_POLICY.md`.
- Gates restant : règles de vérification par pays, modèle tenant/scopes, IAM/IDOR, SLO/RPO/RTO, restore.
