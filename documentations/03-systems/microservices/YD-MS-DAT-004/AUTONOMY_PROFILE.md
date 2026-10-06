# YD-MS-DAT-004 — Data Quality & Validation

Statut : `C1-BASELINE / QUALITY-VALIDATION-SEMANTICS-CLOSED`

- Autorité : règles qualité, runs, décisions de validation et anomalies.
- C1, backup AUTH. I/M2M.
- Dépendances : DAT-002/003/005.
- Panne : quarantaine; aucune promotion automatique si validation impossible ou échoue.
- Sécurité : séparation règle/exécution/décision, version des règles, audit overrides manuels.
- Repo : `brendolys-ydiase-data-quality-validation`.
- Gate : seuils par classe de données, override governance, SLO/RPO/RTO, restore et contrats.

- Politique normative : `DATA_GOVERNANCE_POLICY.md`.
- Gates restant : seuils par classe, règles réelles, gouvernance overrides, SLO/RPO/RTO et restore.
