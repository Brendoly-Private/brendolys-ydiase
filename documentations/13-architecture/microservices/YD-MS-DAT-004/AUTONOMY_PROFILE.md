# YD-MS-DAT-004 — Data Quality & Validation

Statut : `autonomy-profile-draft`

- Autorité : règles qualité, runs, décisions de validation et anomalies.
- C1, backup AUTH. I/M2M.
- Dépendances : DAT-002/003/005.
- Panne : quarantaine; aucune promotion automatique si validation impossible ou échoue.
- Sécurité : séparation règle/exécution/décision, version des règles, audit overrides manuels.
- Repo : `brendolys-ydiase-data-quality-validation`.
- Gate : seuils par classe de données, override governance, SLO/RPO/RTO, restore et contrats.