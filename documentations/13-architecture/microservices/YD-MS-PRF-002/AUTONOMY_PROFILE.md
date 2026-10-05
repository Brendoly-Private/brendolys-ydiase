# YD-MS-PRF-002 — Education & Experience Profile

Statut : `autonomy-profile-draft`

- Logique : PRF-002. Frontière physique autonome selon `ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md`.
- Mission : conserver l'historique individuel éducatif et professionnel déclaré ou vérifié, ses réalisations et ses liens de preuve sans devenir propriétaire des référentiels Education, Skills ou des décisions Privacy.
- Données possédées : EducationRecord, ExperienceRecord, AchievementClaim, ProfileEvidenceLink, états de vérification propres à ces déclarations, références de provenance nécessaires et temporalité métier associée.
- Autorité : source autoritative YDIASE de l'historique éducatif/professionnel individuel. EDU reste autoritatif pour institutions, programmes, curricula et qualifications de référence. SKL reste autoritatif pour taxonomies et profils de compétences selon leurs frontières.
- Temporalité : chaque historique conserve, lorsque pertinent, période de validité métier, observation/déclaration, enregistrement, version et état de vérification. Une correction ne réécrit pas silencieusement l'histoire.
- Preuves : une déclaration, une preuve et une vérification restent distinctes. Une preuve de diplôme ou d'expérience ne crée pas automatiquement une compétence autoritative.
- Datastore : privé au service, migrations privées, aucune lecture DB externe et aucun datastore partagé avec PRF-001, EDU, SKL ou DAT.
- Backup/restore : obligatoire, chiffré, restauration indépendante et testée. Nature `AUTH`. Criticité candidate `C1` en raison de la sensibilité, de la valeur historique et du coût de perte. RPO/RTO/SLO restent `TBD-PREPROD`.
- Reconstruction : PRF-002 n'est pas un service DERIVED. Les preuves externes et référentiels ne suffisent pas à reconstruire l'historique personnel complet. Le backup autoritatif est obligatoire.
- IAM audience : `ydiase-profile-history`.
- IAM realms : `brendolys-customers` principal, `brendolys-internal` pour support/conformité explicitement autorisés, `brendolys-networks` refusé par défaut. M2M par workload identity dédiée.
- Scopes candidats : `profile-history:read:self`, `profile-history:education:write:self`, `profile-history:experience:write:self`, `profile-history:evidence:write:self`, `profile-history:read:support`, `profile-history:projection:read`, `profile-history:verify`. Les scopes finaux passent par le Contract Registry.
- Autorisation : `:self` exige correspondance avec le sujet. La vérification utilise un rôle ou scope séparé du droit de déclaration. Aucun consommateur ne reçoit l'historique complet lorsqu'une projection minimale suffit.
- Privacy : CNS-001 reste autoritatif pour finalités, restrictions, demandes et instructions de rétention/effacement. PRF-002 applique ces décisions. Les conflits entre conservation probatoire et effacement exigent une règle de conformité documentée, jamais une décision locale implicite.
- API : commandes de déclaration/correction des historiques, consultation autorisée, rattachement/détachement de preuves et projections minimales. Aucun accès DB direct par PRF-001.
- Événements candidats : changements d'historique, de vérification et de disponibilité de preuve avec payload minimal, versionné et sans diffusion inutile de PII. Les noms et schémas définitifs relèvent du Contract Registry.
- Données consommées : IdentityRef minimal, décisions CNS, CountryConfig, références Institution/Program/Qualification depuis EDU, taxonomies nécessaires depuis SKL, références de provenance depuis DAT-003. Ces références ne deviennent pas des copies autoritatives locales.
- Réseau : DNS interne requis. Exposition utilisateur uniquement via edge/API management. Flux sortants limités aux contrats D3. Aucun accès direct aux bases de PRF-001, EDU, SKL, DAT ou CNS.
- Sécurité : chiffrement au repos et en transit, audit des consultations et mutations sensibles, minimisation des projections, séparation déclaration/vérification, protection renforcée des pièces et métadonnées de preuve.
- Secrets/certificats : secrets, certificats et workload identity propres. Aucun secret partagé avec PRF-001.
- Résilience : consultation du dernier état local autorisé selon politique. Une panne EDU n'efface ni ne rend faux l'historique déjà enregistré. Les nouvelles liaisons nécessitant une référence autoritative indisponible sont mises en attente ou refusées selon le contrat. Une décision privacy obligatoire non vérifiable entraîne fail-closed pour la mutation concernée.
- Scaling : unité principale `subject`, avec volumes historiques potentiellement très supérieurs au profil courant. Index/projections de lecture peuvent être séparés sans transférer l'autorité.
- Repo candidat : `brendolys-ydiase-profile-history`. Repo, CI/CD, artefact, migrations, secrets, workload identity, sauvegarde, restauration, observabilité et rollback propres.
- Observabilité : logs sans PII inutile, métriques de mutation/lecture/vérification, traces corrélées sans contenu sensible, health/readiness indépendants.
- Runbook/DR : perte ou corruption DB, restauration historique, divergence avec projections, indisponibilité EDU/DAT/CNS, preuve orpheline, correction contestée, suppression accidentelle, réconciliation après restauration.
- Retrait/migration : export sémantique documenté, préservation des identifiants durables, temporalité, provenance et liens de preuve. Une migration ne doit pas aplatir l'historique en simple profil courant.
- Gates préproduction : owner opérationnel, RPO/RTO/SLO, règles de rétention par catégorie/pays, politique de pièces de preuve, clients OIDC physiques, step-up si requis, tests de restauration, contrats PRF-001/EDU/SKL/DAT/CNS, règles de portabilité et effacement.