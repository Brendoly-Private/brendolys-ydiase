# Dependency Map D3 — BRENDOLYS YDIASE

Cette carte décrit les dépendances logiques entre bounded contexts. Elle ne prescrit ni Kafka, ni HTTP, ni gRPC, ni broker précis. Les choix physiques relèvent des ADR. Chaque relation porte un mode logique, une autorité, une attente de cohérence, un comportement de panne, une interdiction et un risque de cycle.

## Légende

- **SYNC/API** : lecture ou commande nécessitant une réponse immédiate.
- **ASYNC/EVT** : événement versionné propagé après changement autoritatif.
- **ASYNC/PROJ** : projection locale reconstruisible depuis une source autoritative.
- **HYBRID** : API pour validation/commande, événement ou projection pour lectures découplées.
- **Forte locale** : cohérence forte dans l’agrégat du producteur uniquement.
- **Éventuelle** : le consommateur tolère un décalage borné et ne réécrit pas la source.
- En panne, aucun consommateur ne devient owner de secours d’un agrégat externe.

## A. Identité, profil, consentement et configuration

| Producteur → consommateur | Données minimales | Mode | Contrat logique | Autorité | Cohérence | Panne | Dépendance interdite | Cycle |
|---|---|---|---|---|---|---|---|---|
| IDN-001 → PRF-001 | IdentityRef, account status | HYBRID | API + IdentityStatusChanged | IDN | éventuelle hors création | refuser création si identité inconnue; lecture profil dégradée possible | PRF ne crée/modifie pas Identity | faible |
| IDN-001 → PRF-002/SKL-002/ASM/ORI/APP/COM | IdentityRef, subject status | ASYNC/PROJ | IdentityProjection | IDN | éventuelle | suspendre action sensible si projection absente ou révoquée | consommateurs ne copient pas credentials | faible |
| PRF-001 → ORI/REC-001/ORI-002/CAR-002/003/004/CNT-002 | objectifs, préférences, contraintes autorisées | ASYNC/PROJ | ProfileProjection | PRF | éventuelle versionnée | utiliser dernière version valide ou demander rafraîchissement; jamais inventer | moteurs ne modifient pas Profile | moyen si PRF consomme leurs résultats |
| PRF-002 → SKL-002/ORI/REC-001/OPP-002/CAR | EducationRecord, ExperienceRecord, evidence refs | ASYNC/PROJ | ExperienceProjection | PRF-002 | éventuelle | résultat signalé incomplet si données indisponibles | aucun calculateur ne réécrit l’historique | faible |
| CNS-001 → tous traitements personnels | PurposeGrant, consent status, restrictions, retention | HYBRID | PrivacyDecision API + ConsentChanged | CNS | forte pour autorisation; éventuelle pour cache révocable | fail-closed pour traitement non indispensable; arrêt/queue selon finalité | aucun service n’interprète seul le consentement | faible |
| CFG-001 → domaines pays | country, territory, language, currency, framework binding, local parameters | ASYNC/PROJ | CountryConfigProjection | CFG | éventuelle versionnée | geler écriture dépendante si config requise absente; lectures connues possibles | domaine ne crée pas sa propre vérité pays | faible |
| AUD-001 ← services sensibles | actor, action, objectRef, timestamp, outcome, traceRef | ASYNC/EVT | AuditEvent | producteur pour fait; AUD pour trail | éventuelle durable | buffer/retry; action à criticité définie peut être bloquée si audit obligatoire | AUD ne commande pas les agrégats métier | faible |

## B. Éducation, compétences et carrières

