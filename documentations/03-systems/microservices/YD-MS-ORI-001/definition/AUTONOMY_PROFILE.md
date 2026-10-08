---
document_id: "YD-DOC-MS-ORI-001-AUT"
title: "YD-MS-ORI-001 — Orientation & Decision Support"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-ORI-001."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-ORI-001 — Orientation & Decision Support

> **Rôle du document**
> Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-ORI-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Logique : ORI-001 + ORI-002. Autorité sur dossiers, objectifs/contraintes de décision, comparaisons et choix enregistrés.
- C1, backup AUTH. C/I/M2M.
- Dépendances : PRF, ASM, REC, CNS; Recommendation via job/contrat sans boucle synchrone circulaire.
- Panne : dossier consultable; nouvelle recommandation en attente; dernier résultat uniquement s’il est daté et présenté comme tel.
- Sécurité : profilage, explications, finalités et accès objet audités. Decision Support ne crée pas une vérité concurrente du ranking REC.
- Repo : `brendolys-ydiase-orientation-decision`.
- Gate : SLO/RPO/RTO, durée de conservation dossiers, règles mineurs, workflow REC, restore et contrats.