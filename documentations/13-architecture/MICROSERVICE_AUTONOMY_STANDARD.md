# Microservice Autonomy Standard — BRENDOLYS YDIASE

Statut : `D3-normative-candidate`

## 1. Objet

Ce standard définit l’autonomie obligatoire des frontières physiques YDIASE. Il s’applique aux 47 `YD-MS-*` confirmés et, avec adaptations explicites, aux 4 `YD-PLT-*`. Il ne signifie pas qu’un microservice doit posséder un serveur physique complet. Il signifie qu’il doit pouvoir être développé, déployé, sécurisé, observé, sauvegardé, restauré, mis à l’échelle et retiré sans dépendre du cycle de vie d’un autre microservice.

## 2. Règles non négociables

Chaque frontière autonome possède :

1. un identifiant physique stable
2. un repository Git propre
3. un owner d’équipe et un suppléant
4. un artefact de build/version propre
5. un pipeline CI/CD propre
6. un runtime et une configuration propres
7. un datastore possédé lorsqu’elle détient des données persistantes
8. ses migrations et son schéma privés
9. une politique backup/restore testée
10. RPO, RTO et SLO définis selon criticité
11. ses contrats API/événements/projections enregistrés
12. une identité machine propre
13. une politique IAM explicite
14. ses secrets et certificats gérés séparément
15. des règles réseau minimales et deny-by-default
16. chiffrement en transit et au repos selon classification
17. audit, logs, métriques et traces corrélables
18. health, readiness et dépendances vérifiables
19. quotas et rate limits lorsque l’exposition le demande
20. stratégie de scaling propre
21. rollback indépendant
22. mode dégradé documenté
23. runbook d’incident
24. plan de reprise et test de restauration
25. politique de rétention et suppression
26. procédure de retrait/decommission
27. registre des dépendances autorisées et interdites
28. SBOM et politique de dépendances logicielles
29. scans de vulnérabilités et règles de patching
30. tests de contrats et de compatibilité

## 3. Repository et supply chain

Convention cible : un repository par frontière physique. Le nom exact sera fixé dans le registre des déploiements, avec convention candidate `brendolys-ydiase-<service-slug>`.

Le repository contient au minimum : code, README opérationnel, manifestes de build, migrations détenues, tests, contrats publiés par le service, configuration non secrète, runbook, ownership, politique de version et changelog.

Les secrets, clés privées, tokens, mots de passe et sauvegardes n’entrent jamais dans Git.

Chaque build produit un artefact immuable et traçable vers commit, pipeline, SBOM et résultats de contrôles. Une release de service n’exige pas la release simultanée d’un autre service.

## 4. Données et datastore

Chaque microservice est seul propriétaire en écriture de ses agrégats. Aucun autre service ne lit directement ses tables, collections ou fichiers internes.

`Database per service` signifie propriété exclusive du schéma, des migrations, des credentials et du cycle backup/restore. Plusieurs services peuvent utiliser un même cluster physique si l’isolation logique, les credentials, quotas, sauvegardes et restaurations indépendantes sont démontrés. Les services de criticité ou sensibilité élevée peuvent imposer une isolation physique par ADR.

Les jointures interservices en base sont interdites. Les besoins transverses utilisent API, événement ou projection gouvernée.

## 5. Backup, restore et reprise

Chaque frontière persistante définit : classification des données, fréquence de backup, type de backup, chiffrement, rétention, localisation, contrôle d’accès, RPO, RTO, procédure de restauration et fréquence de test.

Une sauvegarde non testée n’est pas considérée comme capacité de reprise. La restauration d’un microservice ne doit pas exiger la restauration coordonnée de tous les autres. Les incohérences post-restore sont traitées par replay, réconciliation ou reconstruction de projections documentés.

Les projections reconstructibles peuvent avoir une politique différente des sources autoritatives.

## 6. API, événements et DNS

