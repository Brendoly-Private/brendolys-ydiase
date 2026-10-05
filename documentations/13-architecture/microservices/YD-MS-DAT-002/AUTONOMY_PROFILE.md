# YD-MS-DAT-002 — Data Acquisition

Statut : `C2-BASELINE / ACQUISITION-RAW-SEMANTICS-CLOSED`

- Autorité : batches d’acquisition, enveloppes raw et état connecteurs; pas la vérité métier publiée.
- C2, backup AUTH selon nécessité de replay et droits de conservation. I/M2M; N seulement canal contrôlé.
- Dépendances : DAT-001, AMB/Institution channels, sources externes.
- Panne : queue, retry, backpressure; aucune publication directe vers domaines sans provenance/validation.
- Sécurité : isolation connecteurs, secrets par source, raw chiffré, quarantaine, limites de taille/type.
- Repo : `brendolys-ydiase-data-acquisition`.
- Gate : politique raw/replay/rétention, connecteurs, quotas, SLO/RPO/RTO, restore.

- Politique normative : `DATA_GOVERNANCE_POLICY.md`.
- Gates restant : connecteurs réels, quotas, politique raw/replay/rétention, SLO/RPO/RTO et restore.
