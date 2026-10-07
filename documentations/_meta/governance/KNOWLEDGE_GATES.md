---
document_id: "YD-DOC-META-KNOWLEDGE-GATES"
title: "YDIASE Knowledge Gates — K0 à K6"
document_type: "governance-reference"
document_role: "Documente une référence de gouvernance ou de maturité utilisée pour qualifier le corpus et les composants YDIASE."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "meta"
---

# YDIASE Knowledge Gates — K0 à K6

> **Rôle du document**
> Documente une référence de gouvernance ou de maturité utilisée pour qualifier le corpus et les composants YDIASE.
> **Usage développement :** référence de support pour la gouvernance et la qualification documentaire.

## Objet

Les Knowledge Gates empêchent une entité YDIASE d'afficher une maturité supérieure aux connaissances réellement disponibles et vérifiables.

Le niveau K ne remplace ni `architectureStatus`, ni `implementationStatus`, ni `deploymentStatus`. Ces axes restent indépendants.

## K0 — Identifié

Minimum : ID stable, type, nom et responsabilité ou finalité.

Usage : inventaire initial, capacité future, composant candidat.

## K1 — Cadré

K0 + autorité ou propriétaire, domaine ou périmètre, frontières et sources documentaires.

Usage : objet suffisamment défini pour entrer dans la gouvernance YDIASE.

## K2 — Relié

K1 + relations logiques, dépendances, amont/aval, ownership autoritatif et traçabilité d'impact.

Usage : analyse d'impact et raisonnement humain/IA sur le graphe.

## K3 — Contractualisé

K2 + contrats API/événements applicables, contrats de données, invariants, exigences, ADR structurants, versionnement et compatibilité.

Usage : préparation fiable à l'implémentation sans dépendre de connaissances tacites.

## K4 — Gouverné

K3 + classification des données, contrôles de sécurité, confidentialité/rétention applicables, criticité/SLO, observabilité, sauvegarde/reprise si stateful, procédure d'exploitation et responsables nommés.

Usage : préparation exploitation, sécurité et conformité.

## K5 — Vérifié

K4 + validations automatiques, tests de contrats, vérifications sécurité, tests de résilience/restauration applicables, preuves reliées et aucun gap critique non traité.

Usage : connaissance techniquement vérifiable avant ou pendant l'activation.

## K6 — Opérationnel et maintenu

K5 + lien vers implémentation, lien vers déploiement, observabilité runtime si déployé, analyse d'impact des changements, cadence de revue, retrait contrôlé et détection de dérive.

Usage : maintenir la connaissance synchronisée avec le système réel sur la durée.

## Règles de preuve

Chaque critère doit produire l'un des états suivants :

- `PASS` : preuve présente et valide
- `FAIL` : preuve obligatoire absente ou invalide
- `N/A` : non applicable avec justification explicite
- `UNKNOWN` : information insuffisante, bloque le niveau concerné

Une simple phrase déclarative ne constitue pas automatiquement une preuve. Une preuve peut être un contrat versionné, un test automatisé, un ADR approuvé, une configuration contrôlée, un rapport CI, une procédure testée, une référence de code ou une observation runtime selon le critère.

## Calcul

Le Knowledge Gate calcule le niveau maximal continu. Une entité qui satisfait K0, K1 et K2 mais échoue K3 reste K2, même si elle possède certains éléments de K4 ou K5.

Le niveau déclaré ne peut pas dépasser le niveau calculé.

## Cinquième axe recommandé : Evidence Confidence

En complément des quatre axes `Knowledge`, `Architecture`, `Implementation` et `Deployment`, YDIASE doit suivre la confiance des preuves.

Niveaux proposés :

- `E0 UNVERIFIED` : déclaration sans preuve contrôlée
- `E1 SOURCED` : reliée à une source identifiable
- `E2 CORROBORATED` : plusieurs éléments cohérents ou source autoritative
- `E3 TESTED` : vérifiée par test ou contrôle reproductible
- `E4 OBSERVED` : confirmée par observation runtime ou opérationnelle récente

La confiance est attachée aux assertions et preuves, pas uniquement au microservice entier. Une même entité peut donc contenir des faits E1 et E4.

Cette séparation empêche une documentation très complète mais non vérifiée d'être interprétée comme une vérité opérationnelle.
