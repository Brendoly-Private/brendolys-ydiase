---
document_id: "YD-DOC-DOM-IDP-007"
title: "Frontières et dépendances — Identité et profils"
document_type: "domain-boundaries-dependencies"
document_role: "Définit les frontières métier et physiques du domaine Identité et profils ainsi que ses dépendances autorisées et interdites."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "domain"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# Frontières et dépendances — Identité et profils

> **Rôle du document**
> Définit les frontières métier et physiques du domaine Identité et profils ainsi que ses dépendances autorisées et interdites.
> **Usage développement :** référence obligatoire pour les conceptions, contrats et décisions relevant de son périmètre.

Statut : `DOMAIN-REVIEW-CANDIDATE`

## Frontières métier confirmées

### Identité technique et accès

Responsabilité : comptes, principal technique, credentials bindings, sessions et état d'accès.
Traduction D3 : `IDN-001` via BRENDOLYS Identity.
Décision : `CONFIRM-SEPARATION`.

### Profil courant

Responsabilité : `UserProfile`, préférences, objectifs, contraintes déclarées et vues sémantiques du profil.
Traduction D3 : `PRF-001` → `YD-MS-PRF-001`.
Décision : `KEEP-SEPARATE-PHYSICAL`.

### Historique éducatif et expérience

Responsabilité : `EducationRecord`, `ExperienceRecord`, `AchievementClaim`, `ProfileEvidenceLink`.
Traduction D3 : `PRF-002` → `YD-MS-PRF-002`.
Décision : `KEEP-SEPARATE-PHYSICAL`.

La séparation physique est retenue par `ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md`. Les raisons principales sont la temporalité longue, la provenance, les preuves, les permissions minimales, la rétention et la réduction du rayon d'impact.

### Consentement et privacy

Responsabilité : finalités, consentements, restrictions, demandes des personnes et instructions de rétention.
Traduction D3 : `CNS-001`.
Décision : `CONFIRM-SEPARATION`.

## Dépendances autorisées

| Producteur | Consommateur domaine 02 | Donnée minimale | Autorité |
|---|---|---|---|
| IDN | PRF-001 / PRF-002 | `IdentityRef`, état de compte strictement nécessaire | IDN |
| PRF-001 | PRF-002 | `ProfileRef` et attributs minimaux requis | PRF-001 |
| Privacy/CNS | PRF-001 / PRF-002 | droits, finalités et restrictions applicables | CNS |
| Country Framework | PRF-001 / PRF-002 | règles pays pertinentes | Country/CFG |
| Education | PRF-002 | références institution/formation/qualification | Education |
| Skills | PRF-002 | références de taxonomie lorsque nécessaires | Skills |
| Data Provenance | PRF-002 | références de source/provenance | Data |

## Dépendances interdites

- PRF-001 et PRF-002 ne partagent aucune base de données
- PRF-001 ne modifie pas les agrégats historiques de PRF-002
- PRF-002 ne modifie pas le profil courant PRF-001
- Profile ne crée pas un compte IAM
- PRF-002 ne crée pas une institution, formation, qualification ou compétence de référence
- Recommendation ne transforme pas directement une inférence en fait de profil
- un consommateur ne réplique pas le dossier complet par commodité
- une projection analytique ne devient pas owner du profil

## Cohérence

L'incohérence D3 antérieure est close. `DDD_REVIEW.md` et `SENSITIVE_MERGER_REVIEW.md` doivent considérer la séparation physique comme la décision canonique. Toute future proposition de fusion exige un nouvel ADR.

## Effet sur la cible

La cible contient désormais deux microservices métier pour ces responsabilités. Le comptage physique D3 doit passer de 47 à 48 microservices métier et de 51 à 52 frontières autonomes avec les quatre composants plateforme.