---
document_id: "YD-DOC-DOM-IDP-001"
title: "Domaine 02 — Identité et profils"
document_type: "domain-overview"
document_role: "Définit la mission, l’autorité sémantique, les exclusions et la doctrine durable du domaine Identité et profils."
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

# Domaine 02 — Identité et profils

> **Rôle du document**
> Définit la mission, l’autorité sémantique, les exclusions et la doctrine durable du domaine Identité et profils.
> **Usage développement :** référence obligatoire pour les conceptions, contrats et décisions relevant de son périmètre.

Statut : `DOMAIN-BASELINE-CANDIDATE`
Owner fonctionnel : `Identity & Profile`

## Mission

Le domaine représente la personne dans YDIASE sans confondre son identité d'accès, son profil métier, ses déclarations, ses historiques, ses preuves, ses compétences, ses droits de données ou les référentiels externes.

Il doit rester sémantiquement interprétable après remplacement complet des technologies actuelles.

## Documents

1. `MODELE_DOMAINE.md`
2. `IDENTITE_DURABLE.md`
3. `PROFIL_ET_TEMPORALITE.md`
4. `PREUVES_ET_PROVENANCE.md`
5. `VISIBILITE_ET_PARTAGE.md`
6. `CYCLE_VIE_PERSONNE.md`
7. `REGLES_METIER.md`
8. `FRONTIERES_ET_DEPENDANCES.md`
9. `CAPACITES_ET_TRACABILITE.md`
10. `GATES_ET_INCONNUES.md`

## Frontière

Le domaine possède la sémantique du profil individuel et de l'historique personnel déclaré ou vérifié. Il ne possède pas :

- les credentials, sessions et mécanismes IAM
- les établissements, formations et qualifications de référence
- le référentiel des compétences
- l'état individuel de compétence calculé ou évalué
- les résultats d'évaluation
- les consentements, finalités et instructions de rétention
- les recommandations
- les opportunités ou candidatures

## Doctrine de pérennité

Les identifiants métier, états historiques, preuves, liens de provenance et règles de temporalité doivent survivre aux migrations. Un identifiant IAM, un email, un numéro de téléphone, un identifiant national ou un identifiant externe ne devient jamais à lui seul l'identité métier durable de la personne.

## Relation avec D3

Les frontières `IDN-001`, `PRF-001`, `PRF-002` et `CNS-001` sont des traductions architecturales candidates. Ce dossier peut imposer leur révision si la sémantique métier le demande.

## Gate

Le domaine devient `ACTIVE` après validation de ses règles, frontières, temporalité, preuve/provenance, cycle de vie et cohérence avec les domaines Skills, Education, Guidance, Privacy et l'architecture D3.