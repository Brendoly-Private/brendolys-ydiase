---
document_id: "YD-DOC-DOM-IDP-009"
title: "Preuves et provenance du profil"
document_type: "evidence-provenance-policy"
document_role: "Définit la sémantique des déclarations, preuves, vérifications, contradictions et provenance associées au profil."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "normative"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "domain"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# Preuves et provenance du profil

> **Rôle du document**
> Définit la sémantique des déclarations, preuves, vérifications, contradictions et provenance associées au profil.
> **Usage développement :** référence obligatoire pour les conceptions, contrats et décisions relevant de son périmètre.

Statut : `DOMAIN-BASELINE-CANDIDATE`

## Principe

YDIASE sépare ce qu'une personne déclare, ce qu'un tiers affirme, ce qu'une source fournit et ce que YDIASE a vérifié selon une méthode documentée.

## États d'une assertion

Une assertion de profil peut notamment être : `DECLARED`, `SOURCE-SUPPORTED`, `VERIFIED`, `DISPUTED`, `INVALIDATED`, `EXPIRED` ou `UNKNOWN`.

Ces états décrivent le statut de l'assertion. Ils ne constituent pas une note globale de la personne.

## ProfileEvidenceLink

Le lien de preuve relie une assertion à :

- source ou émetteur
- type de preuve
- date ou période
- méthode de vérification lorsqu'elle existe
- version ou empreinte logique du document lorsque nécessaire
- droits d'usage et restrictions
- statut de validité
- provenance technique/métier requise

Le domaine 02 possède le lien entre profil et preuve. Le registre/source ou document sous-jacent peut appartenir à un autre domaine.

## Non-transitivité

Une preuve valide d'un diplôme ne prouve pas automatiquement une compétence. Une expérience déclarée ne prouve pas automatiquement un métier maîtrisé. Une institution reconnue ne rend pas automatiquement chaque assertion issue d'elle vraie.

## Contradictions

Des assertions contradictoires peuvent coexister jusqu'à arbitrage. YDIASE conserve leur provenance et ne remplace pas silencieusement l'une par l'autre.

## Pérennité

Une preuve externe peut disparaître dans le futur. Lorsque les droits le permettent et que l'usage le requiert, YDIASE conserve les métadonnées minimales permettant d'expliquer pourquoi une assertion avait obtenu un statut donné, sans conserver inutilement le document complet.