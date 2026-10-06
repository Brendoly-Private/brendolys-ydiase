# YD-MS-KNW-001 — Knowledge Graph

Statut : `C2-BASELINE / KNOWLEDGE-GRAPH-SEMANTICS-CLOSED`

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

- Politiques normatives : `KNOWLEDGE_GRAPH_PROJECTION_POLICY.md` et `KNW_TO_SEARCH_PROJECTION_CONTRACT.md`.
- Classes de relations : SOURCE-ASSERTED, DETERMINISTIC-DERIVED, INFERRED, CURATED-GRAPH ; aucune inférence ne devient vérité métier sans validation de l'owner.
- Dépendance SRH : enrichment optionnel/reconstructible; Search primaire ne dépend pas synchroniquement de KNW.
- Gates restant : ontology/schema physique, contrats/replay, seuils confidence/freshness, FULL_REBUILD réussi, RTO/SLO et tests intégrité/Privacy.
