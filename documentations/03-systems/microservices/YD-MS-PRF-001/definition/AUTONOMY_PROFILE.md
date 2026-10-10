---
document_id: "YD-DOC-MS-PRF-001-AUT"
title: "YD-MS-PRF-001 — Profile"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-PRF-001."
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

# YD-MS-PRF-001 — Profile

> **Rôle du document**
> Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-PRF-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Logique : PRF-001 uniquement. PRF-002 possède désormais une frontière physique autonome selon `ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md`.
- Données possédées : Profile Core, préférences, objectifs, contraintes déclarées et vues sémantiques du profil courant. Le service ne possède pas EducationRecord, ExperienceRecord, AchievementClaim ni ProfileEvidenceLink.
- Autorité : source autoritative du profil courant individuel dans YDIASE. Les historiques éducatifs et professionnels relèvent de `YD-MS-PRF-002`.
- Datastore : privé au service, migrations privées, aucune lecture DB externe et aucun datastore partagé avec PRF-002.
- Backup/restore : obligatoire, chiffré, restauration indépendante et testée. Criticité C1 confirmée. RPO/RTO/SLO restent `TBD-PREPROD`.
- IAM audience : `ydiase-profile`.
- IAM realms : `brendolys-customers` principal, `brendolys-internal` pour support/conformité autorisés, `brendolys-networks` refusé par défaut, M2M par workload identity dédiée.
- Scopes : `profile:read:self`, `profile:write:self`, `profile:goals:read:self`, `profile:goals:write:self`, `profile:read:support`, `profile:projection:read`. Les scopes education/experience appartiennent à PRF-002 et sont interdits ici.
- Claims minimaux : `sub`, `iss`, `aud`, claims temporels standard et scopes. `org_id`/tenant uniquement si nécessaire. Aucune donnée de profil dans le token.
- Autorisation : les scopes `:self` exigent correspondance avec `sub`. Accès support contrôlé et audité. Décision CNS obligatoire fail-closed si non vérifiable. Un scope client universel `profile:*` est interdit.
- API/événements : API du profil courant et projections minimales du profil. Consomme IdentityRef, Consent/Privacy, CountryConfig et, uniquement si nécessaire, des projections minimales de PRF-002 et référentiels autorisés.
- Réseau : aucun accès direct aux DB tierces ou PRF-002. Flux sortants limités aux contrats D3. DNS interne requis. Exposition utilisateur uniquement via edge/API management.
- Sécurité : minimisation forte, chiffrement, audit des accès sensibles, interdiction d'export du dossier complet sans finalité et interdiction de reconstruire localement l'historique PRF-002 par réplication de commodité.
- Résilience : lecture de dernière version locale autorisée selon fraîcheur. Une indisponibilité PRF-002 ne doit pas bloquer les opérations de profil courant qui n'en dépendent pas. Traitement personnel non autorisé fail-closed sur décision privacy requise.
- Scaling : unité `subject`. Séparation lecture/écriture possible sans changer l'ownership.
- Repo candidat : `brendolys-ydiase-profile`. CI/CD, artefact, secrets, certificats et workload identity propres.
- Runbook/DR : perte DB, corruption, suppression accidentelle, révocation privacy, restauration puis réconciliation des projections.
- Gate Contract Registry : `CLOSED` pour PRF-IAM.
- Gates préproduction : RPO/RTO/SLO, rétention, clients OIDC physiques, step-up si requis, tests restore et contrats minimaux PRF-001 ↔ PRF-002.