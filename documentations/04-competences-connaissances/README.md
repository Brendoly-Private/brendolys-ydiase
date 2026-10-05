# Domaine 04 — Compétences et connaissances

Statut : `DOMAIN-BASELINE-CANDIDATE`

## Mission

Le domaine Compétences et connaissances sépare deux vérités différentes :

- `SKL-001 — Skills Knowledge` : vocabulaire/taxonomie canonique des compétences et concepts de connaissance ;
- `SKL-002 — User Skills Profile` : état individuel de compétence, niveau, preuves et historique.

Une compétence canonique n'est jamais créée parce qu'un utilisateur, un curriculum, un métier ou une IA la mentionne. Une compétence individuelle n'est jamais stockée dans la taxonomie canonique.

## Criticité

- SKL-001 : `AUTH / C2`.
- SKL-002 : `AUTH / C1`, données personnelles et profilage sensible.

## Doctrine

- IDs Skill/Knowledge durables et taxonomie versionnée ;
- provenance obligatoire pour les relations/mappings gouvernés ;
- evidence EDU/CAR alimente la gouvernance sémantique sans transférer l'ownership ;
- Assessment reste autorité de ses résultats ;
- PRF-002 reste autorité de l'historique Education/Experience ;
- SKL-002 reste autorité de l'état individuel de compétence ;
- IA peut proposer des mappings/inférences mais ne publie jamais seule une vérité canonique ou un niveau individuel autoritatif ;
- projections minimisées selon finalité et Privacy.

Voir `FRONTIERES_ET_DEPENDANCES.md` et `GATES_ET_INCONNUES.md`.
