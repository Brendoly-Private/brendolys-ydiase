# Autonomy Profile Register — BRENDOLYS YDIASE

Statut : `D3-autonomy-profile-baseline`

Ce registre applique `MICROSERVICE_AUTONOMY_STANDARD.md` aux 47 microservices métier et aux 4 composants de plateforme. Les valeurs chiffrées RPO/RTO/SLO, moteurs de stockage, protocoles et technologies restent `TBD` tant qu’une analyse de criticité ou un ADR ne les justifie pas. Aucun `TBD` concerné ne peut survivre au gate production.

## Légende

- Realms : `C` = brendolys-customers, `N` = brendolys-networks, `I` = brendolys-internal, `M2M` = identité machine dédiée.
- Exposition : `INT` = DNS interne, `EDGE` = API utilisateur via edge, `EXT` = API partenaire/client gouvernée, `NONE` = aucune API utilisateur.
- Backup : `AUTH` = données autoritatives à sauvegarder/restaurer, `DERIVED` = projection reconstruisible, `MIXED` = autoritatif + dérivé.
- Criticité candidate : `C1` haute, `C2` importante, `C3` standard. Elle doit être validée par exploitation avant production.

## Profils métier

| Boundary | Realms | Expo | Backup | Crit. | Données / stockage possédés | Dépendances structurantes | Mode dégradé principal |
|---|---|---|---|---|---|---|---|
| YD-MS-PRF-001 Profile | C,I,M2M | EDGE,INT | AUTH | C1 | profils, préférences, objectifs, éducation/expérience; PII sensible | Identity, CNS, CFG, référentiels | lecture bornée; privacy requise fail-closed |
| YD-MS-EDU-001 Institution Catalog | I,N,M2M; C lecture | EDGE,INT | AUTH | C2 | institutions, campus, statuts, versions | CFG, DAT validation, PRT/INS | lecture dernière version; création bloquée si config/source invalide |
| YD-MS-EDU-002 Program Catalog | I,N,M2M; C lecture | EDGE,INT | AUTH | C2 | programmes, rattachements, conditions | EDU-001, EDU-004, CFG | lecture stale; publication bloquée si institution/qualification non validable |
| YD-MS-EDU-003 Curriculum & Module | I,N,M2M; C lecture | EDGE,INT | AUTH | C2 | curricula, modules, versions, mappings | EDU-002, SKL-001 | draft possible; publication bloquée sans Program valide |
| YD-MS-EDU-004 Qualification Framework | I,M2M; C lecture | EDGE,INT | AUTH | C2 | qualifications, niveaux, équivalences pays | CFG, DAT-005 | dernière version; nouveaux mappings bloqués si référentiel absent |
| YD-MS-SKL-001 Skills Knowledge | I,M2M; C lecture | EDGE,INT | AUTH | C2 | skills, concepts, taxonomie, relations | DAT-005, EDU/CAR evidence | dernière taxonomie valide; nouveaux mappings inconnus bloqués |
| YD-MS-SKL-002 User Skills Profile | C,I,M2M | EDGE,INT | AUTH | C1 | compétences individuelles, niveaux, preuves | PRF, SKL-001, CNS | lecture bornée; écriture sensible suspendue sans privacy/identity |
| YD-MS-CAR-001 Occupation & Career Graph | I,M2M; C lecture | EDGE,INT | AUTH | C2 | métiers, exigences, relations carrière | SKL-001, CFG, LAB evidence | catalogue daté utilisable; édition bloquée si référentiel requis absent |
| YD-MS-CAR-002 Career Path & Transition | C,I,M2M | EDGE,INT | MIXED | C2 | trajectoires persistées et transitions; snapshots d’entrée | CAR-001, PRF, SKL-002 | résultat partiel/indisponible signalé; aucune invention de données |
| YD-MS-ASM-001 Assessment | C,I,M2M | EDGE,INT | AUTH | C1 | sessions, réponses/résultats, validité | Identity, CNS, CFG | reprise session selon règles; calcul sensible suspendu si privacy non vérifiable |
| YD-MS-ORI-001 Orientation & Decision Support | C,I,M2M | EDGE,INT | AUTH | C1 | dossiers, contraintes, comparaisons, décisions | PRF, ASM, REC, CNS | dossier consultable; nouvelle recommandation mise en attente si dépendances manquent |
| YD-MS-REC-001 Recommendation | C via ORI/edge,I,M2M | INT,EDGE | MIXED | C1 | runs, sets, scores, explications, module RSH non autoritatif | EDU,CAR,LAB,PRF,SKL,ASM,CNS | abstention ou résultat précédent daté; jamais ranking fabriqué |
| YD-MS-SRH-001 Search & Discovery | C,N,I,M2M | EDGE,INT | DERIVED | C2 | index de recherche seulement | EDU,CAR,OPP,CNT,LRN | recherche partielle; reconstruction index |
| YD-MS-LAB-001 Labor Signals | I,M2M | INT | AUTH | C2 | signaux normalisés, territoire, provenance refs | DAT-003/004, CFG, CAR/SKL refs | ingestion différée; aucun signal sans validation minimale |
| YD-MS-LAB-002 Labor Market Intelligence | I,M2M; C lecture produits autorisés | INT,EDGE | MIXED | C2 | indicateurs, séries, méthodologies | LAB-001, CFG | derniers indicateurs datés; recalcul différé |
| YD-MS-OPP-001 Opportunity | C,N,I,M2M | EDGE,INT | AUTH | C1 | opportunités, exigences, validité, politiques candidature | EMP-001, CFG, MOD | lecture possible; soumission revalide état; publication sensible bloquée |
| YD-MS-OPP-002 Opportunity Matching | C,I,M2M | EDGE,INT | MIXED | C2 | runs/matches et explications | OPP, PRF, SKL, CNS | abstention si inputs minimum absents; anciens matches datés |
| YD-MS-APP-001 Application | C,I,M2M | EDGE,INT | AUTH | C1 | candidatures, états, transitions | OPP, EMP-002, CNS, NTF | soumission bloquée si opportunité non validable; consultation dernier état |
| YD-MS-EMP-001 Employer | C organisations,I,M2M | EDGE,INT | AUTH | C2 | employeurs, vérification, statut | PRT, CFG, DAT validation | lecture; mutation sensible bloquée si vérification impossible |
| YD-MS-EMP-002 Talent & Recruitment | C organisations,I,M2M | EDGE,INT | AUTH | C1 | campagnes, viviers, décisions de sélection | EMP-001, APP, OPP-002, CNS | campagne consultable; décisions mises en attente si APP indisponible |
| YD-MS-CNT-001 Content | C,N,I,M2M | EDGE,INT | AUTH | C2 | contenus, versions, publication | MOD, CFG | contenu publié connu reste lisible; publication/retrait selon politique |
| YD-MS-CNT-002 Feed | C,N,I,M2M | EDGE,INT | DERIVED | C3 | projections/feed/ranking non autoritatifs | CNT, COM, MOD, SPN isolé | feed simplifié/chronologique ou indisponibilité contrôlée |
| YD-MS-COM-001 Community | C,N,I,M2M | EDGE,INT | AUTH | C2 | interactions, commentaires, relations | MOD, CNT, CNS | lecture bornée; nouvelles interactions suspendues si contrôle critique absent |
| YD-MS-LRN-001 Learning Discovery | C,N,I,M2M | EDGE,INT | MIXED | C2 | ressources propres + projections programmes/offres | EDU, SKL, MKT | ressources valides restent visibles; offre commerciale invalide masquée |
| YD-MS-NTF-001 Notification | M2M; I support | INT | AUTH | C2 | demandes, tentatives, états de livraison; pas de vérité métier | CNS/PRF préférences, providers externes | queue/retry; le métier ne rollback pas sauf règle explicite |
| YD-MS-PRT-001 Partner | N,I,M2M | EDGE,INT | AUTH | C1 | partenaires, accords, rôles, scopes | CFG, CNS selon contacts | nouvelle action suspendue si accord/droit non vérifiable |
| YD-MS-AMB-001 Ambassador Network | N,I,M2M | EDGE,INT | AUTH | C1 | mandats, renouvellements, contributions | PRT, DAT-002, CNS | collecte suspendue si mandat invalide; consultation bornée |
| YD-MS-DAT-001 Data Source Registry | I,M2M | INT | AUTH | C1 | sources, droits, territoires, politiques accès | PRT, CFG, CNS/legal registry | acquisition nouvelle fail-closed si droits non vérifiables |
| YD-MS-DAT-002 Data Acquisition | I,N via canal contrôlé,M2M | INT | AUTH | C2 | batches, raw envelopes, connecteur state | DAT-001, AMB/INS, external sources | queue/retry/backpressure; aucune publication directe métier |
| YD-MS-DAT-003 Data Provenance | I,M2M | INT | AUTH | C1 | lineage, assertions, preuves/références | DAT-002, sources | écriture durable/retry; publication aval suspendue sans preuve requise |
| YD-MS-DAT-004 Data Quality & Validation | I,M2M | INT | AUTH | C1 | règles, runs, décisions qualité, anomalies | DAT-002/003/005 | quarantaine; aucune promotion automatique en cas d’échec |
| YD-MS-DAT-005 Reference & Taxonomy | I,M2M; lecture services | INT | AUTH | C2 | datasets de référence, taxonomies transversales | CFG, sources validées | dernière version valide; mutation bloquée si source non validée |
| YD-MS-KNW-001 Knowledge Graph | I,M2M | INT | DERIVED | C2 | graphe dérivé, watermarks, mappings | EDU,SKL,CAR,LAB,DAT provenance | version précédente; reconstruction; jamais source autoritative |
| YD-MS-ANL-001 Analytics | I,M2M | INT | DERIVED | C2 | snapshots, agrégats, métriques dérivées | événements/projections domaines | données datées; recalcul; aucune écriture transactionnelle |
| YD-MS-ANL-002 Institution Intelligence | C org autorisée,I,M2M | EXT/EDGE,INT | MIXED | C2 | insights institutionnels, éditions, règles produit | ANL-001, EDU, BIL entitlement | dernière édition datée; accès fail-closed sur entitlement |
| YD-MS-ANL-003 Employer Intelligence | C org autorisée,I,M2M | EXT/EDGE,INT | MIXED | C2 | insights employeur, éditions, règles produit | ANL-001, EMP, LAB, BIL | dernière édition datée; accès fail-closed sur entitlement |
| YD-MS-AI-002 Retrieval & Grounding | M2M,I diagnostic | INT | DERIVED | C2 | index/corpus de grounding, citations refs | SRH, KNW, sources autorisées, CNS/purpose | abstention si grounding sous seuil; aucune réponse non fondée |
| YD-MS-AI-003 AI Verification | M2M,I diagnostic | INT | AUTH | C1 | décisions de vérification, evidence refs, règles | AI outputs, sources/grounding | fail-closed pour usage exigeant vérification; jamais auto-validation par générateur |
| YD-MS-BIL-001 Subscription & Entitlement | C organisations/clients,I,M2M | EDGE,INT | AUTH | C1 | plans, abonnements, entitlements, quotas commerciaux | BIL-002 état financier, catalogues produits | dernier entitlement valide selon règle; révocation prioritaire |
| YD-MS-BIL-002 Billing | C payeur,I,M2M | EDGE,INT | AUTH | C1 | comptes facturation, factures, transactions refs | payment providers, BIL-001 | opérations idempotentes; queue/reconciliation; jamais double débit |
| YD-MS-MKT-001 Learning Marketplace | C,N/I opérateurs,M2M | EDGE,INT | AUTH | C1 | listings commerciaux, orders, états | LRN, BIL-002, MOD | consultation possible; nouvelle commande suspendue si billing/entitlement critique absent |
| YD-MS-SPN-001 Sponsored Placement | C annonceurs,I,M2M | EDGE,INT | AUTH | C2 | campagnes, placements, budget refs, deliveries | BIL-002, MOD, surfaces | sponsoring supprimé du rendu en panne; ranking organique inchangé |
| YD-MS-DPR-001 Data Product | C org autorisée,I,M2M | EXT,INT | AUTH | C1 | releases datasets, licences, privacy status, manifests | ANL/DAT, BIL, CNS | accès fail-closed si licence/privacy/entitlement non vérifiable |
| YD-MS-INT-001 Intelligence Product | C org autorisée,I,M2M | EXT/EDGE,INT | AUTH | C1 | briefs/éditions, evidence refs, accès produit | ANL,LAB,KNW,BIL | dernière édition autorisée; génération nouvelle suspendue si evidence insuffisante |
| YD-MS-MOD-001 Moderation | C/N signalement,I,M2M | INT/EDGE signalement | AUTH | C1 | policies, dossiers, décisions | CNT,COM,MKT,SPN,AUD | objet explicitement bloqué reste fail-closed; décisions en queue vers owners |
| YD-MS-CFG-001 Country Configuration | I,M2M | INT | AUTH | C1 | pays, territoires, langues, monnaies, bindings cadres | Country Frameworks | lecture dernière config; nouvelles écritures dépendantes gelées si config absente |
| YD-MS-CNS-001 Consent & Privacy | C,I,M2M | EDGE,INT | AUTH | C1 | grants, restrictions, purposes, demandes privacy, retention rules | Identity, CFG/legal | fail-closed pour traitement non indispensable; révocation prioritaire |

