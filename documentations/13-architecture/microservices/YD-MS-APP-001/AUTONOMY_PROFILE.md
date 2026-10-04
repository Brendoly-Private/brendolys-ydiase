# YD-MS-APP-001 — Application

Statut : `autonomy-profile-draft`

- Autorité : candidatures, états et transitions.
- C1, backup AUTH; PII et données de recrutement sensibles.
- IAM : C candidat, C organisation via permissions explicites, I support, M2M.
- Dépendances : OPP validation, EMP-002 commandes de décision, CNS, NTF.
- Panne : nouvelle soumission bloquée si opportunité non validable; dernier état consultable; commandes idempotentes.
- Sécurité : contrôle candidat/employeur par objet, audit complet des transitions, aucune écriture directe par Employer Workspace.
- Repo : `brendolys-ydiase-application`.
- Gate : machine d’état, rétention légale, scopes, SLO/RPO/RTO, restore et tests d’idempotence.