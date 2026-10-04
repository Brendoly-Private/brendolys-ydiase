# YD-MS-ORI-001 — Orientation & Decision Support

Statut : `autonomy-profile-draft`

- Logique : ORI-001 + ORI-002. Autorité sur dossiers, objectifs/contraintes de décision, comparaisons et choix enregistrés.
- C1, backup AUTH. C/I/M2M.
- Dépendances : PRF, ASM, REC, CNS; Recommendation via job/contrat sans boucle synchrone circulaire.
- Panne : dossier consultable; nouvelle recommandation en attente; dernier résultat uniquement s’il est daté et présenté comme tel.
- Sécurité : profilage, explications, finalités et accès objet audités. Decision Support ne crée pas une vérité concurrente du ranking REC.
- Repo : `brendolys-ydiase-orientation-decision`.
- Gate : SLO/RPO/RTO, durée de conservation dossiers, règles mineurs, workflow REC, restore et contrats.