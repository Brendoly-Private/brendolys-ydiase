# YD-MS-EMP-002 — Talent & Recruitment

Statut : `C1-BASELINE / TALENT-RECRUITMENT-SEMANTICS-CLOSED`

- Autorité : campagnes, viviers autorisés et décisions de sélection; APP reste owner de l’état candidature.
- C1, backup AUTH. C organisations, I, M2M.
- Dépendances : EMP-001, APP, OPP-002, CNS.
- Panne : campagnes consultables; décision mise en attente si Application indisponible; jamais d’état candidature concurrent.
- Sécurité : tenant isolation, accès recruteur, minimisation des profils candidats, audit des décisions.
- Repo : `brendolys-ydiase-talent-recruitment`.
- Gate : permissions recruteur, finalités traitement candidats, SLO/RPO/RTO, restore, contrats APP.

- Politique normative : `TALENT_ACCESS_RECRUITMENT_POLICY.md`.
- Gates restant : policy sourcing proactif, fairness, rôles/scopes, rétention pays, BIA/RPO/RTO, restore et contrats APP.
