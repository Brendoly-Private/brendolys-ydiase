# YD-MS-OPP-001 — Opportunity

Statut : `autonomy-profile-draft`

- Autorité : opportunités, exigences, validité et politiques de candidature.
- C1, backup AUTH. C/N/I/M2M selon création/consultation autorisée.
- Dépendances : EMP-001, CFG, MOD. Fournit projection à Matching, Application, Search, Recommendation.
- Panne : lecture du dernier état connu; candidature revalide synchroniquement l’opportunité; publication sensible bloquée si employeur/modération requis non validables.
- Sécurité : anti-fraude, provenance de l’annonce, contrôle organisation, audit publication/retrait.
- Repo : `brendolys-ydiase-opportunity`.
- Gate : vérification employeur, expiration, modération, SLO/RPO/RTO, restore et contrats.