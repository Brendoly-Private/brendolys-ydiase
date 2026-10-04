# YD-MS-KNW-001 — Knowledge Graph

Statut : `autonomy-profile-draft`

- Classification : `DERIVED`, criticité C2. État actuel : `REBUILD-UNVERIFIED`.
- Autorité : aucune vérité métier primaire; graphe, mappings et relations sont des projections dérivées avec provenance.
- Sources : EDU, SKL, CAR, LAB et preuves/provenance DAT. Contrats, versions et fenêtres de rétention exactes restent à enregistrer.
- Checkpoint/watermark : watermark par source et partition; le graphe conserve la position source ayant produit chaque génération de projection.
- Replay : idempotent, gère corrections, suppression de nœuds/relations, changements de taxonomie, événements hors ordre et révocations applicables.
- Reconstruction : FULL_REBUILD du graphe depuis sources gouvernées; PARTIAL_REBUILD par sous-graphe/type/territoire; CATCH_UP depuis watermark cohérent.
- Fraîcheur : FRESH/STALE-ACCEPTABLE/EXPIRED/UNKNOWN avec seuils TBD-PREPROD. Toute relation exposée doit garder provenance et version source suffisantes.
- Intégrité : nœuds/références orphelins, cardinalités, relations invalides, trous de versions, doublons et cohérence provenance vérifiés après rebuild.
- Panne : version précédente datée si dans limite de fraîcheur, sinon indisponibilité/reconstruction; jamais source autoritative de secours.
- Sécurité : minimisation PII, suppression propagée, provenance obligatoire de chaque relation.
- Scaling : stockage/compute spécialisé permis par ADR; budget de rebuild distinct.
- IAM : I/M2M. Repo : `brendolys-ydiase-knowledge-graph`.
- DR/test : destruction contrôlée du graphe + FULL_REBUILD avant production et selon cadence C2.
- Gates : sources/versions/rétention; watermark; stratégie rebuild; FULL_REBUILD réussi; `REBUILDABLE`; freshness; RTO/SLO; seuils d’usage.