---
title: 'Fondation documentaire de BRENDOLYS YDIASE'
type: 'documentation-baseline'
created: '2026-10-04'
status: 'approved'
delivery_kind: 'baseline-documentaire'
documentation_status: 'approved-for-baseline'
route: 'dispatch'
review_loop_iteration: 2
context:
  - '/opt/brendolys-ydiase/documentations/'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Contexte et intention

**Problème :** BRENDOLYS YDIASE vise une infrastructure panafricaine reliant éducation, compétences, carrières et emploi. Ses notes fondatrices sont riches, mais aucune gouvernance documentaire ne relie encore vision, capacités, exigences, décisions, données, services, contrats et vérifications.

**Approche :** Créer une baseline documentaire française, organisée par domaines métier et capacités transversales. Elle établit le registre maître, les identifiants, les modèles et les documents de cadrage nécessaires à un corpus extensible. Tout microservice identifié dans l’architecture cible reçoit une fiche minimale dès son identification ; seuls les contrats détaillés deviennent prescriptifs lorsque leurs prérequis sont validés.

## Principes directeurs et limites

**Toujours :** employer exclusivement le nom BRENDOLYS YDIASE ; séparer domaine, produit, capacité, microservice et infrastructure ; attribuer chaque type de donnée à une source métier autoritative ; concevoir la cible panafricaine tout en distinguant le pilote Burkina ; documenter provenance, qualité, version, validité, responsabilité, droits d’usage et finalité des données ; préserver l’historique lorsqu’il a une valeur analytique ou probatoire ; rendre chaque décision, exigence, risque et hypothèse traçable.

**Jamais :** adopter BRENDOLYS NEXORA ou BRENDOLYS IDIASE ; imposer un nombre de microservices ; traiter l’IA conversationnelle comme source de vérité ; rendre Kafka, Spark, Flink, Cassandra, HBase, GPU ou service mesh obligatoires sans ADR et seuil d’activation ; assimiler les offres publiées au marché du travail réel ; commercialiser des données personnelles.

### Organisation documentaire

Les domaines métier constituent la référence fonctionnelle. Data, Knowledge, Analytics et AI restent distincts, y compris lorsque leurs premiers documents cohabitent. Les capacités transversales relient les domaines sans les remplacer. Tout élément durable reçoit un identifiant stable, non réutilisable et traçable après renommage ou retrait. La maturité fonctionnelle et la couverture géographique sont deux dimensions indépendantes.

## Situations de référence

| Situation | Comportement attendu |
|---|---|
| Document créé, modifié ou obsolète | Statut, propriétaire principal et suppléant, version, date de revue et transition approuvée sont enregistrés ; un brouillon ne fait pas référence. |
| Exigence critique consultée | Son origine, capacité, décision, phase, composants concernés et critères de vérification sont retrouvables. |
| Deux sources se contredisent | Les assertions sont conservées séparément avec provenance, niveau de confiance et statut jusqu’à arbitrage documenté. |
| Même entité présente dans plusieurs systèmes | L’Autoritative Source Registry désigne le propriétaire, le système autoritatif, copies permises, consommateurs et règles de synchronisation. |
| Donnée évolutive ou retirée | Historique, période de validité, compatibilité, notification des consommateurs et retrait contrôlé sont documentés. |
| Nouveau microservice cible | Fiche minimale obligatoire : domaine, mission, frontières, capacités, données, dépendances, phase, maturité documentaire et condition d’activation. |
| Nouvelle technologie ou IA | ADR ; finalité, données accessibles, risques, évaluation, métriques et seuil d’activation sont obligatoires. |
| Nouvelle donnée personnelle | Base légale ou consentement, finalités, accès, rétention, restrictions géographiques et effacement sont définis. |
| Nouveau pays | Country Framework validé : éducation, qualifications, territoires, langues, monnaies, droit, classifications et sources. |
| Suppression ou remplacement d’un service | Contrats, événements, données, dépendances, migration et décision de retrait sont vérifiés. |
| Document remplacé | Son statut devient `SUPERSEDED`, avec un lien obligatoire et vérifié vers son successeur. |

</frozen-after-approval>

## Sources et périmètre documentaire

- `documentations/` -- racine documentaire, vide à l’exception des artefacts de test.
- Documents joints de vision, modèle économique, viabilité et hiérarchie documentaire -- sources à traduire en décisions, capacités et hypothèses vérifiables.
- Cette livraison couvre le système documentaire et les fiches minimales de tous les microservices de l’architecture cible ; elle ne déclenche ni développement, ni déploiement, ni activation.

## Résultats attendus

### Gouvernance documentaire

- [x] `documentations/README.md`, `GLOSSAIRE_METIER.md` et `REGISTRE_DOCUMENTAIRE.md` -- fournir l’entrée de lecture, le vocabulaire de référence et le catalogue maître des documents.
- [x] `documentations/00-gouvernance-documentaire/` -- créer charte, registre des décisions, référentiel des exigences, matrice de traçabilité, convention d’identifiants, registre des risques, registre des hypothèses, registre des sources, registre des systèmes autoritatifs, cycle de vie et modèles versionnés.
- [x] Le registre -- suivre au minimum ID, titre, domaine, propriétaire et suppléant, statut, version, phase, maturité, dépendances, impacts, dernière et prochaine revue.
- [x] Le cycle documentaire -- appliquer `DRAFT`, `IN_REVIEW`, `APPROVED`, `ACTIVE`, `DEPRECATED`, `RETIRED`, `REJECTED` et `SUPERSEDED` ; un élément `SUPERSEDED` référence obligatoirement son successeur.

