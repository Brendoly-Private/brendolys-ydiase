---
document_id: "YD-DOC-POL-LAB-002-LABOR-INTELLIGENCE"
title: "YD-MS-LAB-002 — Labor Market Intelligence Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de labor intelligence pour YD-MS-LAB-002."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "policy"
---

# YD-MS-LAB-002 — Labor Market Intelligence Policy

> **Rôle du document**
> Établit les règles normatives de labor intelligence pour YD-MS-LAB-002.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / METHODOLOGY-VALIDATION-PENDING`
Nature : `MIXED`
Criticité : `C2`

## 1. Autorité
LAB-002 possède les indicateurs, séries, snapshots et analyses publiés qu'il calcule : LaborMarketIndicator, LaborMarketSnapshot, DemandSupplyMeasure, TensionMeasure et SectorTerritoryAnalysis.

Il ne possède ni les signaux LAB-001 ni les faits CAR/SKL/OPP.

## 2. IndicatorEdition
Chaque publication conserve indicator_ref, methodology_version, input snapshot/watermark, territory, period, produced_at, freshness, coverage state, uncertainty state, provenance summary et revision/version.

Un indicateur sans méthodologie/version n'est pas publiable.

## 3. Demande et offre
YDIASE ne déduit pas automatiquement "demande réelle" du nombre d'annonces ni "offre de travail" du nombre de profils.

Chaque DemandSupplyMeasure précise ses proxies, sources, déduplication, couverture et limites.

## 4. Tension
Une TensionMeasure n'est calculée qu'avec une méthodologie explicitant numérateur/dénominateur ou modèle, fenêtres temporelles, population/territoire, traitement des inconnues et seuils.

Les catégories comme `HIGH`, `MEDIUM`, `LOW` ne sont activées qu'après validation de seuils contextualisés.

## 5. Couverture et représentativité
Tout indicateur expose un état de couverture. Une analyse Burkina, régionale ou continentale ne peut être publiée sous ce scope que si la méthodologie définit les exigences de couverture correspondantes.

L'agrégation de quelques villes, plateformes ou partenaires ne devient pas "marché du travail du Burkina Faso" par simple sommation.

## 6. Incertitude
États minimaux : `LOW`, `MEDIUM`, `HIGH`, `NOT-ASSESSABLE`, avec facteurs explicatifs : couverture, fraîcheur, source mix, déduplication, mapping, sampling et révisions.

Une valeur numérique ne masque jamais une incertitude élevée.

## 7. Révisions
Une nouvelle donnée tardive, correction ou méthodologie crée une nouvelle édition. L'ancienne reste historisée avec son statut `SUPERSEDED` ou `CORRECTED`.

Les consommateurs doivent pouvoir distinguer valeur initiale, révisée et courante.

## 8. Comparabilité
Deux périodes/pays/secteurs ne sont comparables que si méthodes, unités, mappings et couverture sont suffisamment compatibles. Sinon le produit affiche `NOT-COMPARABLE` ou explique les limites.

## 9. Forecasting
La prévision est une responsabilité logique distincte des indicateurs observés. Toute forecast conserve horizon, model/version, training/input window, hypothèses, intervalles/incertitude et backtesting.

Forecasting reste dans LAB-002 tant qu'il ne nécessite pas dataset, équipe, SLO, lifecycle modèle ou gouvernance propres. Ces divergences déclenchent ADR d'extraction.

Une prévision n'est jamais présentée comme observation.

## 10. Consommation REC/ORI
REC/ORI reçoivent indicator/version, freshness, coverage et uncertainty. Ils ne doivent pas convertir un indicateur faible en certitude de carrière/emploi/salaire.

## 11. PII
Les produits LAB-002 sont agrégés par défaut. Toute donnée personnelle nécessite justification/finalité distincte et gouvernance CNS.

## 12. Gates
DEFINED : edition/version, demande/offre comme proxies, tension, couverture, incertitude, révision, comparabilité, frontière Forecasting.
TBD : méthodologies numériques, seuils, exigences de couverture, backtesting, SLO/RPO/RTO, restore.

Statut final : `LABOR-INTELLIGENCE-SEMANTICS-CLOSED / NUMERIC-METHODOLOGY-AND-PREPROD-PENDING`.
