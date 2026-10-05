# Authoritative Source Registry — BRENDOLYS YDIASE

Statut : `ACTIVE-D3-CANDIDATE`

## 1. Principe

Ce registre distingue l'owner métier d'une donnée, sa frontière physique D3 candidate et les copies autorisées. Une frontière `STABLE-CANDIDATE` n'est pas irrévocable : la revue des dossiers métier peut la rouvrir par analyse d'impact.

BRENDOLYS Identity est autoritatif pour l'identité d'authentification. Il n'est pas owner des profils métier YDIASE.

| Type/agrégat | Owner métier | Frontière/système autoritatif D3 | Copies/projections permises | Règle |
|---|---|---|---|---|
| Identité d'authentification | BRENDOLYS Identity | IAM externe Brendolys | claims minimaux dans tokens/caches bornés | pas de mot de passe dans YDIASE |
| Profil utilisateur | Profiles | `YD-MS-PRF-001` | projections minimales autorisées | accès par contrat, pas DB directe |
| Formation/institution | Education | `YD-MS-EDU-*` selon agrégat | Search, Knowledge, Analytics, orientation | publication/version source |
| Compétence/référentiel | Skills | `YD-MS-SKL-*` selon agrégat | Knowledge, Search, recommendation | version/provenance conservées |
| Métier/carrière | Careers | `YD-MS-CAR-*` selon agrégat | Search, Knowledge, orientation | contrats versionnés |
| Évaluation utilisateur | Assessment | `YD-MS-ASM-001` | résultats minimaux vers orientation/recommendation | finalité et accès contrôlés |
| Dossier/plan d'orientation | Orientation | `YD-MS-ORI-001` | projections nécessaires aux recommandations | historique/version métier |
| Recommandation métier | Recommendation | `YD-MS-REC-001` pour états autoritatifs; sous-parties dérivées séparées | vues utilisateur/analytics autorisés | ne pas confondre calcul dérivé et décision conservée |
| Données Labor autoritatives internes | Labor Market | `YD-MS-LAB-*` selon agrégat | analytics, knowledge, orientation | distinguer observation, estimation et méthodologie |
| Opportunité publiée | Opportunities | `YD-MS-OPP-*` | Search, Feed, Analytics | état de publication versionné |
| Candidature | Applications | `YD-MS-APP-001` | vues candidat/recruteur autorisées | donnée transactionnelle AUTH |
| Employeur/organisation emploi | Employment | `YD-MS-EMP-*` | Search/Analytics selon finalité | autorisation organisationnelle |
| Contenu éditorial | Content | `YD-MS-CNT-001` | Feed/Search/AI selon droits | modération/retrait propagés |
| Feed personnalisé | Content/Feed | `YD-MS-CNT-002` | cache/vues uniquement | DERIVED, reconstruisible |
| Communauté | Community | `YD-MS-COM-001` | Feed/modération/analytics bornés | privacy/modération |
| Ressource learning propre | Learning | `YD-MS-LRN-001` pour partie AUTH | Search/Feed/recommendation | partie DERIVED séparée |
| Notification et état de livraison | Notifications | `YD-MS-NTF-001` | observabilité/support bornés | provider externe non autoritatif du métier |
| Partenaire | Partnerships | `YD-MS-PRT-001` | vues internes autorisées | contrat/mandat |
| Ambassadeur/mandat réseau | Ambassadors | `YD-MS-AMB-001` | vues opérationnelles | realm networks ne remplace pas l'owner métier |
| Source/provenance/qualité Data | Data | `YD-MS-DAT-*` selon responsabilité | projections vers consommateurs | provenance conservée |
| Knowledge Graph | aucun owner métier primaire | `YD-MS-KNW-001` | graphe dérivé | DERIVED, jamais source unique |
| Analytics dérivés | aucun owner métier primaire | `YD-MS-ANL-001` | résultats analytiques gouvernés | DERIVED, sources/méthodes requises |
| Artefact analytique autoritatif | Analytics | `YD-MS-ANL-002/003` selon agrégat | consommateurs avec entitlement | séparer résultat dérivé et publication gouvernée |
| Corpus Retrieval/Grounding | aucun owner métier primaire | `YD-MS-AI-002` | index/corpus dérivé | DERIVED, droits et provenance |
| Preuve/vérification AI | AI Verification | `YD-MS-AI-003` | AI Gateway/audit | règles et evidence gouvernées |
| Entitlement | Billing/Entitlements | `YD-MS-BIL-001` | caches de décision bornés | backend reste responsable de l'autorisation métier |
| Paiement/ledger métier YDIASE | Billing | `YD-MS-BIL-002` | vues financières autorisées | idempotence et réconciliation |
| Commande marketplace | Marketplace | `YD-MS-MKT-001` | billing/analytics autorisés | transaction AUTH |
| Sponsoring/placement commercial | Sponsoring | `YD-MS-SPN-001` | Feed/placement explicite | séparé du ranking organique |
| Data Product Release/LicenseManifest | Data Products | `YD-MS-DPR-001` | consommateurs sous licence/entitlement | CNS décide privacy, DPR ne remplace pas les sources |
| Décision d'intégrité/evidence | Integrity | `YD-MS-INT-001` | services autorisés/audit | evidence traçable |
| Politique/décision de modération | Moderation | `YD-MS-MOD-001` | Content/Community/Feed | owner fonctionnel Moderation |
| Configuration métier globale | Configuration | `YD-MS-CFG-001` | consommateurs explicitement abonnés | pas de secrets dans config métier |
| Consentement/finalité/privacy decision | Consent & Privacy | `YD-MS-CNS-001` | décisions minimales vers consommateurs | fail-closed lorsque décision requise indisponible |
| Routage/policy AI plateforme | AI Platform | `YD-PLT-AI-001` pour metadata plateforme uniquement | runtime AI | jamais owner du contenu métier |
| Artefacts/modèles ML approuvés | ML Platform | `YD-PLT-MLP-001` | AI runtime | approval/version requis |
| Clients/configuration API externe | API Platform | `YD-PLT-API-001` pour metadata API uniquement | gateway/runtime | ne devient pas owner backend |
| Journal d'audit append-only | Audit Platform | `YD-PLT-AUD-001` | consultation conformité autorisée | producteur reste owner du fait métier audité |

## 2. Frontières à détailler lors des revues métier

Les lignes utilisant `YD-MS-EDU-*`, `YD-MS-SKL-*`, `YD-MS-CAR-*`, `YD-MS-LAB-*`, `YD-MS-OPP-*`, `YD-MS-EMP-*` ou `YD-MS-DAT-*` doivent être détaillées par agrégat lors de l'audit de leur domaine. Cette granularité n'est pas inventée dans le dossier 00.

## 3. Interdictions

- accès direct au datastore d'un autre owner
- promotion d'une projection DERIVED en source autoritative sans ADR et revue métier
- duplication d'une donnée personnelle sans finalité
- changement d'owner par simple contrat technique