## Composants plateforme

| Boundary | Realms | Expo | Backup | Crit. | Données / rôle | Dépendances | Mode dégradé |
|---|---|---|---|---|---|---|---|
| YD-PLT-AI-001 AI Gateway | C/N/I selon use case,M2M | EDGE,INT | MIXED | C1 | policies, request metadata, routing refs; pas de vérité métier | BRENDOLYS Identity, CNS, AI-002/003, modèles approuvés | refuse usage si policy/consent/model approval requis non vérifiable |
| YD-PLT-MLP-001 Model Lifecycle & Registry | I,M2M | INT | AUTH | C1 | modèles refs, versions, évaluations, approvals, deployments | AI, artefact/model storage | dernier modèle approuvé continue si sûr; nouveau déploiement bloqué en panne |
| YD-PLT-API-001 External API Management | C org/API clients,I,M2M | EXT | MIXED | C1 | clients API, quotas techniques, usage counters; aucune donnée métier autoritative | Identity, BIL entitlements, services exposés | fail-closed auth/entitlement; throttling; isolation d’un backend défaillant |
| YD-PLT-AUD-001 Audit & Trace | I sécurité,M2M producteurs | INT | AUTH append-only | C1 | trail, preuves, corrélation; pas d’ownership métier | tous producteurs sensibles | buffer/retry durable; actions classées peuvent être bloquées si audit obligatoire indisponible |

