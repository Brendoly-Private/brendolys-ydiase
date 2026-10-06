# YD-MS-KNW-001 — Runbook

Statut : `OPERATIONAL-PROCEDURE-BASELINE / IMPLEMENTATION-PENDING`

## Triage

Identifier : source affectée, contract/source version, graph version, watermark, type d'incident, portée des projections et éventuel impact Privacy.

## Incidents

### Source ou contrat incompatible
1. arrêter l'application du payload incompatible ;
2. placer en quarantaine ;
3. conserver payload/ref et motif selon règles de rétention ;
4. alerter Technical Owner et owner source ;
5. reprendre uniquement après compatibilité validée ou nouvelle version contractuelle.

### Provenance manquante
Ne pas exposer la relation comme fiable. Isoler la projection et rechercher la source/version manquante.

### DELETE/WITHDRAW/REVOKE non propagé
Priorité élevée. Identifier toutes les projections dépendantes, retirer/invalider, vérifier Search/GraphRAG et produire une trace d'audit.

### Divergence du graphe
Geler les publications concernées si nécessaire. Capturer versions/watermarks. Lancer PARTIAL ou FULL_REBUILD selon portée. Comparer convergence avant réouverture.

### KNW indisponible
Les consommateurs utilisent leur mode dégradé sans KNW. Aucun consommateur ne doit promouvoir son cache KNW comme autorité primaire.

### Entity resolution incorrecte
Suspendre la fusion/relation concernée, conserver evidence/version, corriger la règle gouvernée puis reconstruire les projections impactées.

## Recovery

Ordre : restaurer règles/configurations → vérifier sources/replay → reconstruire → valider provenance/intégrité → comparer convergence → rouvrir les lectures/enrichissements.

## Escalade

Technical Owner pilote l'incident. Data Governance intervient sur provenance/qualité. Security/Privacy Reviewer intervient immédiatement si PII, accès indu ou retrait non propagé. L'owner source arbitre la vérité métier.

Les coordonnées et astreintes sont référencées dans le registre organisationnel opérationnel.
