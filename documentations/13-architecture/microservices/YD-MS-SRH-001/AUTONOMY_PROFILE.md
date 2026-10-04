# YD-MS-SRH-001 — Search & Discovery

Statut : `autonomy-profile-draft`

- Classification : `DERIVED`, criticité C2. État actuel : `REBUILD-UNVERIFIED` jusqu’au premier FULL_REBUILD réussi.
- Autorité : index uniquement; aucune autorité sur EDU, CAR, OPP, CNT ou LRN.
- Sources de reconstruction : projections versionnées de EDU, CAR, OPP, CNT et LRN. Les contrats/versions exacts et leurs rétentions seront enregistrés au Contract Registry; ils constituent un gate préproduction.
- Checkpoint/watermark : position par flux/partition source obligatoire. Un timestamp local seul est interdit. Le mécanisme physique reste ADR-REQUIRED.
- Replay : idempotent; doublons, événements hors ordre, suppressions, retraits d’opportunités, dépublication de contenu et révocations applicables doivent converger vers l’état source.
- Reconstruction : `FULL_REBUILD` de tous les index; `PARTIAL_REBUILD` par type d’objet/partition; `CATCH_UP` depuis checkpoint valide.
- Fraîcheur : états `FRESH`, `STALE-ACCEPTABLE`, `EXPIRED`, `UNKNOWN`; seuils numériques TBD-PREPROD. Les résultats EXPIRED/UNKNOWN ne sont pas présentés comme actuels.
- Intégrité : contrôle de cardinalité, versions, trous, doublons, objets supprimés et références orphelines après rebuild.
- Panne : recherche partielle ou indisponibilité contrôlée; aucun résultat Search ne vaut validation métier.
- Sécurité : indexation minimale, suppression/révocation propagée, aucun secret ni PII inutile dans l’index.
- Scaling : lectures élevées et indexation asynchrone; budget distinct pour rebuild/catch-up.
- IAM : C/N/I/M2M selon surface. Repo : `brendolys-ydiase-search-discovery`.
- DR/test : destruction contrôlée de l’index + FULL_REBUILD obligatoire avant production; conserver durée, fraîcheur finale, positions source et anomalies.
- Gates : contrats/versions et rétention des sources; watermark; FULL_REBUILD réussi; statut `REBUILDABLE`; seuils de fraîcheur; RTO/SLO; politique suppression.