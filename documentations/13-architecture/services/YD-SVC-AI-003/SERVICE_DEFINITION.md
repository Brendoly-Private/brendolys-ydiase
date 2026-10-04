# YD-SVC-AI-003 — AI Verification Service

`domain: ai` · `phase: P2` · `documentation: D1` · `implementation: not-started`

## Mission
Évaluer sorties IA selon preuves disponibles, règles, risques et niveaux de confiance.

## Frontière DDD
Ne transforme pas une génération en fait autoritatif. Produit un statut de vérification et des motifs.

## Dépendances
AI Gateway, Retrieval & Grounding, Data Provenance.

## Verdict DDD
`MERGE-CANDIDATE` dans AI Gateway au pilote, frontière logique conservée.

## Activation
Avant tout usage IA ayant effet sur une recommandation utilisateur.