## Profils candidats différés

Ces frontières n’ont pas de ressources dédiées avant ADR d’extraction.

| Boundary | Profil candidat |
|---|---|
| YD-MS-CAR-004 Career Simulation | C/I/M2M; données de scénarios sensibles; compute-heavy; backup des scénarios autoritatifs seulement; extraction si scaling/modèles/SLO distincts |
| YD-MS-LAB-003 Labor Forecasting | I/M2M; datasets et modèles versionnés; outputs agrégés; séparation lorsque forecasting industrialisé |
| YD-PLT-AI-004 AI Orchestration | M2M/I; état workflow durable seulement si orchestration complexe; extraction lorsque plusieurs workflows/outils/modèles imposent lifecycle propre |

## Exigences communes injectées dans chaque profil

Chaque ligne ci-dessus hérite obligatoirement de : repo propre, artefact immuable, CI/CD propre, datastore/schema/credentials privés si persistant, migrations privées, namespace secrets, identité machine, certificats, deny-by-default réseau, TLS, logs/métriques/traces, audit selon classe, health/readiness, timeouts, retry idempotent, quotas selon exposition, scaling indépendant, rollback, runbook, DR, rétention, suppression et decommission.

## DNS

- chaque frontière confirmée reçoit un nom DNS interne stable dérivé de son Physical Boundary ID
- aucun DNS public par défaut
- `EDGE` et `EXT` décrivent une exposition logique via edge/API management; ils ne créent pas automatiquement un sous-domaine public par microservice
- tout sous-domaine public individuel exige une ADR et une justification produit/sécurité

## Backup et restauration

`AUTH` exige backup et restauration indépendants. `DERIVED` privilégie reconstruction depuis sources et watermarks, avec backup seulement si son coût de reconstruction ou son SLO le justifie. `MIXED` sépare strictement état autoritatif et projections reconstruisibles.

## IAM

Chaque frontière doit encore figer son `audience`, ses clients OIDC, scopes, rôles et claims dans le Contract Registry/IAM matrix. Les realms listés ici définissent uniquement les populations admissibles. L’accès `I` ne signifie jamais accès administratif universel.

## Gates restant à fermer avant production

Pour chacune des 51 frontières : owner humain/équipe et suppléant, repository final, classe runtime, moteur datastore, politique de migration, valeurs RPO/RTO/SLO, fréquence/rétention backup, preuve de restore, audience/scopes/roles, flux réseau exacts, quotas, rate limits, dashboards/alertes, stratégie de déploiement/rollback, cadence DR, rétention et ADR ouverts.

Ces champs restent ouverts volontairement : ils nécessitent la phase d’architecture physique, de capacity planning, de sécurité détaillée ou le Contract Registry. Ils ne doivent pas être remplacés par des valeurs arbitraires.