| Producteur → consommateur | Données minimales | Mode | Contrat logique | Autorité | Cohérence | Panne | Dépendance interdite | Cycle |
|---|---|---|---|---|---|---|---|---|
| EDU-001 → EDU-002 | InstitutionRef, CampusRef, status | HYBRID | validation API + InstitutionChanged | EDU-001 | forte à création; éventuelle ensuite | interdire nouvelle offre sur institution inconnue; conserver versions existantes | Program ne modifie pas Institution | faible |
| EDU-002 → EDU-003 | ProgramRef, ProgramVersionRef, status | HYBRID | API + ProgramChanged | EDU-002 | forte à rattachement; éventuelle ensuite | curriculum draft possible, publication bloquée sans Program valide | Curriculum ne modifie pas Program | **élevé** si EDU-002 lit Curriculum transactionnellement |
| EDU-003 → EDU-002 | CurriculumRef publié, version, coverage summary | ASYNC/EVT | CurriculumPublished | EDU-003 | éventuelle | Program garde dernier ref publié | EDU-002 ne commande pas Curriculum dans sa transaction | **élevé maîtrisé** par sens événementiel |
| EDU-004 → EDU-002/PRF-002/CAR-001 | QualificationRef, level, equivalence/prerequisite refs | ASYNC/PROJ | QualificationProjection | EDU-004 | éventuelle versionnée | marquer qualification non résolue; publication selon règle pays | consommateurs ne maintiennent pas équivalences parallèles | faible |
| SKL-001 → EDU-003/SKL-002/CAR-001/LRN/RSH | SkillRef, KnowledgeConceptRef, taxonomy version | ASYNC/PROJ | SkillTaxonomyProjection | SKL-001 | éventuelle | conserver version précédente; bloquer nouveaux mappings inconnus | aucun consommateur ne crée un Skill canonique | moyen |
| EDU-003 → SKL-001 | module refs et assertions de couverture de compétence | ASYNC/EVT | CurriculumSkillEvidence | EDU-003 pour module; SKL pour Skill | éventuelle | mise à jour sémantique différée | SKL ne réécrit pas Curriculum | moyen, sans commande inverse |
| SKL-001 → CAR-001 | SkillRef, relations sémantiques | ASYNC/PROJ | SkillProjection | SKL | éventuelle | dernière version valide | CAR ne possède pas Skill | **moyen** |
| CAR-001 → SKL-001 | OccupationRef, skill-demand assertions | ASYNC/EVT | OccupationSkillEvidence | CAR pour occupation | éventuelle | enrichissement différé | SKL ne possède pas Occupation | **moyen maîtrisé** |
| SKL-002 → ORI/REC-001/OPP-002/CAR-002/003/004 | UserSkillRef, level, evidence status, version | ASYNC/PROJ | UserSkillProjection | SKL-002 | éventuelle | résultat incomplet/abstention selon seuil | moteurs ne mettent pas à jour UserSkill directement | faible |
| CAR-001 → CAR-002/003/004/ORI/REC/LAB | OccupationRef, requirements, career edges | ASYNC/PROJ | OccupationProjection | CAR-001 | éventuelle | dernière version ou résultat suspendu | dérivés ne réécrivent pas occupation | faible |
| CAR-002/003 → CAR-004 | paths, transition gaps, assumptions refs | ASYNC/PROJ | CareerScenarioInputs | CAR-002/003 | éventuelle | simulation indisponible ou partielle | simulation ne devient pas owner des plans sources | faible |

## C. Orientation, recommandation, évaluation et recherche

| Producteur → consommateur | Données minimales | Mode | Contrat logique | Autorité | Cohérence | Panne | Dépendance interdite | Cycle |
|---|---|---|---|---|---|---|---|---|
| ASM-001 → ORI/REC-001 | AssessmentResultRef, dimensions, validity, confidence | ASYNC/EVT + PROJ | AssessmentCompleted | ASM | éventuelle | orientation fonctionne sans assessment si règle le permet, sinon demande évaluation | ORI/REC ne modifient pas résultat | faible |
| ORI-001 → REC-001 | OrientationCaseRef, objective, constraints, eligible scope | SYNC/API ou ASYNC job | RecommendationRequest contract | ORI pour cas | cohérence de requête figée par version | queue/retry; présenter absence de résultat, jamais résultat fabriqué | REC ne modifie pas cas ORI | **moyen** si ORI attend REC |
| REC-001 → ORI-001 | RecommendationSetRef, ranked items, explanations, evidence snapshot | ASYNC/EVT ou réponse job | RecommendationCompleted | REC pour résultat | résultat immuable par run | ORI conserve run précédent explicitement daté ou attend | ORI ne recalcule pas le ranking comme vérité concurrente | **moyen maîtrisé** via job, pas appel circulaire |
| REC-001 → ORI-002 | RecommendationItem refs, scores/explanations | ASYNC/PROJ | RecommendationProjection | REC | éventuelle | comparaison possible sans score REC si critères autonomes | ORI-002 ne modifie pas ranking | faible |
| EDU/CAR/LAB → REC-001 | candidats, requirements, signaux/indicateurs autorisés | ASYNC/PROJ | RecommendationFeatureProjections | domaines sources | éventuelle avec snapshot versionné | abstention si fraîcheur sous seuil | REC ne requête pas en cascade tous les domaines à chaque calcul | faible |
| SRH-001 ← EDU/CAR/OPP/CNT/LRN | IDs, texte public, filtres, publication state | ASYNC/PROJ | SearchDocuments | domaines sources | éventuelle | recherche partielle; index reconstruisible | Search ne devient pas owner | faible |
| SRH-001 → applications/AI-002 | result refs, rank de recherche, index version | SYNC/API | SearchQuery | SRH pour index, domaine pour objet | éventuelle | fallback contrôlé ou indisponibilité | résultat Search ne vaut pas vérité métier | faible |