Chaque frontière possède ses contrats. Une API interne ou externe doit être versionnée, authentifiée, autorisée, limitée et observable selon sa classe.

Un sous-domaine n’est créé que pour une exposition réseau justifiée. L’autonomie n’impose pas 51 domaines publics. Les noms DNS internes et externes doivent rester séparés. Aucun datastore n’est exposé publiquement.

Les endpoints publics passent par les contrôles d’edge définis par l’architecture. Les communications internes ne contournent pas les politiques d’identité machine et réseau.

## 7. BRENDOLYS Identity

BRENDOLYS Identity est l’IAM externe de référence. YDIASE ne stocke aucun mot de passe utilisateur.

Realms autorisés :

- `brendolys-internal` : employés et équipe interne
- `brendolys-networks` : ambassadeurs et membres externes des réseaux
- `brendolys-customers` : élèves, étudiants, professionnels, organisations clientes et utilisateurs clients

Issuer OIDC : `https://sso.godinfradsby.xyz/realms/{realm}/protocol/openid-connect`.

Pour chaque microservice, la fiche d’autonomie doit déclarer : realms acceptés, audience, clients autorisés, scopes, rôles, claims minimaux, règles tenant/organisation, politiques de step-up si nécessaires et comportement en indisponibilité IAM.

Un token valide n’accorde jamais automatiquement une permission métier. L’autorisation reste contrôlée par les politiques du domaine.

## 8. Service-to-service

Les appels machine-to-machine utilisent une identité de workload/service dédiée. Les credentials utilisateur ne sont pas réutilisés comme secret permanent de service. Le mécanisme final de workload identity sera choisi par ADR.

Chaque relation déclare : caller, callee, audience, scopes machine, protocole, timeout, retry, circuit breaker si nécessaire et comportement de panne.

## 9. Secrets et certificats

Chaque frontière a un namespace logique de secrets. L’accès est least-privilege. Rotation, révocation, expiration et audit sont obligatoires. Aucun secret partagé global entre tous les microservices.

Les certificats ont propriétaire, durée, rotation et procédure d’urgence documentés.

## 10. Réseau

Politique cible : deny-by-default entre workloads. Les flux autorisés dérivent de `DEPENDENCY_MAP.md` et du futur Contract Registry. Un service ne reçoit pas un accès réseau parce qu’il appartient au même cluster.

Les flux vers bases, cache, broker, stockage objet, IAM, observabilité et services externes sont explicitement déclarés.

## 11. Chiffrement et classification

TLS est requis pour les communications transportant des données non publiques. Les données au repos suivent la classification définie par sécurité/conformité. Les données personnelles sensibles et très sensibles reçoivent des contrôles renforcés, minimisation et journalisation d’accès.

## 12. Observabilité

Chaque frontière produit : logs structurés, métriques techniques, métriques de service, traces distribuées lorsque pertinentes, identifiants de corrélation, événements de sécurité et alertes reliées à des SLO.

Aucun log ne doit devenir une copie incontrôlée de données personnelles, tokens ou secrets.

## 13. Health et readiness

Chaque déploiement expose des contrôles séparant au minimum : process alive, capacité à recevoir du trafic, état des dépendances critiques et version de build. Une dépendance analytique facultative ne doit pas rendre un service transactionnel indisponible si son mode dégradé le permet.

## 14. Résilience

Chaque dépendance distante possède timeout. Les retries ne sont appliqués qu’aux opérations sûres/idempotentes ou protégées par clé d’idempotence. Les cascades de retries sont interdites.

Le service documente ses bulkheads, limites de concurrence, files d’attente, backpressure, circuit breakers et stratégie de shedding lorsque son profil le justifie.

## 15. Scaling et capacité

Chaque frontière déclare son unité de scaling, ses métriques de saturation, ses limites de ressources et ses contraintes stateful/stateless. Aucun service ne doit exiger le scaling simultané de tout YDIASE.

## 16. CI/CD et environnements

