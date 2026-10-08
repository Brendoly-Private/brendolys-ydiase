---
document_id: "YD-DOC-POL-REC-001-RECOMMENDATION-RANKING"
title: "YD-MS-REC-001 — Recommendation Ranking Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de recommendation ranking pour YD-MS-REC-001."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "policy"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-REC-001 — Recommendation Ranking Policy

> **Rôle du document**
> Établit les règles normatives de recommendation ranking pour YD-MS-REC-001.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `DECISION-BASELINE / IMPLEMENTATION-PENDING`
Nature : politique normative C1

## 1. Pipeline normatif

REC-001 est autoritatif sur RecommendationRun/Set/Item/Explanation/EvidenceSnapshot, jamais sur ses données d'entrée.

Le pipeline sépare :
1. `ELIGIBILITY` ;
2. `ORGANIC-SCORING` ;
3. `ORGANIC-RANKING` ;
4. `PRESENTATION`.

Aucune logique commerciale ne peut rétroagir sur les trois premières étapes.

## 2. Run et versionnement

Chaque run conserve au minimum : run_id, subject/context ref autorisé, purpose_ref, recommendation_type, policy_version, model_version si applicable, candidate_generation_version, evidence_snapshot_ref, country/context_ref, timestamps, freshness_state, quality_state et abstention_state/reason.

Un changement de policy/modèle crée un nouveau run. L'historique n'est jamais réécrit silencieusement.

## 3. Éligibilité

Contraintes : `HARD`, `REQUIRED`, `SOFT`, `INFORMATIONAL`.

Un échec HARD exclut ou marque explicitement non éligible. Un score élevé ne compense jamais un HARD constraint.

`UNKNOWN` n'est jamais `FAILED`. Une donnée critique inconnue entraîne abstention, dégradation explicite ou statut conditionnel selon policy.

## 4. Candidats

La génération peut utiliser EDU, CAR, LAB, OPP, LRN, KNW et autres projections gouvernées. Elle conserve source/version d'inventaire, règles de filtrage, contexte, état de publication/validité et exclusions.

Une projection incomplète ne prouve jamais qu'un candidat n'existe pas.

## 5. Score organique et pondérations

Le score organique utilise uniquement des critères métier/utilisateur autorisés : objectifs, skills/gaps, prérequis, formation/qualification, contraintes, disponibilité, signaux marché, qualité/fraîcheur et diversité/exploration si la policy le prévoit.

Chaque composante conserve sens, source et contribution.

Paiement, budget publicitaire, commission, statut partenaire ou probabilité de conversion commerciale sont interdits dans le score organique.

Les pondérations appartiennent à une `RecommendationPolicyVersion` : versionnées, explicables, validées et contextualisées seulement avec justification gouvernée. Aucun poids numérique n'est inventé ici.

## 6. Ranking organique

Le ranking ordonne les candidats éligibles selon score organique et tie-breaks versionnés. Il conserve organic_score, organic_rank, composantes, contraintes/exclusions et incertitude/qualité.

Diversité/exploration peut modifier l'ordre seulement comme règle organique explicite, traçable et non financée commercialement.

## 7. Evidence Snapshot

Chaque run persistant référence les versions nécessaires : PRF autorisé, SKL-002, ASM, EDU, CAR, LAB, OPP/LRN, KNW watermark si utilisé, CFG/policy et décision CNS/purpose applicable.

Le snapshot privilégie refs/version IDs et valeurs dérivées minimales ; il ne copie pas les dossiers personnels complets ni les preuves brutes par défaut.

## 8. Fraîcheur et abstention

Motifs minimaux : `INSUFFICIENT-EVIDENCE`, `STALE-CRITICAL-INPUT`, `PRIVACY-NOT-VERIFIABLE`, `NO-ELIGIBLE-CANDIDATE`, `CONFLICTED-INPUT`, `MODEL-POLICY-NOT-APPROVED`, `PROJECTION-NOT-READY`.

REC ne fabrique jamais un ranking pour éviter une réponse vide. Un ancien run n'est affiché qu'avec date/version/fraîcheur explicites.

## 9. Explicabilité et incertitude

Chaque item explique : éligibilité, principaux critères contributifs, gaps/contraintes, données majeures utilisées, inconnues critiques, signaux marché, incertitude/qualité et policy/model version.

Un LLM peut reformuler l'explication structurée mais n'invente aucune justification.

L'incertitude est distincte du score : `LOW-UNCERTAINTY`, `MEDIUM-UNCERTAINTY`, `HIGH-UNCERTAINTY`, `NOT-ASSESSABLE`. Un rang élevé ne masque jamais une forte incertitude.

## 10. Biais et équité

Avant activation d'une policy personnalisée : définir les contextes d'évaluation, mesurer couverture/erreurs et disparités injustifiées d'éligibilité, score, exposition et abstention, documenter limites/dérives et prévoir revue/rollback.

Les attributs sensibles/protégés ne personnalisent pas le ranking sauf base légitime, finalité explicite et validation de gouvernance. Leur usage éventuel pour audit d'équité est séparé, minimisé et contrôlé.

## 11. Séparation absolue organique / sponsoring

SPN-001 ne peut jamais écrire ou influencer : `organic_score`, `organic_rank`, pondérations REC, critères organiques, exclusions organiques ou RecommendationExplanation organique.

REC ne consomme aucun budget, enchère, commission ou relation commerciale pour calculer le ranking organique.

Un placement sponsorisé est demandé/produit séparément par SPN-001, explicitement étiqueté, soumis à éligibilité/modération/Privacy et métriqué séparément.

Une position visuelle sponsorisée ne change jamais organic_rank. Un sponsor intercalé dans l'UI reste hors séquence de rang organique.

Le statut partenaire ou marketplace ne confère aucune pertinence organique.

## 12. Privacy, correction et reproductibilité

Toute personnalisation est liée à purpose_ref et minimisée. Si une décision Privacy requise n'est pas vérifiable, fail-closed ou mode non personnalisé explicitement autorisé.

Une correction d'entrée ne réécrit pas un ancien run : snapshot historique conservé, run marqué stale/invalidated si nécessaire, nouveau run produit.

Un run doit être reproductible/auditable via candidate generation version, evidence snapshot, policy/model versions, scoring components, tie-breaks, contexte et timestamps.

## 13. RSH-001

RSH-001 reste module logique tant qu'il n'a pas d'autorité académique autonome. Catalogue autoritatif de sujets, validation académique, encadrement, mémoire/thèse/soutenance ou règles PI propres déclenchent la revue d'extraction.

## 14. Gates

`DEFINED` : pipeline, hard constraints, UNKNOWN, pondérations versionnées, evidence snapshot, abstention, explicabilité, incertitude, biais/équité de principe, séparation sponsoring, correction, reproductibilité, limite RSH.

`DEFINED-BY-COMPANION-POLICY` : métriques/protocole d'équité et suite de tests anti-influence SPN.

`TBD-VALIDATION/PREPROD` : coefficients/seuils de ranking, seuils numériques d'équité, datasets représentatifs/preuves d'évaluation, exécution des tests anti-influence SPN, règles mineurs, Privacy/rétention, BIA/RPO/RTO/restore, IAM/IDOR et contrats/runtime/observabilité.

Statut final : `RECOMMENDATION-POLICY-CLOSED / FAIRNESS-AND-SPONSOR-GUARDS-DEFINED / PREPROD-EVIDENCE-PENDING`.
