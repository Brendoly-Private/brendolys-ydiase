---
document_id: "YD-DOC-POL-LAB-001-LABOR-SIGNAL"
title: "YD-MS-LAB-001 — Labor Signal Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de labor signal pour YD-MS-LAB-001."
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

# YD-MS-LAB-001 — Labor Signal Policy

> **Rôle du document**
> Établit les règles normatives de labor signal pour YD-MS-LAB-001.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / IMPLEMENTATION-PENDING`
Nature : `AUTH`
Criticité : `C2`

## 1. Autorité
LAB-001 possède les signaux marché normalisés YDIASE : LaborSignal, ObservedDemandSignal, DeclaredNeedSignal, InstitutionalSignal, EconomicSignal et SignalObservation.

DAT conserve raw/provenance/validation ; CAR/SKL possèdent métiers/compétences ; EMP/OPP possèdent leurs objets métier. LAB ne transforme pas une observation externe en vérité universelle.

## 2. Observation ≠ signal ≠ indicateur
Une `SignalObservation` représente une observation sourcée. Un `LaborSignal` est sa représentation normalisée publiée selon une policy LAB. Un indicateur agrégé appartient à LAB-002.

Une offre d'emploi, une déclaration d'employeur, une statistique institutionnelle et une observation économique restent des types distincts.

## 3. Champs minimaux
Tout signal publié conserve : signal_type, subject refs (occupation/skill/sector lorsque pertinents), territory scope, observed_at/period, source/provenance ref, validation ref, normalization_policy_version, freshness/expiry, coverage metadata, confidence/quality state et publication version.

## 4. Couverture
La couverture décrit ce que les données permettent réellement d'observer : territoire, période, secteurs/populations/canaux couverts et limites connues.

Une forte quantité d'observations provenant d'un seul canal ne prouve pas une représentativité nationale.

`UNKNOWN`, `PARTIAL`, `KNOWN-LIMITED` et `SUFFICIENT-FOR-DEFINED-USE` sont distingués.

## 5. Fraîcheur
Chaque classe de signal possède une politique de fraîcheur/expiration versionnée. Un signal expiré reste historique mais n'est pas présenté comme signal actuel.

Aucune durée universelle n'est inventée ici.

## 6. Normalisation
Les unités, périodes, territoires et références CAR/SKL sont normalisés seulement avec mappings/version compatibles. Une conversion incertaine conserve son incertitude ; aucun mapping approximatif n'est présenté comme identité.

## 7. Confiance
La confiance/qualité dépend séparément de provenance, validation DAT-004, fraîcheur, couverture, cohérence et nature du signal. Elle n'est pas synonyme de volume.

## 8. Corrections
Correction source ou validation DAT produit correction/invalidation/version liée. L'ancien signal n'est jamais réécrit silencieusement. Les consommateurs reçoivent un changement versionné.

## 9. Promotion
Aucun signal n'est publié si provenance obligatoire ou validation minimale requise manque. `NOT-ASSESSABLE` ne devient jamais PASS.

## 10. Gates
DEFINED : typologie, observation/signal/indicator, couverture, fraîcheur, normalisation, confiance, corrections.
TBD : seuils qualité/fraîcheur par classe, sources réelles, SLO/RPO/RTO, restore et contrats physiques.

Statut final : `LABOR-SIGNAL-SEMANTICS-CLOSED / THRESHOLDS-AND-PREPROD-PENDING`.
