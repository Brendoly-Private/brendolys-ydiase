# YD-PLT-AI-001 — AI Gateway

Statut : `autonomy-profile-draft`

- Rôle : point de contrôle des usages AI, policy gate et routage; aucune vérité métier.
- C1, backup MIXED des policies/config et métadonnées nécessaires; contenu utilisateur selon minimisation/rétention.
- IAM : C/N/I selon use case, M2M; audience dédiée. Identity + CNS obligatoires selon finalité.
- Dépendances : BRENDOLYS Identity, CNS, AI-002/003, modèles approuvés MLP.
- Panne : refuse l’usage si policy, consentement ou approbation modèle requis non vérifiable.
- Sécurité : rate limit, quotas, prompt/input controls, redaction, journalisation sans secrets, isolation tenant/use case.
- Repo : `brendolys-ydiase-ai-gateway`.
- Gate : matrice use-case/realm/purpose/model, SLO/RPO/RTO, secrets, DR et contrats.