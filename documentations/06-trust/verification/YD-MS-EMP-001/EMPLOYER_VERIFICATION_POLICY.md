---
document_id: "YD-DOC-TRU-EMP-001-EMPLOYER-VERIFICATION-POLICY"
title: "YD-MS-EMP-001 — Employer Identity & Verification Policy"
document_type: "verification-specification"
document_role: "Définit un protocole ou une spécification de vérification servant de preuve contrôlée."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "evidence"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "trust"
---

# YD-MS-EMP-001 — Employer Identity & Verification Policy

> **Rôle du document**
> Définit un protocole ou une spécification de vérification servant de preuve contrôlée.
> **Usage développement :** référence de vérification obligatoire pour le périmètre concerné.

Statut : `NORMATIVE-BASELINE / COUNTRY-EVIDENCE-PENDING`
Nature : `AUTH`
Criticité : `C2`

## 1. Autorité
EMP-001 possède Employer, EmployerPresence, EmployerVerification et EmployerProfile. PRT conserve les accords partenaires ; IDN les identités/comptes ; OPP les opportunités ; EMP-002 le recrutement.

## 2. Employer ≠ compte utilisateur
Un compte individuel ne devient jamais employeur par simple déclaration. L'organisation, ses présences et les personnes habilitées sont des concepts distincts.

## 3. Vérification multidimensionnelle
Une vérification doit indiquer sa dimension : existence/identité organisationnelle, représentation, présence/territoire, coordonnées ou autre dimension gouvernée.

Un état générique "VERIFIED" sans dimension/preuve/version n'est pas suffisant.

États minimaux par dimension : `UNVERIFIED`, `PENDING`, `VERIFIED`, `LIMITED`, `SUSPENDED`, `REVOKED`, `EXPIRED`, `NOT-ASSESSABLE`.

## 4. Preuve de représentation
Toute action organisationnelle sensible requiert un principal autorisé relié à l'Employer et un scope. La preuve/mandat possède effective dates et peut être révoqué.

La vérification de l'organisation ne donne pas automatiquement à tous ses utilisateurs le droit de publier ou recruter.

## 5. Tenant isolation
Tout accès organisationnel porte employer_ref/tenant context. Un utilisateur de l'employeur A ne peut lire/modifier l'employeur B par simple changement d'identifiant.

Les tests horizontaux/IDOR sont release-blocking.

## 6. Sources et corrections
Les preuves gardent provenance/version. Correction ou révocation produit un nouvel état ; aucune preuve historique n'est réécrite silencieusement.

## 7. Propagation
`employer.changed` transporte employer_ref, verification/status, version et effective_at minimaux. OPP/EMP-002 réévaluent les opérations sensibles après suspension/révocation.

## 8. Country
Les preuves légales/administratives requises varient par pays via CFG/policies validées. Aucun modèle Burkina n'est supposé universel.

Statut final : `EMPLOYER-SEMANTICS-CLOSED / COUNTRY-RULES-AND-PREPROD-PENDING`.
