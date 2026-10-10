---
document_id: "YD-DOC-DOM-IDP-004"
title: "Modèle du domaine Identité et profils"
document_type: "domain-model"
document_role: "Définit les concepts, distinctions, relations et invariants du modèle métier Identité et profils."
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

# Modèle du domaine Identité et profils

> **Rôle du document**
> Définit les concepts, distinctions, relations et invariants du modèle métier Identité et profils.
> **Usage développement :** référence obligatoire pour les conceptions, contrats et décisions relevant de son périmètre.

Statut : `DOMAIN-BASELINE-CANDIDATE`

## Concepts durables

| Concept | Sens métier | Autorité sémantique |
|---|---|---|
| Person | personne représentée dans YDIASE indépendamment de son compte d'accès | domaine 02 |
| PersonRef | référence stable et opaque permettant aux autres domaines de viser une personne sans copier son profil | domaine 02 |
| UserProfile | état courant publiable/consommable du profil selon finalité et droits | domaine 02 |
| Preference | préférence déclarée liée à l'expérience ou aux choix de la personne | domaine 02 |
| Goal | objectif déclaré, daté et révisable | domaine 02 |
| DeclaredConstraint | contrainte déclarée avec contexte et période de validité | domaine 02 |
| EducationRecord | fait ou déclaration concernant l'histoire éducative d'une personne | domaine 02, références EDU externes |
| ExperienceRecord | fait ou déclaration concernant une expérience professionnelle ou assimilée | domaine 02 |
| AchievementClaim | assertion d'accomplissement distincte d'une preuve et d'une compétence autoritative | domaine 02 |
| ProfileEvidenceLink | lien entre une assertion de profil et une preuve/provenance | domaine 02 |

## Distinctions obligatoires

- `Person` ≠ compte IAM
- `Person` ≠ `UserProfile`
- profil courant ≠ historique complet
- déclaration ≠ fait vérifié
- preuve ≠ vérité métier absolue
- expérience ≠ métier de référence
- historique éducatif individuel ≠ catalogue Education
- achievement ≠ compétence acquise
- préférence produit ≠ consentement Privacy
- visibilité du profil ≠ autorisation de traitement

## Relations

Une `Person` peut posséder zéro ou plusieurs identités d'accès au cours du temps, selon les politiques applicables. Elle possède un profil courant versionné et peut posséder des historiques éducatifs, professionnels et autres assertions autorisées.

Les enregistrements personnels référencent les objets des autres domaines par identifiants stables et version/context lorsque nécessaire. Ils ne dupliquent pas leur autorité métier.

## Invariants

1. la suppression ou le remplacement d'un compte IAM ne doit pas changer silencieusement la signification de `Person`
2. un identifiant externe ne remplace jamais `PersonRef`
3. toute assertion vérifiée conserve le type de vérification et sa provenance
4. une correction historique ne réécrit pas silencieusement le passé
5. toute donnée temporelle indique le niveau de précision réellement connu
6. une donnée inconnue reste inconnue et n'est pas inventée pour compléter le profil
7. les autres domaines consomment le minimum requis selon la finalité

## Hors domaine

Credentials et sessions : IAM/IDN.
Consentements et finalités : Privacy/CNS.
Compétences individuelles : Skills.
Évaluations : Assessment.
Référentiels Education : Education.
Recommandations : Guidance/Recommendation.