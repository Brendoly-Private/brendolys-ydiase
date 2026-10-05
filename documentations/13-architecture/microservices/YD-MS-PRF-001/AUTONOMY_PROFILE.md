# YD-MS-PRF-001 — Profile

Statut : `autonomy-profile-draft`

- Logique : PRF-001 + PRF-002. Gate fusion PRF-002 avant production Burkina.
- Données possédées : Profile Core, préférences/objectifs, EducationRecord, ExperienceRecord. Données personnelles; sous-modèles, permissions, rétention et audit séparés.
- Datastore : privé au service; migrations privées; aucune lecture DB externe.
- Backup/restore : obligatoire, chiffré, restauration indépendante et testée. Criticité C1 confirmée; RPO/RTO/SLO restent TBD-PREPROD.
- IAM audience : `ydiase-profile`.
- IAM realms : `brendolys-customers` principal; `brendolys-internal` pour support/conformité autorisés; `brendolys-networks` refusé par défaut; M2M par workload identity dédiée.
- Scopes : `profile:read:self`, `profile:write:self`, `profile:education:read:self`, `profile:education:write:self`, `profile:experience:read:self`, `profile:experience:write:self`, `profile:goals:read:self`, `profile:goals:write:self`, `profile:read:support`, `profile:projection:read`.
- Claims minimaux : `sub`, `iss`, `aud`, claims temporels standard et scopes; `org_id`/tenant uniquement si nécessaire. Aucune donnée de profil dans le token.
- Autorisation : les scopes `:self` exigent correspondance avec `sub`; accès support contrôlé et audité; décision CNS obligatoire fail-closed si non vérifiable. Un scope client universel `profile:*` est interdit.
- API/événements : API profil; ProfileProjection, ExperienceProjection. Consomme IdentityRef, Consent/Privacy, CountryConfig et référentiels autorisés.
- Réseau : aucun accès direct aux DB tierces; flux sortants limités aux contrats D3. DNS interne requis; exposition publique seulement via edge/API management.
- Sécurité : minimisation forte, chiffrement, audit des accès sensibles, interdiction d’export du dossier complet sans finalité.
- Résilience : lecture de dernière version locale autorisée selon fraîcheur; traitement personnel non autorisé fail-closed sur décision privacy requise.
- Scaling : unité `subject`; séparation lecture/écriture possible sans changer l’ownership.
- Repo candidat : `brendolys-ydiase-profile`. CI/CD, artefact, secrets et workload identity propres.
- Runbook/DR : perte DB, corruption, suppression accidentelle, révocation privacy, restauration puis réconciliation des projections.
- Gate Contract Registry : `CLOSED` pour PRF-IAM.
- Gates préproduction : RPO/RTO/SLO, rétention, clients OIDC physiques, step-up si requis, tests restore et validation finale de la fusion PRF-002.