## D. Marché du travail, opportunités et recrutement

| Producteur → consommateur | Données minimales | Mode | Contrat logique | Autorité | Cohérence | Panne | Dépendance interdite | Cycle |
|---|---|---|---|---|---|---|---|---|
| DAT-002/003/004 → LAB-001 | raw observation ref, source, provenance, quality decision | ASYNC/EVT | ValidatedLaborObservation | DAT pour acquisition/preuve; LAB pour signal publié | éventuelle contrôlée | quarantaine si preuve/qualité insuffisante | LAB ne réécrit pas raw/provenance | faible |
| LAB-001 → LAB-002 | normalized signals, territory, occupation/skill refs, observedAt | ASYNC/EVT/PROJ | LaborSignalPublished | LAB-001 | éventuelle | indicateurs restent datés; recalcul différé | LAB-002 ne modifie pas signal | faible |
| LAB-002 → LAB-003 | indicator snapshots, series, methodology version | ASYNC/PROJ | LaborIntelligenceDataset | LAB-002 | éventuelle | forecast suspendu ou basé sur snapshot daté explicitement | Forecast ne corrige pas indicateur source | faible |
| EMP-001 → OPP-001/EMP-002/003 | EmployerRef, verification/status | ASYNC/PROJ | EmployerProjection | EMP-001 | éventuelle | publication sensible bloquée si employeur invalide | consommateurs ne modifient pas Employer | faible |
| OPP-001 → OPP-002/APP-001/SRH/REC-001 | OpportunityRef, requirements, status, validity | ASYNC/PROJ | OpportunityProjection | OPP-001 | éventuelle | matching/search ignorent opportunités expirées selon projection; candidature revalide en SYNC | aucun consommateur ne réécrit Opportunity | faible |
| OPP-002 ← PRF/SKL/OPP | refs profil, skills, opportunity requirements | ASYNC/PROJ | MatchInputSnapshot | sources respectives | éventuelle snapshot | match abstient si minimum manquant | OPP-002 ne devient pas recommandation générique | moyen avec REC-001 |
| OPP-002 → EMP-002/utilisateur | MatchRef, score, explanation, evidence version | ASYNC/EVT/PROJ | OpportunityMatchCompleted | OPP-002 | éventuelle | aucun match ancien présenté comme courant sans date | EMP-002 ne modifie pas score | faible |
| APP-001 → EMP-002/EMP-003/NTF | ApplicationRef, status, opportunity/employer refs | ASYNC/EVT | ApplicationStatusChanged | APP-001 | éventuelle | retries; UI affiche dernier état connu | Employer workspace ne maintient pas statut concurrent | faible |
| OPP-001 → APP-001 | OpportunityRef + application policy/status | HYBRID | projection + validation API à soumission | OPP-001 | forte au moment de soumettre | refuser/mettre en attente si opportunité non validable | APP ne réactive pas opportunité | faible |
| EMP-002 → APP-001 | candidate selection command, actor, campaign ref | SYNC/API | RecruitmentDecisionCommand | EMP-002 pour décision de recrutement; APP pour transition d’état | forte sur commande idempotente | retry idempotent, pas de double transition | EMP-002 n’écrit pas directement Application | faible |

