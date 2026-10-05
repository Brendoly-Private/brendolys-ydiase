# YD-MS-PRF-002 — Education & Experience Profile

Statut : `autonomy-profile-draft`

## Nature et criticité

- Nature : `AUTH`.
- Criticité : `C1`.
- PRF-002 n'est jamais traité comme `DERIVED`.
- La perte de son datastore constitue une perte de données métier autoritatives et non une simple perte de projection reconstruisible.

## Mission

Conserver l'historique individuel éducatif et professionnel déclaré ou vérifié, ses réalisations et ses liens de preuve sans devenir propriétaire des référentiels Education, Skills ou des décisions Privacy.

## Données autoritatives possédées

- `EducationRecord`
- `ExperienceRecord`
- `AchievementClaim`
- `ProfileEvidenceLink`
- états de vérification propres aux déclarations
- références de provenance nécessaires
- temporalité et versions métier associées

PRF-002 est la source autoritative YDIASE de cet historique personnel. EDU reste autoritatif pour les institutions, programmes, curricula et qualifications de référence. SKL reste autoritatif pour les taxonomies et états de compétences relevant de ses frontières.

## Non-reconstructibilité

L'historique PRF-002 ne peut pas être reconstruit de manière complète depuis EDU, SKL, DAT, des pièces externes ou PRF-001.

Ces sources peuvent confirmer certaines références ou preuves, mais elles ne possèdent pas nécessairement :

- la déclaration originale du sujet
- les corrections successives
- la temporalité complète
- les états de vérification historiques
- les relations entre déclarations et preuves
- les décisions de retrait ou rectification
- les métadonnées de provenance propres au dossier individuel

En conséquence, un `FULL_REBUILD` depuis les services amont n'est pas une stratégie DR valide pour PRF-002.

## Datastore

- datastore autoritatif privé à PRF-002
- migrations privées
- credentials propres
- aucune base partagée avec PRF-001, EDU, SKL, DAT ou CNS
- aucune lecture directe de la base par un autre service
- aucune réplication complète vers un autre microservice comme mécanisme de secours

## Politique de sauvegarde autoritative

La sauvegarde est `MANDATORY-AUTH-BACKUP`.

PRF-002 doit disposer avant `ready-for-production` :

1. de sauvegardes chiffrées du datastore autoritatif
2. d'une politique de sauvegarde indépendante de PRF-001
3. d'une rétention de sauvegarde documentée selon les catégories de données et les règles pays
4. d'une protection contre la suppression ou l'altération accidentelle des sauvegardes
5. d'un contrôle d'accès distinct pour les opérations de backup et restore
6. d'une vérification d'intégrité des sauvegardes
7. d'une traçabilité des opérations de sauvegarde et restauration
8. d'une procédure de restauration documentée et testée
9. d'une copie de secours dont le blast radius ne se confond pas avec celui du datastore actif
10. d'un mécanisme permettant de restaurer une version cohérente de l'historique sans dépendre de la disponibilité de PRF-001

Les technologies, fréquences et emplacements physiques restent soumis aux ADR d'infrastructure. Ils ne doivent pas être inventés dans ce profil.

## RPO / RTO / SLO

- RPO : `TBD-PREPROD`
- RTO : `TBD-PREPROD`
- SLO : `TBD-PREPROD`

Ces valeurs doivent provenir de l'analyse de criticité C1 et du capacity planning. Aucune valeur arbitraire n'est acceptée.

## Restore gate

PRF-002 ne passe pas `ready-for-production` tant qu'un test de restauration indépendant n'a pas démontré au minimum :

- restauration d'une sauvegarde exploitable dans un environnement isolé
- validation d'intégrité des agrégats autoritatifs
- conservation des identifiants durables
- conservation de la temporalité et des versions
- conservation des liens de preuve et références de provenance
- absence de dépendance à une base PRF-001 pour récupérer l'historique
- réconciliation contrôlée des projections et consommateurs après restauration
- traçabilité de l'opération
- respect des décisions Privacy applicables après restauration

Un backup jamais restauré avec succès ne ferme pas le gate REC.

## Scénarios DR obligatoires

Le runbook PRF-002 doit couvrir :

- perte complète du datastore actif
- corruption logique ou physique
- suppression accidentelle d'un historique
- restauration à un point antérieur autorisé
- divergence entre datastore autoritatif et projections aval
- indisponibilité simultanée d'EDU ou DAT pendant la restauration
- preuve orpheline après restauration
- correction contestée
- révocation Privacy reçue avant ou pendant un incident
- reprise des événements après restauration sans duplication métier

## Cohérence après restauration

Le datastore restauré reste l'autorité PRF-002. Les projections aval doivent se réconcilier depuis PRF-002 et non imposer leur état au service restauré.

Toute republication d'événements doit utiliser des mécanismes idempotents et préserver les versions métier afin d'éviter la duplication ou la régression silencieuse des consommateurs.

## Privacy et sauvegardes

