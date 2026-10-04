# YD-MS-DAT-003 — Data Provenance

Statut : `autonomy-profile-draft`

- Autorité : lineage, assertions de provenance, preuves/références et chaînes de transformation.
- C1, backup AUTH renforcé. I/M2M.
- Dépendances : DAT-002 et sources référencées.
- Panne : écriture/retry durable; promotion aval suspendue lorsqu’une preuve obligatoire manque.
- Sécurité : append/history, intégrité, audit, accès restreint aux preuves sensibles; aucune altération silencieuse.
- Repo : `brendolys-ydiase-data-provenance`.
- Gate : modèle lineage, immutabilité/versioning, SLO/RPO/RTO, restore vérifié et réconciliation.