## E. Contenu, communauté, learning, modération et notifications

| Producteur → consommateur | Données minimales | Mode | Contrat logique | Autorité | Cohérence | Panne | Dépendance interdite | Cycle |
|---|---|---|---|---|---|---|---|---|
| CNT-001 → CNT-002/SRH/MOD | ContentRef, publication state, taxonomy, author ref | ASYNC/PROJ | ContentProjection | CNT | éventuelle | contenu absent du feed/search jusqu’au rattrapage | Feed/Search ne modifient pas Content | faible |
| COM-001 → CNT-002/MOD | relation/reaction/comment refs, visibility state | ASYNC/EVT/PROJ | CommunityActivity | COM | éventuelle | feed sans signaux communautaires; modération rattrape | Feed ne modifie pas Community | faible |
| MOD-001 → CNT/COM/MKT/SPN | ModerationDecision, objectRef, effect, policyVersion | ASYNC/EVT + commande si retrait immédiat | ModerationDecisionIssued | MOD pour décision; domaine pour état objet | retrait critique rapidement convergent | fail-closed pour objet explicitement bloqué; retry commande | MOD ne modifie pas DB du domaine | **moyen** si domaine renvoie dossier à MOD; utiliser événements |
| LRN-001 ← EDU/SKL/MKT | resource refs, skill mappings, commercial availability | ASYNC/PROJ | LearningDiscoveryProjection | sources respectives; LRN pour ressource propre | éventuelle | masquer offre commerciale indisponible; conserver ressource non commerciale valide | LRN ne possède pas Program ou MarketplaceOrder | moyen |
| RSH-001 ← EDU/SKL/CAR/LAB | domain refs, knowledge concepts, labor signals/indicators | ASYNC/PROJ | ResearchTopicInputs | sources | éventuelle | génération/recommandation suspendue si seuil de preuve non atteint | RSH ne publie pas faits marché comme source | faible |
| services → NTF-001 | event type, recipientRef, template key, objectRef, priority | ASYNC/EVT | NotificationRequested | producteur pour événement; NTF pour livraison | éventuelle | retry/DLQ logique; événement métier reste valide sans notification sauf règle explicite | NTF ne commande pas transition métier | faible |
| CNS/PRF → NTF-001 | channel permission/preferences | ASYNC/PROJ | NotificationPreferenceProjection | CNS/PRF selon nature | éventuelle avec révocation prioritaire | fail-closed marketing; transactionnel selon base applicable | NTF ne devient pas owner des consentements | faible |

## F. Partenaires, ambassadeurs et workspaces

| Producteur → consommateur | Données minimales | Mode | Contrat logique | Autorité | Cohérence | Panne | Dépendance interdite | Cycle |
|---|---|---|---|---|---|---|---|---|
| PRT-001 → DAT-001/AMB/INS/EMP-003 | PartnerRef, agreement status, role, access scope | ASYNC/PROJ | PartnershipProjection | PRT | éventuelle | suspendre nouvelle ingestion/action si droit non vérifiable | consommateurs ne créent pas droits contractuels parallèles | moyen avec DAT-001 |
| DAT-001 → DAT-002 | SourceRef, usage rights, territory, access policy | HYBRID | SourcePolicy API + SourceChanged | DAT-001 | forte avant acquisition; éventuelle ensuite | acquisition bloquée si droit inconnu/révoqué | DAT-002 ne contourne pas registry | faible |
| AMB-001 → DAT-002 | AmbassadorRef, mandate, submission context | ASYNC/EVT/API submission | AmbassadorSubmission | AMB pour mandat; DAT-002 pour batch | validation forte du mandat à soumission | mise en attente si mandat non vérifiable | ambassadeur ne publie pas directement domaine métier | faible |
| INS-001 → DAT-002 | InstitutionSubmission, institutionRef, submitter, version | ASYNC/EVT | InstitutionDataSubmitted | INS pour workflow; DAT pour ingestion | éventuelle | conserver draft et retry | INS ne modifie pas EDU directement | faible |
| DAT pipeline → EDU | validated candidate record + provenance + quality | ASYNC/EVT | CandidateDomainRecordValidated | DAT pour validation; EDU décide publication | éventuelle contrôlée | quarantaine/review | DAT ne publie pas Institution/Program à la place d’EDU | faible |
| EMP-003 → OPP/EMP-002 | commands portant employerRef et actor rights | SYNC/API | WorkspaceCommands | domaine cible | forte sur commande | erreur explicite, retry idempotent | workspace n’écrit pas DB cible | faible |

