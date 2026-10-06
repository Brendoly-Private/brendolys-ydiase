# YD-MS-AI-003 — AI Verification

Statut : `autonomy-profile-draft`

- Autorité : décisions de vérification AI, evidence refs, règles/version de vérification.
- C1, backup AUTH. M2M, I diagnostic.
- Dépendances : outputs AI, grounding et sources de preuve. Indépendance obligatoire du générateur.
- Panne : fail-closed pour usage exigeant vérification; aucun générateur ne s’auto-valide.
- Sécurité : séparation des rôles, audit des overrides, evidence immutable/versionnée, tests adversariaux.
- Repo : `brendolys-ydiase-ai-verification`.
- Gate : classes d’usage exigeant vérification, seuils, SLO/RPO/RTO, restore, politique override.