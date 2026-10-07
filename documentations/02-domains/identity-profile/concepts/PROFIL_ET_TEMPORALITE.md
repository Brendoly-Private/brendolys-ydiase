---
document_id: "YD-DOC-DOM-IDP-005"
title: "Profil et temporalité"
document_type: "domain-concept"
document_role: "Définit la temporalité du profil, des historiques, corrections, objectifs et préférences sans créer de précision artificielle."
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

# Profil et temporalité

> **Rôle du document**
> Définit la temporalité du profil, des historiques, corrections, objectifs et préférences sans créer de précision artificielle.
> **Usage développement :** référence obligatoire pour les conceptions, contrats et décisions relevant de son périmètre.

Statut : `DOMAIN-BASELINE-CANDIDATE`

## Principe

Le profil d'une personne change. YDIASE ne doit jamais interpréter le profil courant comme une vérité historique permanente.

## Dimensions temporelles

Selon la donnée, le modèle conserve :

- `valid_from` / `valid_to` : période pendant laquelle l'information est considérée valable dans le métier
- `observed_at` : moment où elle a été observée ou déclarée
- `recorded_at` : moment où YDIASE l'a enregistrée
- `version` : version de la représentation ou de l'agrégat
- précision temporelle : date exacte, période, année ou inconnue

Aucune précision artificielle ne doit être créée.

## Profil courant

Le profil courant constitue une vue gouvernée des informations actuellement pertinentes. Il peut être reconstruit à partir des sources autoritatives et de l'historique lorsque le modèle retenu le permet.

## Historique éducatif et professionnel

Un enregistrement individuel référence l'institution, la formation, la qualification, le métier ou l'organisation connus dans leurs domaines respectifs. Si le référentiel externe évolue, l'historique personnel conserve le contexte nécessaire pour interpréter l'enregistrement tel qu'il était au moment concerné.

## Corrections

Une correction distingue :

- correction d'une erreur de saisie
- nouvelle information remplaçant une ancienne
- contestation non résolue
- invalidation d'une assertion
- changement réel de situation

Ces cas ne doivent pas produire le même effet historique.

## Objectifs et préférences

Un objectif ou une préférence peut être actif, remplacé, abandonné, atteint, expiré ou contesté. Les moteurs de recommandation ne doivent pas traiter un ancien objectif comme actuel sans règle explicite.

## Longue durée

Une future plateforme doit pouvoir interpréter les états anciens même si les schémas physiques ont changé. Les migrations conservent donc les versions sémantiques ou les règles de transformation nécessaires.