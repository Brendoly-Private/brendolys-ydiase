---
document_id: "YD-DOC-POL-OPP-002-OPPORTUNITY-MATCHING"
title: "YD-MS-OPP-002 — Opportunity Matching Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de opportunity matching pour YD-MS-OPP-002."
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
---

# YD-MS-OPP-002 — Opportunity Matching Policy

> **Rôle du document**
> Établit les règles normatives de opportunity matching pour YD-MS-OPP-002.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / NUMERIC-VALIDATION-PENDING`
Nature : `MIXED`
Criticité : `C2`

## 1. Mission

OPP-002 répond à une question spécialisée : **dans quelle mesure un profil autorisé correspond-il aux exigences d'une opportunité donnée ?**

Il possède OpportunityMatchRun, OpportunityMatch et MatchExplanation. Il ne possède ni profil, ni compétences, ni Opportunity, ni Application.

## 2. Match ≠ recommandation ≠ candidature

Un match mesure une compatibilité selon une policy. REC-001 peut utiliser ce résultat dans une recommandation plus large intégrant objectifs, marché, parcours ou autres critères.

Un match élevé ne crée jamais une candidature et ne garantit ni sélection, ni entretien, ni emploi.

## 3. Pipeline

`PRIVACY-CHECK → INPUT-SNAPSHOT → ELIGIBILITY → MATCH-COMPONENTS → SCORE/STATE → EXPLANATION`.

Si une décision CNS requise n'est pas vérifiable : fail-closed pour le matching personnalisé.

## 4. Snapshot

Chaque run conserve au minimum :
- opportunity_ref/version ;
- profile refs/versions minimisées ;
- SKL-002 state versions ;
- PRF education/experience refs nécessaires ;
- applicable CAR/SKL/EDU mappings ;
- CNS purpose/decision ref ;
- policy/model version ;
- computed_at ;
- freshness/quality states.

Un run historique n'est jamais recalculé silencieusement avec de nouvelles données.

## 5. Eligibility

Les contraintes OPP `REQUIRED` sont évaluées séparément des préférences. Une contrainte légalement/policy interdite n'est jamais utilisée.

`UNKNOWN` n'est pas `FAILED`. Selon criticité, le moteur abstient ou indique compatibilité conditionnelle.

## 6. Score

Dimensions possibles : compétences, expérience, formation/qualification, localisation/mobilité autorisée, contraintes opérationnelles et autres exigences explicitement permises.

Chaque composante est traçable et versionnée. Les coefficients numériques restent à valider.

Aucun sponsoring, paiement, commission, relation commerciale ou priorité employeur ne peut augmenter le score organique.

## 7. Explicabilité

MatchExplanation expose :
- exigences satisfaites ;
- exigences manquantes ;
- exigences inconnues ;
- principaux facteurs contributifs ;
- données/fraîcheur utilisées ;
- incertitude ;
- policy/model version.

Un LLM peut reformuler, jamais inventer une justification.

## 8. Incertitude et abstention

États possibles : `MATCHABLE`, `CONDITIONAL`, `INSUFFICIENT-EVIDENCE`, `NOT-ELIGIBLE`, `NOT-ASSESSABLE`.

Le score et l'incertitude sont distincts. Un score élevé avec données faibles reste explicitement incertain.

## 9. Corrections

Correction PRF/SKL/OPP/CNS ne réécrit pas un ancien run. Celui-ci peut être marqué stale/invalidated ; un nouveau run utilise les nouvelles versions.

## 10. Équité

Avant ACTIVE, les critères/proxies doivent être audités pour discrimination directe/indirecte et disparités injustifiées. Les attributs protégés ne sont pas utilisés pour personnaliser le score sauf base légitime et gouvernance explicite.

L'audit d'équité est séparé de la personnalisation.

## 11. Relation APP-001

Au clic "candidater", OPP-002 transmet au plus un MatchRef/context autorisé. APP-001 revalide l'Opportunity auprès d'OPP-001 et crée sa propre Application.

APP ne doit jamais considérer MatchScore comme décision de recrutement.

## 12. Relation EMP-002

Un employeur ne peut obtenir un matching personnalisé sur une personne sans finalité, droits/scopes et décision CNS applicables. L'accès employeur au talent est une frontière distincte à fermer dans EMP-002.

## 13. Gates

`DEFINED` : frontière match/REC/APP, snapshot, eligibility, score components, explication, incertitude, correction, principe équité, isolation commerciale.

`TBD-PREPROD` : coefficients/seuils, fairness metrics/thresholds, règles par type d'opportunité, IAM/IDOR, rétention des runs, BIA/RPO/RTO, restore et contrats physiques.

Statut final : `OPPORTUNITY-MATCHING-SEMANTICS-CLOSED / NUMERIC-FAIRNESS-AND-PREPROD-PENDING`.
