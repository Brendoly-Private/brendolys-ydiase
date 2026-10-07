---
document_id: "YD-DOC-DOM-IDP-002"
title: "Cycle de vie de la personne dans YDIASE"
document_type: "domain-concept"
document_role: "Définit la sémantique du cycle de vie métier d’une personne indépendamment du cycle de vie de son compte technique."
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

# Cycle de vie de la personne dans YDIASE

> **Rôle du document**
> Définit la sémantique du cycle de vie métier d’une personne indépendamment du cycle de vie de son compte technique.
> **Usage développement :** référence obligatoire pour les conceptions, contrats et décisions relevant de son périmètre.

Statut : `DOMAIN-BASELINE-CANDIDATE`

## Principe

Le cycle de vie métier d'une personne est distinct du cycle de vie de son compte technique.

## États et événements possibles

Le modèle doit supporter notamment : création de représentation, activation d'un accès, changement de statut, correction, rattachement ou retrait d'un identifiant externe, suspension d'accès, fermeture de compte, retour ultérieur, exercice de droits, anonymisation/pseudonymisation lorsque applicable et fin de conservation.

La liste technique d'événements sera définie plus tard dans les contrats. Ce document fixe uniquement la sémantique.

## Fermeture de compte

La fermeture d'un compte IAM ne signifie pas automatiquement suppression immédiate de tous les enregistrements métier. Chaque catégorie suit ses finalités, obligations et règles de rétention.

Inversement, l'existence d'un historique métier ne permet pas de conserver indéfiniment des données personnelles sans fondement.

## Réactivation

Une personne qui revient après plusieurs années peut retrouver une continuité métier uniquement lorsque les règles de conservation et d'identification le permettent. Le système ne doit pas recréer arbitrairement un nouveau passé ni fusionner des personnes sur une correspondance faible.

## Mineurs

Le passage d'un régime applicable aux mineurs vers celui d'un adulte doit être traité comme une transition gouvernée, pas comme une migration manuelle exceptionnelle. Les règles exactes dépendent du Country Framework et de la conformité.

## Décès et situations futures

Le domaine doit pouvoir recevoir des politiques futures concernant décès, incapacité, représentation légale ou succession numérique sans intégrer aujourd'hui des règles juridiques universelles non validées.

## Fin de conservation

À expiration, la suppression, anonymisation, agrégation ou conservation probatoire dépend de la catégorie, de la finalité et du droit applicable. Les projections et copies dérivées doivent recevoir l'instruction correspondante selon leurs contrats.