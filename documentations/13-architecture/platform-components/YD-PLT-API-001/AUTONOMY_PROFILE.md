# YD-PLT-API-001 — External API Management

Statut : `autonomy-profile-draft`

- Rôle : exposition API externe, clients, quotas techniques, routage/policies; aucune donnée métier autoritative.
- C1, backup MIXED pour config clients/quotas/counters nécessaires. C organisations/API clients, I, M2M.
- Dépendances : BRENDOLYS Identity, BIL entitlements, backends exposés.
- Panne : auth/entitlement fail-closed; throttling; backend défaillant isolé sans cascade.
- Sécurité : mTLS/workload identity selon ADR, rate limits, WAF/gateway controls, rotation credentials, audit accès.
- Repo : `brendolys-ydiase-external-api-management`.
- Gate : classes API, onboarding clients, quotas, SLO/RPO/RTO, DR et contrats.