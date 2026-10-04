# YD-MS-LAB-001 — Labor Signals

Statut : `autonomy-profile-draft`

- Autorité : signaux marché normalisés publiés; raw/provenance restent DAT.
- C2, backup AUTH. I/M2M, pas d’écriture client.
- Dépendances : DAT-003/004, CFG, références CAR/SKL.
- Panne : ingestion différée/quarantaine; aucun signal publié sans preuve/qualité minimale.
- Sécurité : source/provenance/territoire/observedAt obligatoires; distinction observation et estimation.
- Repo : `brendolys-ydiase-labor-signals`.
- Gate : seuil qualité, politique expiration, SLO/RPO/RTO, restore et contrats.