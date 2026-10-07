---
document_id: "YD-DOC-OPS-KNW-001-FULL-REBUILD-TEST-PROTOCOL"
title: "YD-MS-KNW-001 — FULL_REBUILD Test Protocol"
document_type: "operations-verification"
document_role: "Définit un protocole ou plan de vérification opérationnelle servant de preuve contrôlée."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "evidence"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "operations"
---

# YD-MS-KNW-001 — FULL_REBUILD Test Protocol

> **Rôle du document**
> Définit un protocole ou plan de vérification opérationnelle servant de preuve contrôlée.
> **Usage développement :** référence de support pour la conception, la vérification ou la contextualisation concernée.

Statut : `TEST-PROTOCOL-DEFINED / NOT-EXECUTED`

## Objectif

Vérifier qu'un graphe KNW vide peut être reconstruit depuis les sources gouvernées et converger vers le même état logique attendu pour un même snapshot source.

## Préconditions

Le rapport d'exécution doit identifier : commit/version KNW, versions schema/ontology/règles, contrats sources, dataset ou snapshot immuable, watermarks, configuration, environnement et reviewer. Une précondition critique absente donne `BLOCKED`.

## Dataset minimal

Couvrir plusieurs domaines sources, relations SOURCE-ASSERTED et DETERMINISTIC-DERIVED, versions successives, retrait/révocation, doublons, événements hors ordre, provenance valide/invalide, résolution d'entités et objet non publiable.

## FULL_REBUILD

1. capturer l'état logique et les watermarks de référence ;
2. partir d'un graphe vide contrôlé ;
3. charger règles/configurations versionnées ;
4. reconstruire depuis les sources autorisées ;
5. rejouer jusqu'aux watermarks ;
6. contrôler l'intégrité ;
7. capturer GraphVersion ;
8. comparer à l'état attendu ;
9. vérifier provenance, versions, retraits et classification ;
10. enregistrer durée, erreurs, quarantaines et verdict.

## Convergence

Doivent converger : nœuds publiables, edges/assertions, source refs/versions, classes de relation, provenance, validité/retraits, versions de dérivation et watermarks. Les seules différences tolérées sont des métadonnées techniques explicitement non déterministes.

## Scénarios complémentaires

### Idempotence
Rejouer le même lot. Aucun doublon ni changement logique ne doit apparaître.

### Hors ordre
Perturber une séquence versionnée. L'état final doit respecter versionnement et temporalité.

### DELETE / WITHDRAW / REVOKE
Vérifier retrait, invalidation ou non-exposition des projections dépendantes.

### Provenance manquante
La relation concernée ne doit pas être exposée comme fiable ; rejet ou quarantaine doit être observable.

### Entity resolution
Une similarité de nom ne doit pas fusionner automatiquement deux entités. Une correction gouvernée doit produire l'état attendu après reconstruction.

### Privacy
Une donnée interdite/non publiable ne doit pas apparaître dans l'état exposable.

## CATCH_UP et PARTIAL_REBUILD

Après FULL_REBUILD, appliquer un changement contrôlé puis exécuter CATCH_UP et PARTIAL_REBUILD. Leur état final doit converger avec un FULL_REBUILD sur le même snapshot.

## KNW vers Search

Vérifier que Search primaire fonctionne sans enrichment KNW, qu'un enrichment stale peut être désactivé sans retirer le document source valide et que graph_version/watermark restent traçables.

## PASS

PASS exige reconstruction terminée, convergence, idempotence, retraits corrects, provenance, entity resolution, Privacy et modes de reconstruction applicables vérifiés. Sinon verdict `FAIL` ou `BLOCKED`.

## Rapport attendu

Chaque exécution produit un rapport versionné sous `documentations/_meta/evidence/verification/YD-MS-KNW-001/runs/` avec versions, environnement, dataset, suite utilisée, résultats, métriques, divergences et verdict.

Ce protocole n'est pas lui-même une preuve K5 tant qu'il n'a pas été exécuté.