CNS-001 reste autoritatif pour les finalités, restrictions, demandes Privacy et instructions applicables de rétention ou d'effacement.

La politique de backup doit documenter le traitement des données supprimées ou révoquées présentes dans des sauvegardes historiques. Une restauration ne doit pas réactiver durablement une donnée dont la suppression est devenue applicable. La procédure de reprise doit donc réappliquer les décisions Privacy pertinentes après restauration.

Les conflits entre conservation probatoire et effacement exigent une règle de conformité documentée. PRF-002 ne tranche pas ce conflit implicitement.

## Temporalité et preuves

Chaque historique conserve, lorsque pertinent, période de validité métier, observation ou déclaration, enregistrement, version et état de vérification. Une correction ne réécrit pas silencieusement l'histoire.

Une déclaration, une preuve et une vérification restent distinctes. Une preuve de diplôme ou d'expérience ne crée pas automatiquement une compétence autoritative.

## IAM

- Audience : `ydiase-profile-history`.
- Realms : `brendolys-customers` principal, `brendolys-internal` pour support ou conformité explicitement autorisés, `brendolys-networks` refusé par défaut.
- M2M : workload identity dédiée.
- Scopes candidats : `profile-history:read:self`, `profile-history:education:write:self`, `profile-history:experience:write:self`, `profile-history:evidence:write:self`, `profile-history:read:support`, `profile-history:projection:read`, `profile-history:verify`.
- Les scopes finaux passent par le Contract Registry.
- Les opérations administratives de backup/restore ne réutilisent pas les scopes utilisateur et suivent une identité opérationnelle dédiée selon l'ADR IAM/infrastructure.

## Autorisation

`:self` exige correspondance avec le sujet. La vérification utilise un rôle ou scope séparé du droit de déclaration. Aucun consommateur ne reçoit l'historique complet lorsqu'une projection minimale suffit.

## API et événements

API : commandes de déclaration et correction des historiques, consultation autorisée, rattachement ou détachement de preuves et projections minimales. Aucun accès DB direct par PRF-001.

Événements candidats : changements d'historique, de vérification et de disponibilité de preuve avec payload minimal, versionné et sans diffusion inutile de PII. Les noms et schémas définitifs relèvent du Contract Registry.

## Données consommées

IdentityRef minimal, décisions CNS, CountryConfig, références Institution/Program/Qualification depuis EDU, taxonomies nécessaires depuis SKL et références de provenance depuis DAT-003. Ces références ne deviennent pas des copies autoritatives locales.

## Réseau et sécurité

- DNS interne requis
- exposition utilisateur uniquement via edge/API management
- flux sortants limités aux contrats D3
- aucun accès direct aux bases PRF-001, EDU, SKL, DAT ou CNS
- chiffrement au repos et en transit
- audit des consultations et mutations sensibles
- minimisation des projections
- séparation déclaration/vérification
- protection renforcée des pièces et métadonnées de preuve
- secrets, certificats et workload identity propres
- aucun secret partagé avec PRF-001

## Résilience

La consultation du dernier état local reste possible selon politique. Une panne EDU n'efface ni ne rend faux l'historique déjà enregistré. Les nouvelles liaisons nécessitant une référence autoritative indisponible sont mises en attente ou refusées selon le contrat. Une décision Privacy obligatoire non vérifiable entraîne fail-closed pour la mutation concernée.

## Scaling et exploitation

- unité principale : `subject`
- volumes historiques potentiellement supérieurs au profil courant
- index et projections de lecture séparables sans transfert d'autorité
- repo candidat : `brendolys-ydiase-profile-history`
- repo, CI/CD, artefact, migrations, secrets, workload identity, backup, restore, observabilité et rollback propres
- logs sans PII inutile
- métriques de mutation, lecture, vérification, backup et restore
- traces corrélées sans contenu sensible
- health/readiness indépendants

## Retrait et migration

Tout export ou remplacement du service doit préserver les identifiants durables, la temporalité, les versions, la provenance et les liens de preuve. Une migration ne doit pas aplatir l'historique en simple profil courant.

Le retrait de PRF-002 exige une migration vérifiée de l'autorité et une preuve de restauration du système successeur avant suppression des sauvegardes encore requises.

## Gates préproduction

- owner opérationnel et suppléant
- RPO/RTO/SLO validés
- technologie et topologie de backup décidées par ADR
- fréquence de sauvegarde définie
- rétention des backups définie par catégorie et pays
- contrôle d'accès backup/restore défini
- chiffrement et gestion des clés définis
- preuve de restauration indépendante réussie
- politique de pièces de preuve
- clients OIDC physiques
- step-up si requis
- contrats PRF-001/EDU/SKL/DAT/CNS
- règles de portabilité et effacement
- procédure de réapplication Privacy après restore
- runbook DR testé

Tant que la preuve de restauration indépendante n'existe pas, le bloc `REC` reste `TBD-PREPROD` et PRF-002 ne peut pas atteindre `ready-for-production`.