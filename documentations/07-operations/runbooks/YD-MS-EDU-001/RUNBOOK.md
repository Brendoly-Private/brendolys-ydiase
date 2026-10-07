# YD-MS-EDU-001 — Runbook

Statut : RUNBOOK-BASELINE / IMPLEMENTATION-PENDING
Nature : AUTH
Criticité : C2

## Incidents couverts
Perte ou corruption du datastore, suppression accidentelle, publication institutionnelle incorrecte, erreur de statut, provenance invalide, indisponibilité CFG/DAT, échec de projection et restauration.

## Principes
EDU-001 restaure son autorité depuis sa propre chaîne de backup. Les consommateurs ne servent jamais de source de reconstruction. Une contribution non validée ne devient pas publiée pendant une reprise. Une référence pays/source obligatoire non vérifiable bloque les mutations concernées.

## Séquence de restauration
1. déclarer l'incident et limiter les mutations si l'intégrité est incertaine ;
2. identifier le point de restauration autoritatif ;
3. restaurer dans un environnement contrôlé ;
4. vérifier identifiants durables, versions, statuts, campus et liens de provenance ;
5. réappliquer les décisions de retrait/correction postérieures au point restauré ;
6. vérifier les règles de publication et de séparation contribution/validation ;
7. réconcilier CFG/DAT et les références externes ;
8. republier les projections de façon idempotente ;
9. mesurer perte et durée ;
10. valider le retour au fonctionnement normal.

## Interdictions
Pas de reconstruction depuis EDU-002, Search, KNW, Analytics ou cache. Pas de publication automatique d'une contribution restaurée. Pas d'écrasement silencieux d'une version plus récente.

## Preuves attendues
Version/commit, environnement, point de restore, durée, perte mesurée, contrôles d'intégrité, contrôles de publication/provenance, replay, anomalies, verdict et reviewer.

Ce runbook ne constitue une preuve K5 qu'après exécution traçable.
