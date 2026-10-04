# YD-MS-EMP-002 — Talent & Recruitment

Statut : `autonomy-profile-draft`

- Autorité : campagnes, viviers autorisés et décisions de sélection; APP reste owner de l’état candidature.
- C1, backup AUTH. C organisations, I, M2M.
- Dépendances : EMP-001, APP, OPP-002, CNS.
- Panne : campagnes consultables; décision mise en attente si Application indisponible; jamais d’état candidature concurrent.
- Sécurité : tenant isolation, accès recruteur, minimisation des profils candidats, audit des décisions.
- Repo : `brendolys-ydiase-talent-recruitment`.
- Gate : permissions recruteur, finalités traitement candidats, SLO/RPO/RTO, restore, contrats APP.