### Fondation métier

- [x] `documentations/01-fondations-produit/` -- établir charte, vision, limites, parties prenantes, modèle de valeur, trajectoire Burkina et distinction entre offres observées, besoins déclarés, estimés, institutionnels, informels et signaux économiques.
- [x] `documentations/02-identite-profils/` à `11-economie-produit/` -- créer les dossiers : identité-profils, éducation-institutions, compétences-connaissances, métiers-carrières, marché-travail, opportunités-recrutement, orientation-recommandation, contenu-communauté-learning, partenaires-écosystème et économie-produit. Chaque domaine reçoit mission, frontières, termes, propriétaire, dépendances et exclusions.
- [x] `documentations/16-country-frameworks/` et `17-roadmap-phases/` -- créer le cadre multi-pays et les phases P1…Pn ; associer chaque capacité à une maturité M0 Concept, M1 Documenté, M2 Pilote, M3 Production, M4 Industrialisé, M5 Optimisé et une couverture G0 Non déployé, G1 Burkina, G2 Multi-pays, G3 Région ou G4 Continental.

### Capacités transversales

- [x] `documentations/12-data-knowledge-analytics-ai/` -- séparer données, connaissance, analytique et IA ; définir le réseau de sources YDIASE, collecte, corroboration, validation, publication, surveillance et expiration.
- [ ] `documentations/13-architecture/` -- créer architecture cible, Service Map, Dependency Map, Event Map et une fiche minimale par microservice cible ; chaque service indique domaine, statut, justification, consommateurs et retrait.
- [x] `documentations/14-securite-conformite/` et `15-exploitation-resilience/` -- définir classification, modèles de menace, contrôles vérifiables, criticité, RTO, RPO, sauvegardes, tests de restauration et responsables.

## Cadence de mise en œuvre

La fiche minimale d’un microservice est obligatoire dès son identification. Sa documentation progresse de D0 Identifié à D6 Production. Un cahier détaillé devient obligatoire à l’approche d’une phase, à l’exposition d’une API ou d’un événement, au traitement de données personnelles, à une criticité définie ou à un changement incompatible. Une invalidation de domaine, phase ou décision déprécie explicitement les documents dérivés et bloque leur usage comme référence active.

## Critères d’acceptation

- Given un lecteur découvrant le dépôt, when il ouvre `documentations/README.md`, then il comprend le produit, l’ordre de lecture, les statuts et l’emplacement des sujets.
- Given une exigence métier critique, when elle est consultée, then son origine, sa décision, sa phase, ses composants et ses vérifications sont traçables.
- Given deux documents ou sources contradictoires, when la contradiction est détectée, then aucune définition ne devient référence sans décision documentée.
- Given une capacité lointaine non activée au Burkina, when le pilote est défini, then elle n’impose aucune dépendance technique sans ADR.
- Given une équipe souhaitant créer un service, when les prérequis du domaine sont incomplets, then le registre le signale et interdit son passage en réalisation.
- Given un microservice de l’architecture cible, when il est identifié, then une fiche D1 le rattache à un domaine, une phase et des conditions d’activation sans imposer son implémentation.
- Given une donnée utilisable par un moteur, when son droit, sa validité ou sa qualité change, then les consommateurs sont réévalués, suspendus ou migrés de façon traçable.
- Given une donnée métier, when elle est répliquée ou synchronisée, then son système autoritatif, les copies permises et les règles de synchronisation sont identifiables.
- Given un document remplacé, when son successeur est consulté, then le registre maintient le lien de succession et empêche l’ancien document d’être présenté comme actif.
- Given un service critique, when une panne ou compromission est envisagée, then criticité, dépendances, RTO, RPO, procédure et test de reprise sont identifiables.

## Vérification de la fondation

- Vérifier liens, identifiants uniques, métadonnées requises, propriétaires valides, statuts autorisés, successeurs des documents remplacés et dépendances résolues.
- Vérifier que tout document créé figure dans le registre et qu’aucun nom NEXORA ou IDIASE ne subsiste dans les nouveaux livrables.

## Journal de décision et d’évolution

### Triage de revue 2026-10-04

Les recommandations relatives aux exigences, ADR, glossaire, Country Framework, historisation, contradictions de données, maturité, cycle de vie, sécurité mesurable, activation des services et contrôles de registre sont intégrées. Les corrections de prose et l’organisation par résultats remplacent les intitulés techniques initiaux. La révision 2 ajoute les sources autoritatives, les registres des risques, hypothèses et sources, la séparation maturité/couverture, le renommage du domaine 12 et la succession obligatoire des documents remplacés.

## Notes d’implémentation

La première livraison produit les documents maîtres et leur index. Les spécifications de microservices, API, bases, événements et procédures d’exploitation seront créées à partir du registre selon les déclencheurs définis ci-dessus.

Baseline physique créée le 2026-10-04 : index, glossaire, registre, charte de gouvernance, modèles, charte produit, carte des domaines et dossiers de capacité.