## G. Data, Knowledge, Analytics et produits d’intelligence

| Producteur → consommateur | Données minimales | Mode | Contrat logique | Autorité | Cohérence | Panne | Dépendance interdite | Cycle |
|---|---|---|---|---|---|---|---|---|
| DAT-001 → DAT-002/003/004 | source metadata, rights, policy | ASYNC/PROJ + validation API | SourceProjection | DAT-001 | forte pour droit d’usage | ingestion/publication bloquée selon risque | aucune ingestion sans SourceRef gouverné sauf procédure d’urgence documentée | faible |
| DAT-002 → DAT-003 | RawRecordRef, batch, sourceRef, ingest timestamp | ASYNC/EVT | RawRecordAcquired | DAT-002 | éventuelle durable | retry, raw conservé | Provenance ne modifie pas raw | faible |
| DAT-003 → DAT-004/domaines | lineage, evidence, source chain | ASYNC/PROJ | ProvenanceBundle | DAT-003 | éventuelle | validation/publication bloquée si provenance obligatoire | domaine ne fabrique pas provenance manquante | faible |
| DAT-004 → domaines | ValidationDecision, quality dimensions, anomaly refs | ASYNC/EVT | DataValidationCompleted | DAT-004 pour qualité; domaine pour acceptation métier finale | éventuelle | quarantaine | DAT-004 ne remplace pas invariants métier | faible |
| domaines → KNW-001 | stable IDs, public/authorized attributes, semantic relations candidates | ASYNC/PROJ | KnowledgeProjection | domaines pour entités | éventuelle | graphe partiel/reconstruisible | KNW ne réécrit pas domaines | faible |
| domaines → ANL-001 | governed facts/events, dimensions, timestamps, versions | ASYNC/PROJ | AnalyticalProjections | domaines | éventuelle | métriques datées/incomplètes signalées | Analytics ne devient pas système transactionnel | faible |
| ANL-001 → ANL-002/003 | metric refs, aggregate snapshots, methodology version | ASYNC/PROJ | AnalyticsDataset | ANL-001 | éventuelle | produit marqué stale/non disponible | verticals ne recalculent pas métriques communes contradictoires | faible |
| ANL/LAB → INT-001 | insights, indicators, methodology/provenance refs | ASYNC/PROJ | IntelligenceInputs | producteurs pour calcul; INT pour édition | éventuelle | édition suspendue si données minimales absentes | INT ne réécrit pas indicateurs | faible |
| ANL/domaines → DPR-001 | approved aggregate dataset, schema/version, provenance, privacy status | ASYNC/PROJ | DataProductInput | sources; DPR pour release | snapshot immuable à publication | release bloquée si conformité/qualité absente | DPR ne vend pas copie brute personnelle | faible |
| domaines/DPR/INT → API-001 | exposed contract refs, versions, entitlement keys | ASYNC/PROJ | APIProductBinding | domaine pour données; API pour exposition | éventuelle config; contrat versionné | endpoint désactivé si binding invalide | API ne devient pas owner du contenu | faible |

## H. IA et cycle de vie des modèles

