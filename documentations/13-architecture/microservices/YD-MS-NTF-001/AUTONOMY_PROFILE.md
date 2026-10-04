# YD-MS-NTF-001 — Notification

Statut : `autonomy-profile-draft`

- Autorité : demandes de livraison, tentatives et états de livraison; jamais état métier source.
- C2, backup AUTH pour preuve/livraison selon rétention. M2M principal; I support.
- Dépendances : CNS/PRF préférences et providers externes.
- Panne : queue/retry/DLQ; panne notification ne rollback pas une transaction métier sauf règle explicite documentée.
- Sécurité : contenu minimal, secrets provider isolés, marketing fail-closed si permission inconnue, logs sans tokens.
- Repo : `brendolys-ydiase-notification`.
- Gate : canaux/providers, idempotence, rétention, SLO/RPO/RTO, DR et contrats.