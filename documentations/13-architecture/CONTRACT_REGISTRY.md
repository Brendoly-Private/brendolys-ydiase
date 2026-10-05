# Contract Registry canonique — BRENDOLYS YDIASE

Statut : `D3-CANONICAL-CONTRACT-REGISTRY / LOGICAL-CONTRACTS-DEFINED / PHYSICAL-SCHEMAS-PENDING`

## 1. Objet

Source canonique des contrats inter-frontières de BRENDOLYS YDIASE. Ce registre consolide Dependency Map, Event Map, décisions D3 et politiques microservices sans imposer broker, HTTP/gRPC, topic, DNS ou Schema Registry.

Chaque contrat fixe : ID stable, owner, consumers, type, version, autorité, données minimales, Privacy, idempotence, replay, compatibilité et criticité.

## 2. Règles normatives

### Types
`API`, `EVENT`, `PROJECTION`, `HYBRID`, `JOB`, `AUDIT`.

### États
- `ACTIVE-LOGICAL` : contrat logique canonique.
- `DERIVED-SOURCE` : source obligatoire/candidate de reconstruction DERIVED.
- `DEFERRED` : dépend d'une frontière non extraite.
- `SUPERSEDED` : interdit aux nouvelles implémentations.

### Criticité contractuelle
- `K1` : autorisation/révocation, commande ou décision sensible, finance, sécurité, retrait critique.
- `K2` : fonction métier importante, dégradation contrôlée.
- `K3` : enrichissement/expérience reconstruisible.

K1/K2/K3 ne remplacent pas C1/C2/C3 des services.

### Compatibilité v1
Ajout optionnel compatible. Suppression/renommage/changement de type ou de sémantique d'un champ requis = incompatible et nouvelle version majeure. Nouvelle valeur enum exige `UNKNOWN/UNSUPPORTED`. Aucun changement silencieux de sens. Coexistence/dépréciation mesurée avant retrait. Un consommateur incompatible refuse/quarantaine au lieu d'interpréter librement.

