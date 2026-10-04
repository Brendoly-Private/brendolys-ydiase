# YD-MS-PRF-001 — Profile

Statut : `autonomy-profile-draft`

- Logique : PRF-001 + PRF-002. Gate fusion PRF-002 avant production Burkina.
- Données possédées : Profile Core, préférences/objectifs, EducationRecord, ExperienceRecord. Données personnelles; sous-modèles, permissions, rétention et audit séparés.
- Datastore : privé au service; migrations privées; aucune lecture DB externe.
- Backup/restore : obligatoire, chiffré, restauration indépendante et testée. Criticité C1 confirmée par le registre; RPO/RTO/SLO restent à fixer selon cette criticité.
- IAM : `brendolys-customers` principal; `brendolys-internal` uniquement fonctions support autorisées. `brendolys-networks` sans accès par défaut. Autorisation objet par `subject_id`/organisation.
- API/événements : API profil; ProfileProjection, ExperienceProjection. Consomme IdentityRef, Consent/Privacy, CountryConfig et référentiels autorisés.
- Réseau : aucun accès direct aux DB tierces; flux sortants limités aux contrats D3. DNS interne requis; exposition publique seulement via edge/API management.
- Sécurité : minimisation forte, chiffrement, audit des accès sensibles, interdiction d’export du dossier complet sans finalité.
- Résilience : lecture de dernière version locale autorisée selon fraîcheur; traitement personnel non autorisé fail-closed sur décision privacy requise.
- Scaling : unité `subject`; séparation lecture/écriture possible sans changer l’ownership.
- Repo candidat : `brendolys-ydiase-profile`. CI/CD, artefact, secrets et workload identity propres.
- Runbook/DR : perte DB, corruption, suppression accidentelle, révocation privacy, restauration puis réconciliation des projections.
- Gate production : RPO/RTO/SLO, rétention, realms/scopes/audience, tests restore et séparation PRF-002 validés.