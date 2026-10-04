# YD-MS-MOD-001 — Moderation

Statut : `autonomy-profile-draft`

- Autorité : politiques, dossiers et décisions de modération; owner métier applique l’effet sur son objet.
- C1, backup AUTH. C/N pour signalement limité, I modérateurs, M2M.
- Dépendances : CNT, COM, MKT, SPN, AUD.
- Panne : objet explicitement bloqué reste fail-closed; décisions vers owners en retry; aucun accès DB direct aux objets.
- Sécurité : séparation policy/décision, RBAC modérateur, audit complet, protection contre abus internes.
- Repo : `brendolys-ydiase-moderation`.
- Gate : owner de politique formalisé, appels/recours, SLA décision, SLO/RPO/RTO, restore.