---
document_id: "YD-DOC-POL-OPP-001-OPPORTUNITY-LIFECYCLE"
title: "YD-MS-OPP-001 — Opportunity Lifecycle & Publication Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de opportunity lifecycle pour YD-MS-OPP-001."
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

# YD-MS-OPP-001 — Opportunity Lifecycle & Publication Policy

> **Rôle du document**
> Établit les règles normatives de opportunity lifecycle pour YD-MS-OPP-001.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / IMPLEMENTATION-PENDING`
Nature : `AUTH`
Criticité : `C1`

## 1. Autorité

OPP-001 possède la représentation YDIASE publiée des opportunités, leurs versions, exigences, validité et politiques de candidature. Une source externe conserve sa provenance et EMP-001 reste autorité sur l'employeur.

## 2. Opportunity ≠ source ≠ candidature

Une annonce reçue n'est pas automatiquement une Opportunity publiée. DAT gouverne source/provenance/qualité ; OPP décide de la représentation métier publiable.

Une Opportunity ne constitue ni promesse d'emploi, ni validation du candidat, ni candidature. APP-001 seul possède Application et ses transitions.

## 3. Types

Le modèle doit permettre plusieurs catégories (emploi, stage, alternance/apprentissage, mission, programme ou autre catégorie gouvernée) sans supposer qu'elles partagent toutes les mêmes exigences ou règles de candidature.

Chaque type possède une policy/version.

## 4. Cycle de vie

États minimaux :
`DRAFT` → `PENDING-VERIFICATION` → `PUBLISHABLE` → `PUBLISHED`.

Transitions terminales ou latérales : `SUSPENDED`, `EXPIRED`, `WITHDRAWN`, `REJECTED`, `CLOSED`, `ARCHIVED`.

Une opportunité ne devient PUBLISHED que si les gates applicables sont satisfaits.

## 5. Gates de publication

Selon type/source :
- provenance suffisante ;
- employeur/organisation et droit de publication vérifiables lorsque requis ;
- modération/anti-fraude lorsque requis ;
- territoire/configuration valide ;
- dates cohérentes ;
- exigences structurées ;
- canal/processus de candidature connu ;
- absence de restriction bloquante.

`UNKNOWN` critique ne devient jamais validation positive.

## 6. Exigences

OpportunityRequirement conserve requirement_type, required/preferred, value/ref, evidence/provenance, effective version et éventuellement niveau/seuil.

`REQUIRED` et `PREFERRED` sont distincts. Une exigence discriminatoire/interdite selon policy applicable ne doit pas être publiée comme simple critère métier.

Les références SKL/CAR/EDU utilisent versions/mappings gouvernés ; OPP ne recrée pas leurs taxonomies.

## 7. Validité et deadlines

OPP distingue publication window, application window et opportunity validity lorsque ces notions diffèrent.

Après deadline/expiration, l'opportunité peut rester consultable historiquement mais n'est plus présentée comme ouverte. APP-001 revalide synchroniquement l'acceptation des candidatures au moment de la soumission.

Aucune projection Search/REC/Matching ne peut rouvrir une Opportunity expirée.

## 8. Vérification et confiance

Les états `SOURCE-VERIFIED`, `EMPLOYER-VERIFIED`, `CONTENT-VERIFIED` ou équivalents restent séparés ; "verified" sans dimension explicite est interdit.

La vérification d'un employeur ne prouve pas automatiquement l'exactitude de chaque annonce.

## 9. Corrections et retrait

Toute modification substantielle crée OpportunityVersion. Les changements critiques (deadline, exigences, lieu, rémunération si applicable, canal) sont historisés et propagés.

Retrait/suspension produit un événement prioritaire. Les consommateurs cessent la promotion/matching courant selon SLO défini.

## 10. Duplication

Des annonces provenant de plusieurs sources peuvent représenter la même opportunité. La déduplication produit une relation/merge gouverné et préserve toutes les provenances ; elle ne détruit pas silencieusement les sources.

## 11. Commercial

Sponsoring/partenariat ne peut contourner vérification, modération, validité ou exigences de publication. Le statut commercial n'est pas une preuve de qualité.

## 12. Gates

`DEFINED` : lifecycle, publication gates, requirements, deadlines, verification dimensions, correction/retrait, déduplication, séparation APP, commercial isolation.

`TBD-PREPROD` : policies par type, règles anti-fraude/modération réelles, délais/SLO retrait, IAM/tenant, BIA/RPO/RTO, restore, contrats physiques.

Statut final : `OPPORTUNITY-SEMANTICS-CLOSED / TYPE-POLICIES-AND-PREPROD-PENDING`.
