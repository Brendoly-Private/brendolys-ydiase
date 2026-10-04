# YD-MS-AI-002 — Retrieval & Grounding

Statut : `autonomy-profile-draft`

- Classification : `DERIVED`, criticité C2. État actuel : `REBUILD-UNVERIFIED`.
- Autorité : corpus/index de grounding et références de citations; jamais autorité sur les faits métier sources.
- Sources : SRH, KNW et sources autorisées selon finalité CNS. Chaque corpus doit enregistrer source, contrat/version, droit d’usage, territoire, rétention et provenance.
- Checkpoint/watermark : watermark par corpus/source; une réponse ne peut prétendre être fondée sur une source dont la fraîcheur/provenance est UNKNOWN lorsque cette source est requise.
- Replay : ingestion/replay idempotents; gèrent doublons, correction/retrait documentaire, révocation de droit, suppression privacy et réindexation après changement de chunking/embedding.
- Reconstruction : FULL_REBUILD des corpus/index; PARTIAL_REBUILD par corpus/source/tenant autorisé; CATCH_UP depuis checkpoint valide.
- Fraîcheur : FRESH/STALE-ACCEPTABLE/EXPIRED/UNKNOWN, seuils par type de corpus TBD-PREPROD. EXPIRED/UNKNOWN interdit pour une preuve présentée comme actuelle.
- Intégrité : citations résolubles, provenance, versions, documents retirés absents, pas de chunks orphelins/dupliqués, couverture attendue contrôlée.
- Panne : abstention si evidence, droits ou fraîcheur sous seuil; aucune réponse prétendue fondée sans références suffisantes.
- Sécurité : filtrage finalité/tenant, défense contre contenu non fiable, minimisation des passages et propagation des retraits.
- Scaling : indexation/embedding et requêtes séparables; budget de rebuild distinct.
- IAM : M2M; I diagnostic contrôlé. Repo : `brendolys-ydiase-ai-retrieval-grounding`.
- DR/test : destruction contrôlée d’un corpus/index + FULL_REBUILD avec contrôle des citations et retraits.
- Gates : corpus admissibles/droits; sources/versions/rétention; watermark; seuils grounding/fraîcheur; FULL_REBUILD; `REBUILDABLE`; RTO/SLO; tests sécurité AI.