| Producteur → consommateur | Données minimales | Mode | Contrat logique | Autorité | Cohérence | Panne | Dépendance interdite | Cycle |
|---|---|---|---|---|---|---|---|---|
| MLP-001 → AI-001/004 | ModelRef, version, endpointRef, approval state, deployment state, capabilities | ASYNC/PROJ + lookup API | ApprovedModelProjection | MLP | forte pour sélection sensible | aucun modèle non approuvé; fallback seulement vers version approuvée | AI Gateway n’enregistre pas un modèle parallèle | faible |
| domaines/KNW/SRH → AI-002 | authorized documents/refs, provenance, access labels | ASYNC/PROJ | GroundingCorpusProjection | sources | éventuelle | corpus partiel; réponse peut être refusée | AI-002 ne devient pas source de vérité | faible |
| AI-001 → AI-004 | authorized AI request, policy, model eligibility | SYNC/API | AuthorizedAIExecution | AI-001 pour policy gate | forte | refuser/queue selon classe | orchestration ne contourne pas Gateway | faible |
| AI-004 → AI-002 | retrieval task, subject/access context, query | SYNC/API | RetrievalRequest | AI-004 pour task; AI-002 pour retrieval | cohérence par request | workflow dégradé/refusé | AI-004 ne lit pas index interne directement | faible |
| AI-002 → AI-004 | GroundingBundle, source refs, versions | SYNC/API | GroundingResponse | AI-002 pour bundle | snapshot | pas de génération factuelle sans grounding si politique l’exige | orchestration ne fabrique pas citations | faible |
| AI-004 → AI-003 | output claims, grounding refs, model/run refs | SYNC/API ou ASYNC job | VerificationRequest | AI-004 pour output; AI-003 pour verdict | snapshot | output bloqué ou étiqueté selon policy | orchestrator ne s’auto-valide pas | faible |
| AI-003 → AI-001/004 | VerificationDecision, confidence, failed claims | SYNC/API/EVT | AIVerificationCompleted | AI-003 | forte avant diffusion lorsque requise | fail-closed pour usages à risque | Gateway ne remplace pas verdict | faible |
| MLP-001 ← évaluations opérationnelles | evaluation metrics, incidents, drift signals, run refs | ASYNC/EVT | ModelOperationalEvidence | producteur métrique pour observation; MLP pour lifecycle decision | éventuelle | pas de promotion sans evidence requise | MLP ne modifie pas faits métier | faible |

## I. Économie, facturation, API, marketplace et sponsoring

| Producteur → consommateur | Données minimales | Mode | Contrat logique | Autorité | Cohérence | Panne | Dépendance interdite | Cycle |
|---|---|---|---|---|---|---|---|---|
| BIL-001 → API/MKT/DPR/INT/EMP-003/INS | Entitlement, quota commercial, productRef, status | HYBRID | EntitlementDecision API + EntitlementChanged | BIL-001 | forte pour autorisation payante; cache court révocable | fail-closed pour fonction payante sensible; grace explicite possible | consommateurs ne créent pas entitlement parallèle | faible |
| BIL-002 → BIL-001 | billing status, invoice/payment outcome, customerRef | ASYNC/EVT | BillingStateChanged | BIL-002 pour état financier | éventuelle contrôlée | entitlement suit politique de grace, jamais état inventé | Billing ne décide pas directement permission fonctionnelle | faible |
| BIL-001 → BIL-002 | subscriptionRef, billable product/version, pricing terms snapshot | ASYNC/EVT/API | BillableSubscriptionChanged | BIL-001 pour abonnement/catalogue; BIL-002 pour facture | snapshot immuable par facture | retry/idempotence | Billing ne modifie pas catalogue | faible |
| MKT-001 → BIL-002 | MarketplaceOrderRef, amount terms, provider/customer refs | SYNC/API ou EVT | BillingRequest | MKT pour order; Billing pour transaction | forte à paiement | order pending/failed | MKT ne marque pas paiement réussi seul | faible |
| SPN-001 → BIL-002 | campaignRef, billable delivery/budget event | ASYNC/EVT | SponsorshipBillingEvent | SPN pour delivery; BIL pour transaction | éventuelle | campagne suit budget confirmé/policy | SPN ne modifie pas orientation/recommendation | faible |
| API-001 → BIL-001 | API usage/quota consumption facts | ASYNC/EVT | APIUsageRecorded | API pour usage technique; BIL pour entitlement/quota commercial | éventuelle avec limite locale bornée | throttle conservateur si synchronisation perdue | API ne crée pas quota commercial indépendant | **moyen** résolu par séparation quota technique/commercial |

## J. Administration et commandes transversales

