# YD-MS-LAB-002 — Labor Market Intelligence

Statut : `C2-BASELINE / LABOR-INTELLIGENCE-SEMANTICS-CLOSED`

- Autorité : indicateurs/séries/méthodologies publiés; signaux LAB-001 restent source amont.
- C2, backup MIXED. I/M2M, lectures produit autorisées via surfaces gouvernées.
- Dépendances : LAB-001, CFG. Fournit datasets dérivés à Analytics/REC/produits.
- Panne : dernière édition datée reste exploitable; recalcul différé; fraîcheur toujours visible.
- Sécurité : méthodologie/version et provenance agrégée liées à chaque édition; pas de PII dans produits agrégés sauf justification distincte.
- Repo : `brendolys-ydiase-labor-intelligence`.
- Gate : méthodologies, seuils publication, SLO/RPO/RTO, restore, critères d’extraction Forecasting.

- Politique normative : `LABOR_INTELLIGENCE_POLICY.md`.
- Gates restant : méthodologies numériques, seuils de tension/couverture, backtesting Forecasting, SLO/RPO/RTO et restore.
