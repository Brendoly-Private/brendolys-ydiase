---
document_id: "YD-DOC-FND-GOV-REG-007"
title: "Registre des sources — BRENDOLYS YDIASE"
document_type: "source-registry"
document_role: "Enregistre les familles de sources connues et les conditions nécessaires à leur qualification."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
owners:
  - "Documentation Governance"
depends_on:
  - "YD-DOC-FND-GOV-001"
  - "YD-STD-DOC-META-001"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "foundation"
  - "governance-register"
---

# Registre des sources — BRENDOLYS YDIASE

> **Rôle du document**
> Enregistre les familles de sources connues et les conditions nécessaires à leur qualification.
> **Usage développement :** référence obligatoire pour son périmètre.

Statut : `ACTIVE-BASELINE`

Ce registre décrit les familles de sources connues. Une organisation réelle reçoit ensuite son propre `YD-SRC-*` après qualification. Une famille n'est jamais une preuve de droit d'usage.

| ID | Famille de source | Territoire initial | Domaine | Méthode possible | Droits | Qualité initiale | Actualisation | Statut |
|---|---|---|---|---|---|---|---|---|
| YD-SRC-FAM-EDU-001 | Établissements d'enseignement et centres de formation | Burkina Faso | Education | contribution, publication officielle, collecte vérifiée | à qualifier par source | variable | selon cycle établissement | CANDIDATE |
| YD-SRC-FAM-EDU-002 | Représentants/bureaux étudiants et réseau terrain autorisé | Burkina Faso | Education | collecte terrain avec preuve | à encadrer | variable, corroboration requise | campagne/cycle académique | CANDIDATE |
| YD-SRC-FAM-REG-001 | Autorités/référentiels publics éducation, emploi, qualifications | Burkina Faso | Multi-domaines | publication officielle/import | à qualifier | élevée si authenticité confirmée | selon producteur | CANDIDATE |
| YD-SRC-FAM-OPP-001 | Employeurs/recruteurs publiant opportunités | Burkina Faso | Opportunités | contribution/API/import | à qualifier | variable | événementielle | CANDIDATE |
| YD-SRC-FAM-LAB-001 | Plateformes et canaux publics d'offres | Burkina Faso | Labor Market | collecte autorisée/import | à qualifier | signal partiel | fréquente | CANDIDATE |
| YD-SRC-FAM-LAB-002 | Enquêtes, études et statistiques sur emploi/compétences | Burkina Faso | Labor Market | publication/import | à qualifier | dépend méthodologie | périodique | CANDIDATE |
| YD-SRC-FAM-LAB-003 | Signaux économiques et sectoriels | Burkina Faso | Labor Intelligence | sources statistiques/économiques | à qualifier | dépend source | périodique | CANDIDATE |
| YD-SRC-FAM-USR-001 | Données déclarées par l'utilisateur | Burkina Faso | Profiles/Skills/Career | saisie/consentement | finalité requise | déclarative | à l'action utilisateur | CANDIDATE |
| YD-SRC-FAM-PAR-001 | Partenaires institutionnels/écosystème | Burkina Faso | Partenaires/Data | contrat/import/API | contrat requis | à évaluer | contractuelle | CANDIDATE |
| YD-SRC-FAM-YDI-001 | Événements produits par YDIASE | Global selon déploiement | Analytics/Product | événements internes gouvernés | finalité interne définie | contrôlable | continue | CANDIDATE |

## Qualification d'une source réelle

Avant `ACTIVE`, une source doit documenter au minimum : producteur réel, territoire, données fournies, méthode de collecte, provenance, base contractuelle ou droit d'usage, restrictions, fréquence, mécanisme de correction, qualité, responsable et date de revue.

## Interdictions

- une source `CANDIDATE` ne devient pas autoritative par son inscription
- une source publique n'est pas automatiquement librement réutilisable
- une collecte terrain ne remplace pas la provenance
- plusieurs sources concordantes ne suppriment pas leurs identités respectives
- une source d'offres n'est pas automatiquement une source du marché du travail réel
