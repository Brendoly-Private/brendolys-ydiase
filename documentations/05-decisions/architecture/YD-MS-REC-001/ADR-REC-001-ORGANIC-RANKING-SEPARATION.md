---
document_id: "YD-DOC-ADR-ADR-REC-001-ORGANIC-RANKING-SEPARATION"
title: "ADR-REC-001 — Séparation du ranking organique et des influences externes"
document_type: "architecture-decision-record"
document_role: "Consigne une décision d’architecture et ses conséquences applicables."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "decisions"
---

# ADR-REC-001 — Séparation du ranking organique et des influences externes

> **Rôle du document**
> Consigne une décision d’architecture et ses conséquences applicables.
> **Usage développement :** référence obligatoire pour les choix d’architecture concernés.

Statut : `ACCEPTED-DOCUMENTARY-BASELINE`

## Contexte

REC-001 produit des recommandations susceptibles d'utiliser plusieurs sources et, à terme, des modèles. Le produit possède aussi des fonctions commerciales distinctes. Une confusion entre pertinence organique et intérêt commercial détruirait la traçabilité du moteur.

## Décision

REC-001 reste autoritatif uniquement sur ses runs, résultats, explications et snapshots. Le pipeline logique sépare `ELIGIBILITY`, `ORGANIC-SCORING`, `ORGANIC-RANKING` et `PRESENTATION`.

Aucun paiement, budget publicitaire, commission, statut partenaire ou probabilité de conversion commerciale ne peut influencer eligibility, score organique, rang organique, pondérations, exclusions ou explications organiques.

SPN-001 produit ses placements dans un canal/objet distinct. Une insertion visuelle sponsorisée ne change jamais `organic_rank`.

Les données sources restent sous l'autorité de leurs domaines. REC conserve leurs références/version dans son evidence snapshot sans devenir leur propriétaire.

## Conséquences

- les politiques et modèles REC sont versionnés ;
- les runs historiques restent auditables ;
- une correction de source produit un nouveau calcul ou une invalidation ;
- l'abstention est un résultat légitime ;
- l'incertitude reste distincte du score ;
- toute future architecture de sponsoring doit préserver cette frontière ;
- toute modification de cette séparation exige un nouvel ADR et une revue de gouvernance.

## Alternatives rejetées

### Intégrer le sponsoring dans le score

Rejeté car cela confond pertinence et intérêt commercial.

### Réécrire un ancien run après correction

Rejeté car cela détruit la reproductibilité historique.

### Utiliser un LLM comme autorité de justification

Rejeté. Un LLM peut reformuler une explication structurée, jamais inventer la raison d'un rang.
