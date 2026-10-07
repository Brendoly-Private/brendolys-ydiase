---
document_id: "YD-DOC-DOM-IDP-003"
title: "Identité durable"
document_type: "domain-concept"
document_role: "Définit l’identité métier durable, PersonRef, les correspondances externes et les règles de fusion, séparation et migration."
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

# Identité durable

> **Rôle du document**
> Définit l’identité métier durable, PersonRef, les correspondances externes et les règles de fusion, séparation et migration.
> **Usage développement :** référence obligatoire pour les conceptions, contrats et décisions relevant de son périmètre.

Statut : `DOMAIN-BASELINE-CANDIDATE`

## Principe

YDIASE distingue l'identité métier durable d'une personne des moyens utilisés pour l'authentifier ou la reconnaître à une époque donnée.

## Identifiant interne

`PersonRef` est stable, opaque, non signifiant et non réutilisable. Sa représentation technique peut migrer tant que la correspondance et la continuité sémantique restent vérifiables.

Ne doivent pas servir d'identifiant métier primaire durable :

- email
- téléphone
- nom/prénom
- username
- numéro étudiant
- identifiant employeur
- identifiant d'un fournisseur IAM
- identifiant national
- identifiant d'un réseau social

Ces valeurs peuvent devenir des attributs ou correspondances gouvernées lorsque leur usage est légitime.

## Résolution et correspondances

Les liens entre `PersonRef` et identifiants externes doivent être typés, sourcés, datés, révocables et limités à une finalité. Une correspondance peut être contestée, remplacée ou expirer sans changer automatiquement l'identité métier.

## Fusion et séparation

Deux représentations peuvent être reconnues comme la même personne. Une fusion doit rester traçable et réversible tant que le niveau de preuve ne permet pas une consolidation irréversible.

Une fusion erronée doit pouvoir être séparée sans attribuer les historiques d'une personne à une autre.

## Cas de cycle de vie

Le modèle doit supporter sans changer de sémantique : changement de nom, changement de coordonnées, changement de pays, perte ou remplacement du compte d'accès, comptes multiples autorisés, absence temporaire de compte, retour après longue période, décès lorsque le traitement le requiert, suppression/anonymisation selon droits applicables.

## Mineurs et évolution de statut

Le statut d'un individu peut changer avec l'âge et le cadre national. Les règles de représentation, autorisation ou responsabilité ne doivent pas être codées comme une propriété universelle fixe. Elles sont évaluées selon le Country Framework, la date pertinente et les politiques applicables.

## Migration séculaire

Toute migration majeure doit pouvoir exporter au minimum : identifiant durable, version sémantique, liens externes nécessaires, historique autorisé des changements d'identité et métadonnées permettant de comprendre les correspondances. Les secrets IAM ne font pas partie de cette identité métier exportable.