Chaque service peut être construit, testé, promu et rollback indépendamment. Les environnements et promotions sont tracés. Les migrations incompatibles suivent une stratégie expand/migrate/contract ou équivalent documenté.

Un déploiement ne peut pas supposer que tous les consommateurs migrent instantanément.

## 17. Sécurité applicative

Chaque frontière définit threat model proportionnel, validation d’entrée, autorisation objet/action, protections contre abus, politique de dépendances, scans SAST/SCA/image, gestion des vulnérabilités et preuves de correction.

Les services sensibles incluent tests d’accès horizontal/vertical et tests de séparation tenant/organisation lorsque concernés.

## 18. Audit

Les faits de sécurité et actions sensibles sont transmis à `YD-PLT-AUD-001` sans abandonner les logs opérationnels locaux. Le producteur reste responsable de la qualité du fait audité. L’Audit Service ne devient pas owner du fait métier.

## 19. SLO, RTO, RPO et criticité

Aucune valeur universelle n’est inventée. Chaque service reçoit une classe de criticité puis des objectifs mesurables. Les valeurs sont approuvées avant passage en production. Les services dépendants ne peuvent exiger un SLO supérieur à celui que leur fournisseur déclare sans ADR de mitigation.

## 20. Mode dégradé

Chaque fiche précise ce que le service fait lorsque IAM, broker, datastore secondaire, moteur AI, Search, Analytics, Notification ou une dépendance métier est indisponible. Les comportements possibles sont : fail-closed, fail-open explicitement autorisé, lecture stale bornée, mise en file, réponse partielle ou indisponibilité contrôlée.

Les décisions de sécurité et privacy ne passent jamais en fail-open par défaut.

## 21. DR et tests

Le plan DR identifie perte de zone/serveur, corruption logique, suppression accidentelle, compromission, perte de datastore et indisponibilité d’une dépendance externe. Les procédures sont testées à fréquence définie selon criticité.

## 22. Retrait

Un service ne disparaît pas par suppression de son repository. Le retrait traite consommateurs, contrats, événements, données, backups, DNS, certificats, secrets, IAM clients/scopes, dashboards, alertes, jobs, files, projections et obligations de conservation.

## 23. Template obligatoire par frontière

Chaque `YD-MS-*` et `YD-PLT-*` reçoit une `AUTONOMY_PROFILE.md` ou section équivalente contenant :

- Physical Boundary ID
- logical services contained
- business owner / technical owner / backup owner
- repository
- build artifact
- runtime class
- datastore(s) owned
- migration owner
- data classification
- backup policy / restore procedure / last restore test
- RPO / RTO / SLO / criticality
- internal API / external API / events / projections
- internal DNS / external DNS if any
- accepted BRENDOLYS Identity realms
- OIDC audience / clients / scopes / roles / claims
- workload identity
- secrets namespace / certificate policy
- inbound network flows / outbound network flows
- encryption requirements
- audit events
- logs / metrics / traces / dashboards / alerts
- liveness / readiness / startup checks
- quotas / rate limits / concurrency limits
- scaling unit / autoscaling signals
- deployment strategy / rollback
- dependencies / forbidden dependencies
- degraded modes
- runbook / incident owner
- DR procedure / test cadence
- retention / deletion
- decommission checklist
- open ADRs

## 24. Gates

Un service ne passe pas `ready-for-production` si une ligne obligatoire de son profil reste inconnue sans ADR ou dérogation datée. Les valeurs `TBD` sont permises pendant la conception mais bloquent les gates auxquels elles se rapportent.

## 25. Application

Le standard s’applique immédiatement aux 47 microservices métier et aux 4 composants de plateforme fixés dans `MICROSERVICE_BOUNDARY_REVIEW.md`. Les trois frontières `DEFERRED` reçoivent un profil candidat minimal mais pas de ressources d’exploitation dédiées avant leur ADR d’extraction.