### Privacy
`PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `SENSITIVE`, `VERY-SENSITIVE`, `CONTEXTUAL`.
Données personnelles : minimisation, purpose/finalité déterminable, chiffrement/contrôle d'accès selon contexte. Aucun secret/credential dans les contrats.

### Idempotence/replay
Tout EVENT/JOB possède `event_id/request_ref` ou clé métier stable. Les changements d'état utilisent version d'agrégat. Toute PROJECTION destinée à reconstruction expose snapshot/replay + watermark. DELETE/WITHDRAW/REVOKE doivent être représentables. Replay ne répète jamais aveuglément paiement, notification, décision ou commande externe.

## 3. Contrats transversaux

| ID | Owner → Consumers | Type | Autorité / données minimales | Privacy | Idemp./Replay | Crit. | État |
|---|---|---|---|---|---|---|---|
| YD-CTR-IDN-SUBJECT-v1 | IDN → PRF/SKL/ASM/ORI/APP/COM | HYBRID | IDN; IdentityRef, subject/account status | SENSITIVE-min | subject+version; snapshot/catch-up | K1 | ACTIVE-LOGICAL |
| YD-CTR-CNS-PRIVACY-DECISION-v1 | CNS → traitements personnels | HYBRID | CNS; purpose/grant/restriction/retention/decision version | VERY-SENSITIVE | grant/decision+version; revoke replay prioritaire | K1 | ACTIVE-LOGICAL |
| YD-CTR-CFG-COUNTRY-CONFIG-v1 | CFG → domaines | PROJECTION | CFG; country/territory/language/currency/framework/local params | INTERNAL/PUBLIC | config+version; snapshot/catch-up | K1 | ACTIVE-LOGICAL |
| YD-CTR-AUD-GOVERNED-EVENT-v1 | services sensibles → AUD | AUDIT | producteur pour fait, AUD pour trail; actor/action/object/outcome/trace | CONTEXTUAL | event_id; append-only/replay sans effet | K1 | ACTIVE-LOGICAL |
| YD-CTR-NTF-REQUEST-v1 | domaines → NTF | EVENT | demandeur; recipient/template/object/priority/purpose | SENSITIVE-min | request_ref; replay sans double envoi | K2 | ACTIVE-LOGICAL |
| YD-CTR-NTF-DELIVERY-v1 | NTF → demandeur/ANL autorisé | EVENT | NTF; request/channel/status/attempt/delivered_at | SENSITIVE-min | request+channel+attempt | K2 | ACTIVE-LOGICAL |

## 4. Profil, éducation, compétences et carrière

| ID | Owner → Consumers | Type | Autorité / données minimales | Privacy | Idemp./Replay | Crit. | État |
|---|---|---|---|---|---|---|---|
| YD-CTR-PRF-CURRENT-PROFILE-v1 | PRF-001 → ORI/REC/CAR/CNT Feed | PROJECTION | PRF-001; goals/preferences/constraints + source version | VERY-SENSITIVE | subject+version; snapshot/catch-up | K1 | ACTIVE-LOGICAL |
| YD-CTR-PRF-HISTORY-v1 | PRF-002 → SKL/ORI/REC/OPP/CAR | PROJECTION | PRF-002; education/experience/evidence refs + versions | VERY-SENSITIVE | subject+history version; snapshot/catch-up | K1 | ACTIVE-LOGICAL |
| YD-CTR-EDU-INSTITUTION-v1 | EDU-001 → EDU-002/consumers | HYBRID | EDU-001; institution/campus/status/version | PUBLIC/INTERNAL | ref+version | K2 | ACTIVE-LOGICAL |
| YD-CTR-EDU-PROGRAM-v1 | EDU-002 → EDU-003/consumers | HYBRID | EDU-002; program/version/status | PUBLIC/INTERNAL | ref+version | K2 | ACTIVE-LOGICAL |
| YD-CTR-EDU-CURRICULUM-v1 | EDU-003 → EDU-002/SKL | EVENT/PROJECTION | EDU-003; curriculum/module/version/coverage assertions | PUBLIC/INTERNAL | curriculum+version; replay | K2 | ACTIVE-LOGICAL |
| YD-CTR-EDU-QUALIFICATION-v1 | EDU-004 → EDU/PRF/CAR | PROJECTION | EDU-004; qualification/level/equivalence/prerequisite/version | PUBLIC/INTERNAL | ref+version; snapshot | K2 | ACTIVE-LOGICAL |
| YD-CTR-SKL-TAXONOMY-v1 | SKL-001 → EDU/SKL-002/CAR/LRN | PROJECTION | SKL-001; SkillRef/concept/relations/taxonomy version | PUBLIC/INTERNAL | taxonomy+version; snapshot | K2 | ACTIVE-LOGICAL |
| YD-CTR-SKL-USER-SKILLS-v1 | SKL-002 → ORI/REC/OPP/CAR | PROJECTION | SKL-002; skill/level/evidence/confidence/freshness/version | VERY-SENSITIVE | subject+version; correction replay | K1 | ACTIVE-LOGICAL |
| YD-CTR-CAR-OCCUPATION-v1 | CAR-001 → CAR-002/ORI/REC/LAB | PROJECTION | CAR-001; occupation/requirements/career edges/version | PUBLIC/INTERNAL | occupation+version; snapshot | K2 | ACTIVE-LOGICAL |
| YD-CTR-CAR-TRANSITION-v1 | CAR-002 → ORI/REC | PROJECTION | CAR-002; path/gaps/constraints/scenario assumptions/version | SENSITIVE | run/path+version | K2 | ACTIVE-LOGICAL |

## 5. Assessment, orientation, recommendation et matching

| ID | Owner → Consumers | Type | Autorité / données minimales | Privacy | Idemp./Replay | Crit. | État |
|---|---|---|---|---|---|---|---|
| YD-CTR-ASM-RESULT-v1 | ASM → ORI/REC | EVENT/PROJECTION | ASM; result/dimensions/method/version/validity/confidence | VERY-SENSITIVE | result_ref+version | K1 | ACTIVE-LOGICAL |
| YD-CTR-ORI-REC-REQUEST-v1 | ORI → REC | JOB | ORI pour cas; case/objective/constraints/input versions/request_ref | VERY-SENSITIVE | request_ref; retry idempotent | K1 | ACTIVE-LOGICAL |
| YD-CTR-REC-ORI-RESULT-v1 | REC → ORI | EVENT | REC; run/set/items/organic scores/explanations/evidence snapshot | VERY-SENSITIVE | request_ref+run_ref; immutable run | K1 | ACTIVE-LOGICAL |
| YD-CTR-REC-PROJECTION-v1 | REC → module comparaison ORI | PROJECTION | REC; item refs/scores/explanations/run version | VERY-SENSITIVE | run_ref+version | K2 | ACTIVE-LOGICAL |
| YD-CTR-OPP-MATCH-RESULT-v1 | OPP-002 → EMP-002/UI autorisée | EVENT | OPP-002; match/subject/opportunity/score/explanation/input versions | VERY-SENSITIVE | match_ref | K1 | ACTIVE-LOGICAL |

## 6. Opportunités, candidature et recrutement

| ID | Owner → Consumers | Type | Autorité / données minimales | Privacy | Idemp./Replay | Crit. | État |
|---|---|---|---|---|---|---|---|
| YD-CTR-EMP-EMPLOYER-v1 | EMP-001 → OPP/EMP-002/SRH/ANL | PROJECTION | EMP-001; employer/verification/status/version | PUBLIC/INTERNAL | ref+version | K2 | ACTIVE-LOGICAL |
| YD-CTR-OPP-OPPORTUNITY-v1 | OPP-001 → OPP-002/APP/SRH/REC | HYBRID | OPP-001; opportunity/employer/requirements/status/validity/version | PUBLIC/INTERNAL | ref+version; expire/withdraw replay | K1 | ACTIVE-LOGICAL |
| YD-CTR-APP-APPLICATION-v1 | APP → EMP-002/BFF/NTF/AUD | EVENT/PROJECTION | APP; application/status/opportunity/employer/version | VERY-SENSITIVE | application+state version | K1 | ACTIVE-LOGICAL |
| YD-CTR-EMP-RECRUITMENT-v1 | EMP-002 → APP/BFF/ANL | EVENT/PROJECTION | EMP-002; campaign/selection/application ref/decision/version | VERY-SENSITIVE | campaign/selection+version | K1 | ACTIVE-LOGICAL |

## 7. Data, provenance et marché du travail

| ID | Owner → Consumers | Type | Autorité / données minimales | Privacy | Idemp./Replay | Crit. | État |
|---|---|---|---|---|---|---|---|
| YD-CTR-PRT-SOURCE-RIGHTS-v1 | PRT → DAT-001/AMB/BFF | PROJECTION | PRT; agreement/status/role/access scope/effective_at | CONFIDENTIAL | agreement+version; revoke priority | K1 | ACTIVE-LOGICAL |
| YD-CTR-DAT-SOURCE-POLICY-v1 | DAT-001 → DAT-002/003/004 | HYBRID | DAT-001; source/rights/territory/access/validity | CONFIDENTIAL | source+version | K1 | ACTIVE-LOGICAL |
| YD-CTR-DAT-ACQUISITION-v1 | DAT-002 → DAT-003/004 | EVENT | DAT-002; raw ref/batch/source/hash/classification | CONTEXTUAL | record_ref or source+hash | K2 | ACTIVE-LOGICAL |
| YD-CTR-DAT-PROVENANCE-v1 | DAT-003 → DAT-004/domaines/KNW | PROJECTION | DAT-003; lineage/evidence/source chain/version | CONTEXTUAL | assertion+lineage version; replay | K1 | ACTIVE-LOGICAL |
| YD-CTR-DAT-QUALITY-v1 | DAT-004 → domaines | EVENT/PROJECTION | DAT-004; validation/decision/quality/anomalies/provenance | CONTEXTUAL | validation_ref | K1 | ACTIVE-LOGICAL |
| YD-CTR-DAT-REFERENCE-v1 | DAT-005 → CFG/EDU/SKL/CAR/LAB/ANL | PROJECTION | DAT-005; dataset/version/scope/effective_at | PUBLIC/INTERNAL | dataset+version; snapshot | K2 | ACTIVE-LOGICAL |
| YD-CTR-LAB-SIGNALS-v1 | LAB-001 → LAB-002/CAR/REC/KNW/ANL | EVENT/PROJECTION | LAB-001; signal/type/occupation-skill/territory/time/confidence/provenance | INTERNAL/AGGREGATED | signal+version; retraction replay | K2 | ACTIVE-LOGICAL |
| YD-CTR-LAB-INTELLIGENCE-v1 | LAB-002 → REC/CAR/ANL/INT | PROJECTION | LAB-002; indicator/territory/period/value/method/freshness | INTERNAL/AGGREGATED | indicator+period+version | K2 | ACTIVE-LOGICAL |
| YD-CTR-LAB-FORECAST-v1 | LAB-003 → CAR/ORI/REC/INT | PROJECTION | LAB-003; forecast/scope/horizon/scenario/model/confidence | INTERNAL | forecast+version; invalidation replay | K2 | DEFERRED |

## 8. Contenu, communauté, learning et gouvernance

| ID | Owner → Consumers | Type | Autorité / données minimales | Privacy | Idemp./Replay | Crit. | État |
|---|---|---|---|---|---|---|---|
| YD-CTR-CNT-CONTENT-v1 | CNT-001 → Feed/SRH/MOD/KNW | EVENT/PROJECTION | CNT-001; content/author/taxonomy/visibility/version | PUBLIC/SENSITIVE-min | ref+version; retire replay | K2 | ACTIVE-LOGICAL |
| YD-CTR-COM-ACTIVITY-v1 | COM → Feed/MOD | EVENT | COM; activity/actor/object/type/visibility | SENSITIVE-min | activity_ref | K2 | ACTIVE-LOGICAL |
| YD-CTR-MOD-DECISION-v1 | MOD → CNT/COM/MKT/SPN/AUD | EVENT | MOD; case/object/decision/effect/policy version | SENSITIVE | case+decision version; priority replay | K1 | ACTIVE-LOGICAL |
| YD-CTR-LRN-RESOURCE-v1 | LRN → SRH/REC/MKT/KNW | EVENT/PROJECTION | LRN; resource/provider/skills/availability/version | PUBLIC/INTERNAL | ref+version; withdraw replay | K2 | ACTIVE-LOGICAL |
| YD-CTR-AMB-SUBMISSION-v1 | AMB → DAT-002 | EVENT | AMB; submission/mandate/source context/artifact refs | CONTEXTUAL | submission_ref | K2 | ACTIVE-LOGICAL |
| YD-CTR-BFF-INSTITUTION-SUBMISSION-v1 | Institution BFF → DAT-002 | EVENT | BFF; institution/submitter/dataset/artifact refs | CONFIDENTIAL/SENSITIVE-min | submission_ref | K2 | ACTIVE-LOGICAL |
| YD-CTR-ADMIN-COMMAND-v1 | Admin plane ↔ domaine cible | JOB | domaine cible reste autorité; case/command/actor/reason/outcome | VERY-SENSITIVE | command_ref; effet idempotent | K1 | ACTIVE-LOGICAL |

## 9. Contrats DERIVED — reconstruction obligatoire

| ID | Owner → Consumer | Type | Données minimales / autorité | Privacy | Replay | Crit. | État |
|---|---|---|---|---|---|---|---|
| YD-CTR-EDU-SEARCHABLE-v1 | EDU → SRH | PROJECTION | objets publiables + source/version/visibility/language/territory | PUBLIC/INTERNAL | snapshot + catch-up + delete | K2 | DERIVED-SOURCE |
| YD-CTR-CAR-SEARCHABLE-v1 | CAR → SRH | PROJECTION | objets carrière publiables + version/visibility | PUBLIC/INTERNAL | snapshot + catch-up + withdraw | K2 | DERIVED-SOURCE |
| YD-CTR-OPP-SEARCHABLE-v1 | OPP → SRH | PROJECTION | opportunity/status/validity/version | PUBLIC/INTERNAL | snapshot + expire/withdraw | K1 | DERIVED-SOURCE |
| YD-CTR-CNT-SEARCHABLE-v1 | CNT → SRH | PROJECTION | contenu publiable/visibility/version | PUBLIC | snapshot + unpublish/delete | K2 | DERIVED-SOURCE |
| YD-CTR-LRN-SEARCHABLE-v1 | LRN → SRH | PROJECTION | resource/availability/version | PUBLIC/INTERNAL | snapshot + withdraw/retire | K2 | DERIVED-SOURCE |
| YD-CTR-KNW-SRH-SEARCH-ENRICHMENT-v1 | KNW → SRH | PROJECTION | graph version/source refs/provenance/confidence/freshness | INTERNAL | snapshot/catch-up/delete/revoke | K3 | DERIVED-SOURCE |
| YD-CTR-CNT-FEEDABLE-v1 | CNT → CNT-002 | PROJECTION | content/visibility/version | PUBLIC/INTERNAL | snapshot + retire | K3 | DERIVED-SOURCE |
| YD-CTR-COM-FEED-SIGNALS-v1 | COM → CNT-002 | EVENT/PROJECTION | authorized engagement/activity signals | SENSITIVE-min | event id + rebuild window | K3 | DERIVED-SOURCE |
| YD-CTR-MOD-CONTENT-DECISION-v1 | MOD → CNT-002 | PROJECTION | object/effect/policy version | SENSITIVE-min | priority revoke/block replay | K1 | DERIVED-SOURCE |
| YD-CTR-SPN-PLACEMENT-v1 | SPN → delivery/feed | PROJECTION | sponsored placement explicitly labeled; no organic score fields | COMMERCIAL | placement+version | K2 | DERIVED-SOURCE |
| YD-CTR-EDU-KNOWLEDGE-v1 | EDU → KNW | PROJECTION | stable IDs/versions/semantic relations/provenance refs | PUBLIC/INTERNAL | snapshot/catch-up/delete | K2 | DERIVED-SOURCE |
| YD-CTR-SKL-KNOWLEDGE-v1 | SKL-001 → KNW | PROJECTION | taxonomy concepts/relations/version | PUBLIC/INTERNAL | snapshot/catch-up/delete | K2 | DERIVED-SOURCE |
| YD-CTR-CAR-KNOWLEDGE-v1 | CAR → KNW | PROJECTION | occupations/relations/version | PUBLIC/INTERNAL | snapshot/catch-up/delete | K2 | DERIVED-SOURCE |
| YD-CTR-LAB-KNOWLEDGE-v1 | LAB → KNW | PROJECTION | governed signals/indicators/territory/version | INTERNAL/AGGREGATED | snapshot/catch-up/retract | K2 | DERIVED-SOURCE |
| YD-CTR-<DOMAIN>-ANALYTICS-v1 | domaine enregistré → ANL-001 | PROJECTION | facts/dimensions/timestamps/versions + metric-purpose binding | CONTEXTUAL | snapshot/catch-up/delete/revoke | K2 | DERIVED-SOURCE |
| YD-CTR-SRH-RETRIEVAL-v1 | SRH → AI-002 | PROJECTION/API | authorized search documents/source refs/versions/access labels | CONTEXTUAL | index watermark + rebuild | K2 | DERIVED-SOURCE |
| YD-CTR-KNW-GROUNDING-v1 | KNW → AI-002 | PROJECTION/API | graph facts/relations/provenance/confidence/version | INTERNAL | graph watermark + rebuild | K2 | DERIVED-SOURCE |
| YD-CTR-CNS-CORPUS-AUTHORIZATION-v1 | CNS → AI-002 | API/PROJECTION | purpose/corpus authorization/restrictions/decision version | VERY-SENSITIVE | decision+version; revoke priority | K1 | DERIVED-SOURCE |

## 10. Analytics et produits

| ID | Owner → Consumers | Type | Autorité / données minimales | Privacy | Idemp./Replay | Crit. | État |
|---|---|---|---|---|---|---|---|
| YD-CTR-ANL-SNAPSHOT-v1 | ANL-001 → ANL-002/003/INT/DPR | PROJECTION/EVENT | ANL; snapshot/metrics/scope/period/method/freshness | CONTEXTUAL/AGGREGATED | snapshot_ref; rebuildable | K2 | ACTIVE-LOGICAL |
| YD-CTR-ANL-INSTITUTION-INSIGHT-v1 | ANL-002 → institution surface/INT/API | EVENT/PROJECTION | ANL-002; insight/institution/period/metrics/version | CONFIDENTIAL/AGGREGATED | insight+version | K2 | ACTIVE-LOGICAL |
| YD-CTR-ANL-EMPLOYER-INSIGHT-v1 | ANL-003 → employer surface/INT/API | EVENT/PROJECTION | ANL-003; insight/employer/period/metrics/version | CONFIDENTIAL/AGGREGATED | insight+version | K2 | ACTIVE-LOGICAL |
| YD-CTR-DPR-RELEASE-v1 | DPR → API/BIL/clients autorisés | EVENT/API | DPR; release/schema/license/privacy/source snapshots | GOVERNED | release_ref immutable | K1 | ACTIVE-LOGICAL |
| YD-CTR-INT-EDITION-v1 | INT → API/BIL/clients | EVENT/API | INT; product/edition/scope/period/evidence/access class | CONTEXTUAL | edition_ref+version | K1 | ACTIVE-LOGICAL |

## 11. Économie et sponsoring

| ID | Owner → Consumers | Type | Autorité / données minimales | Privacy | Idemp./Replay | Crit. | État |
|---|---|---|---|---|---|---|---|
| YD-CTR-BIL-ENTITLEMENT-v1 | BIL-001 → services protégés/API | HYBRID | BIL-001; subscription/entitlement/capability/quota/state/effective_at | CONFIDENTIAL/PII-min | entitlement+version; revoke priority | K1 | ACTIVE-LOGICAL |
| YD-CTR-BIL-BILLING-v1 | BIL-002 → BIL-001/MKT/SPN | EVENT | BIL-002; account/object/state/amount/currency/provider transaction | FINANCIAL-SENSITIVE | provider transaction + event_id | K1 | ACTIVE-LOGICAL |
| YD-CTR-MKT-ORDER-v1 | MKT → BIL-002/LRN/NTF | EVENT | MKT; order/customer/listing/state/commercial terms | FINANCIAL/SENSITIVE-min | order+version | K1 | ACTIVE-LOGICAL |
| YD-CTR-SPN-CAMPAIGN-v1 | SPN → BIL/MOD/delivery | EVENT/PROJECTION | SPN; campaign/advertiser/state/scope/budget ref | COMMERCIAL-CONFIDENTIAL | campaign+version | K2 | ACTIVE-LOGICAL |
| YD-CTR-SPN-DELIVERY-v1 | SPN → BIL/ANL | EVENT | SPN; delivery/campaign/placement/time/billable unit | COMMERCIAL | delivery_ref | K2 | ACTIVE-LOGICAL |
| YD-CTR-API-USAGE-v1 | API platform → BIL/ANL/AUD | EVENT | API; client/product/units/bucket/technical quota state | CONFIDENTIAL | client+product+bucket+sequence | K2 | ACTIVE-LOGICAL |

Règle absolue : aucun contrat SPN/BIL commercial n'entre dans le score organique REC, OPP Matching ou Search.

## 12. IA et modèles

| ID | Owner → Consumers | Type | Autorité / données minimales | Privacy | Idemp./Replay | Crit. | État |
|---|---|---|---|---|---|---|---|
| YD-CTR-MLP-MODEL-LIFECYCLE-v1 | MLP → AI Gateway/AI orchestration | EVENT/PROJECTION | MLP; model/version/approval/deployment/endpoint/capabilities | CONFIDENTIAL-TECH | model+version; retirement priority | K1 | ACTIVE-LOGICAL |
| YD-CTR-AI-GROUNDED-RETRIEVAL-v1 | AI Gateway/orchestration → AI-002 | API/JOB | caller policy; query/access/purpose/task; AI-002 owns bundle | VERY-SENSITIVE-CONTEXTUAL | request_ref | K1 | ACTIVE-LOGICAL |
| YD-CTR-AI-VERIFICATION-v1 | AI workflow → AI-003 → caller | JOB | AI-003; output claims/grounding/model-run → verdict/confidence/fail refs | SENSITIVE/CONTEXTUAL | verification_ref | K1 | ACTIVE-LOGICAL |
| YD-CTR-AI-ORCHESTRATION-v1 | AI Gateway ↔ AI-004 | JOB | Gateway policy; request/purpose/capability/model scope → run/output refs | VERY-SENSITIVE-CONTEXTUAL | request/run ref | K1 | DEFERRED |

Tant que AI-004 n'est pas extrait par ADR, son contrat reste `DEFERRED` et l'orchestration minimale appartient au composant AI Gateway sans créer une fausse frontière physique.

## 13. Contrats superseded / interdits

| ID | Statut | Remplacement |
|---|---|---|
| YD-CTR-REC-002-* | SUPERSEDED | utiliser APP-001 / `YD-CTR-APP-APPLICATION-v1` |

Aucun nouveau contrat ne doit utiliser REC-002 pour Application.

## 14. Matérialisation EVENT_MAP

Les IDs `EVT-*` existants restent des **événements candidats** rattachés aux familles contractuelles ci-dessus. Ils ne remplacent pas l'ID `YD-CTR-*`.

Exemples :
- EVT-OPP-001/002/003 → `YD-CTR-OPP-OPPORTUNITY-v1`
- EVT-APP-001/002 → `YD-CTR-APP-APPLICATION-v1`
- EVT-DAT-004 → `YD-CTR-DAT-PROVENANCE-v1`
- EVT-DAT-005/006/007 → `YD-CTR-DAT-QUALITY-v1`
- EVT-LAB-001/002 → `YD-CTR-LAB-SIGNALS-v1`
- EVT-ORI-002 + EVT-REC-001/002 → request/result ORI↔REC
- EVT-MOD-001 → `YD-CTR-MOD-DECISION-v1`
- EVT-BIL-001/002 → `YD-CTR-BIL-ENTITLEMENT-v1`
- EVT-BIL-003/004 → `YD-CTR-BIL-BILLING-v1`.

Le futur schéma physique doit déclarer explicitement `contract_id`, `contract_version`, `message/event_id`, `occurred_at`, owner et classification.

## 15. Gates avant PHYSICAL-READY

Pour chaque contrat utilisé au pilote :
1. schéma physique enregistré ;
2. producer et consumers physiques nommés ;
3. authn/authz/scopes/audience fermés ;
4. Privacy/purpose/tenant enforcement testé ;
5. stratégie idempotence testée ;
6. retry/DLQ/quarantaine définis ;
7. compatibilité backward/forward testée ;
8. SLO propagation/freshness/retrait défini ;
9. rétention ou snapshot compatible avec recovery ;
10. contract tests CI ;
11. observabilité et ownership opérationnel ;
12. procédure de dépréciation/rollback.

Pour DERIVED : FULL_REBUILD + convergence restent obligatoires avant production.

## 16. Contrôle de couverture

### Couvert
- identité/profile/privacy/config/audit ;
- EDU/SKL/CAR ;
- ASM/ORI/REC ;
- OPP/APP/EMP ;
- DAT/LAB ;
- CNT/COM/LRN/MOD ;
- PRT/AMB/BFF/admin/notification ;
- Search/Feed/KNW/Analytics/AI-002 sources DERIVED ;
- Analytics produits ;
- Billing/Marketplace/Sponsoring/API ;
- Data/Intelligence Products ;
- Model lifecycle/AI verification/orchestration.

### À détailler lors des fermetures de domaine
Les contrats `YD-CTR-<DOMAIN>-ANALYTICS-v1` sont une famille paramétrée : ANL-001 devra enregistrer une entrée concrète par métrique/source autorisée. Les contrats AI seront approfondis lors de la fermeture AI. Les valeurs numériques de rétention/SLO/compatibilité restent PREPROD.

## 17. Verdict

`CONTRACT-REGISTRY-BASELINE-ESTABLISHED`.

Les contrats logiques inter-frontières disposent désormais d'un registre canonique. La prochaine dette n'est plus l'identification des familles : elle est la **matérialisation des schémas physiques, contract tests, SLO et preuves de replay/rebuild**.

Ce registre n'autorise pas la production à lui seul.
