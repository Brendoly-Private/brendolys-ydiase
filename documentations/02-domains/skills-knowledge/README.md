---
document_id: "YD-DOC-DOM-SKL-001"
title: "Domaine 04 — Compétences et connaissances"
document_type: "domain-overview"
document_role: "Définit la séparation fondamentale entre taxonomie canonique des compétences et état individuel de compétence."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "domain"
---

# Domaine 04 — Compétences et connaissances

> **Rôle du document**
> Définit la séparation fondamentale entre taxonomie canonique des compétences et état individuel de compétence.
> **Usage développement :** référence obligatoire pour les conceptions, contrats et décisions relevant de son périmètre.

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
