# YD-MS-EMP-002 — Talent Access & Recruitment Policy

Statut : `NORMATIVE-C1-BASELINE / PREPROD-PENDING`
Nature : `AUTH`
Criticité : `C1`

## 1. Autorité
EMP-002 possède TalentPool, RecruitmentCampaign, CandidateSelection et RecruitmentPipeline. Il ne possède ni Employer, ni Opportunity, ni Application, ni profil/compétences.

## 2. Interdiction fondamentale
EMP-002 n'est pas un moteur de recherche libre de personnes.

Un recruteur ne peut explorer PRF/SKL ou récupérer des profils simplement parce qu'il possède un compte employeur.

## 3. Conditions d'accès talent
Tout accès personnalisé exige au minimum :
- Employer actif et niveau de vérification requis ;
- principal recruteur autorisé et tenant/scopes valides ;
- purpose/finalité recrutement explicite ;
- campagne/opportunité ou contexte autorisé ;
- décision CNS applicable ;
- politique d'accès et minimisation ;
- journalisation/audit.

Si une condition obligatoire n'est pas vérifiable : fail-closed.

## 4. TalentPool
Un TalentPool est un ensemble gouverné de références/projections autorisées pour une finalité et une durée. Il conserve source d'inclusion, scope, purpose_ref, campaign/opportunity refs, CNS decision/version, expires_at et policy version.

Il n'est jamais une copie permanente du profil YDIASE.

## 5. Projection minimale
EMP-002 ne reçoit que les attributs nécessaires au recrutement concerné. Les données sensibles/non nécessaires, documents complets ou historique hors finalité ne sont pas exposés par défaut.

Un accès à une donnée supplémentaire exige scope/finalité correspondants.

## 6. CandidateSelection
CandidateSelection conserve application/candidate ref autorisé, campaign ref, stage, decision, reason codes, evidence refs, actor/automation identity, policy version et timestamp.

Un score OPP-002 peut être une entrée explicable, jamais la décision elle-même.

## 7. RecruitmentPipeline
Le pipeline recruteur organise le travail EMP-002. Lorsqu'une étape implique l'état officiel d'une candidature, EMP-002 envoie une commande à APP-001 ; seul APP confirme la transition.

EMP-002 ne crée pas un miroir autoritatif du statut Application.

## 8. Accès sans candidature
La découverte proactive de talents, si activée, nécessite une policy distincte : opt-in/autorisation applicable, finalité, visibilité, critères autorisés, limites d'export/contact, expiration et audit.

Tant que cette policy n'est pas validée, **pas de recherche proactive nominative de talents**.

## 9. Révocation Privacy
À révocation/restriction CNS, les projections concernées sont retirées/inaccessibles selon SLO ; caches expirés ne prolongent pas l'accès.

Les obligations de conservation liées à une candidature existante restent traitées via APP/CNS/policy applicable et ne justifient pas un accès général au profil.

## 10. Équité et automatisation
Les critères de sélection doivent être auditables. Les attributs/proxies interdits ne sont pas utilisés. Toute décision automatisée ou assistance algorithmique conserve modèle/policy/version, explication et niveau d'intervention humaine selon gouvernance applicable.

## 11. Exports
Export massif de profils désactivé par défaut. Toute capacité d'export exige finalité, scope, limite, watermark/audit et politique de rétention. Aucun dump de base candidats.

## 12. Multi-tenant
Toutes les campagnes, pools et sélections sont tenant-scoped. Toute fuite cross-tenant ou IDOR est release-blocking.

## 13. Gates
DEFINED : accès talent, minimisation, TalentPool, CandidateSelection, APP authority, proactive discovery gate, revocation, exports, tenant isolation.
TBD : policy proactive réelle, critères/fairness, rôles/scopes, rétention pays, BIA/RPO/RTO, restore, contrats physiques.

Statut final : `TALENT-RECRUITMENT-SEMANTICS-CLOSED / PROACTIVE-ACCESS-AND-PREPROD-PENDING`.