| Producteur → consommateur | Données minimales | Mode | Contrat logique | Autorité | Cohérence | Panne | Dépendance interdite | Cycle |
|---|---|---|---|---|---|---|---|---|
| ADM-001 → domaines | AdminCaseRef, actor, requested command, reason, authorization | SYNC/API | DomainAdminCommand | domaine cible | forte | commande échoue explicitement; case reste ouverte | ADM ne modifie aucune DB métier | faible |
| domaines → ADM-001 | command outcome, domain objectRef, error/reason | ASYNC/EVT/API response | AdminCommandResult | domaine | éventuelle | case pending/reconciliation | domaine ne dépend pas d’ADM pour ses opérations normales | faible |
| MOD/CNS/CFG/PRT → AUD | décisions sensibles et versions de policy | ASYNC/EVT | GovernanceAuditEvent | producteur | éventuelle durable | retry/buffer | Audit ne devient pas policy owner | faible |

## Cycles identifiés et traitement obligatoire

### C1 — EDU-002 ↔ EDU-003
Risque élevé. `Program` référence le curriculum publié, mais `Curriculum` dépend du Program. La création/édition du curriculum utilise `ProgramRef`; le retour vers Program passe uniquement par `CurriculumPublished`. Aucun appel transactionnel EDU-002 → EDU-003 → EDU-002.

### C2 — SKL-001 ↔ CAR-001
Les métiers utilisent les Skills, tandis que les observations métier enrichissent les relations Skill. CAR consomme une projection Skill. Les observations CAR → SKL sont des evidence events. Aucune écriture croisée.

### C3 — ORI-001 ↔ REC-001
Orientation commande un run de recommandation et reçoit un résultat immuable. Le flux doit être modélisé comme job/request-result corrélé, pas comme deux API synchrones se rappelant mutuellement.

### C4 — MOD-001 ↔ domaines modérés
Les domaines envoient objets/activités à modérer. MOD émet une décision. Le domaine applique la décision via commande ou événement idempotent. MOD n’écrit jamais directement la donnée source.

### C5 — BIL-001 ↔ API-001
BIL possède entitlement et quota commercial. API possède rate-limit technique et mesure d’usage. L’usage remonte vers BIL; l’autorisation commerciale descend vers API. Les deux quotas portent des identifiants et finalités différents.

### C6 — PRT-001 ↔ DAT-001
PRT possède accord/partenariat. DAT-001 possède la traduction opérationnelle des droits d’usage de source avec référence obligatoire vers l’accord. DAT-001 ne crée pas de droit juridique autonome.

## Dépendances interdites globales

1. Un domaine autoritatif ne lit jamais la base privée d’un autre service.
2. Aucun service ne met à jour un agrégat dont il n’est pas owner.
3. Recommendation, Analytics, Search, Knowledge Graph et AI ne deviennent jamais autoritatifs sur les faits projetés.
4. Un catalogue métier n’a aucune dépendance obligatoire vers Recommendation, Analytics ou AI pour écrire ses faits de base.
5. Sponsored Placement n’influence aucun score ORI, REC ou OPP Matching.
6. Une panne AI ne bloque pas les fonctions métier qui ne nécessitent pas explicitement l’IA.
7. Une panne Analytics ne bloque pas l’écriture transactionnelle métier.
8. Une projection ne sert jamais à valider une commande sensible si une vérification autoritative est requise.
9. Aucun workflow distribué n’utilise une transaction ACID inter-service.
10. Aucun cycle synchrone A → B → A n’est autorisé.

## Politique de panne D3

Chaque contrat D3 devra choisir explicitement parmi : `fail-closed`, `fail-open-borné`, `queue-and-retry`, `stale-read-borné`, `partial-result`, `manual-review`, `circuit-break`. Le choix dépend de la criticité et ne peut pas être implicite.

## Verdict de la carte

La cible peut être rendue acyclique au niveau des commandes. Les six relations bidirectionnelles identifiées sont converties en combinaison projection + événement, ou commande + résultat corrélé. Aucun besoin fonctionnel identifié n’exige une écriture croisée de base de données ou une transaction distribuée.

Cette carte est D3-candidate. Elle devient normative après création des contrats d’événements/API, définition des SLO de cohérence/fraîcheur et validation automatique de l’absence de cycles synchrones.
