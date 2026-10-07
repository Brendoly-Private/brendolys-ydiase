---
document_id: "YD-DOC-CON-EVENT-MAP"
title: "Event Map D3 — BRENDOLYS YDIASE"
document_type: "event-contract-map"
document_role: "Définit la carte des contrats événementiels D3 et leurs garanties logiques."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "contracts"
---

# Event Map D3 — BRENDOLYS YDIASE

> **Rôle du document**
> Définit la carte des contrats événementiels D3 et leurs garanties logiques.
> **Usage développement :** référence contractuelle obligatoire pour les implémentations et intégrations concernées.

Cette carte transforme la Dependency Map D3 en contrats événementiels candidats. Elle décrit le sens métier et les garanties attendues sans imposer un broker, Kafka, un format de sérialisation ou une infrastructure précise.

## Enveloppe commune obligatoire

Tout événement D3 porte au minimum :

`event_id`, `event_type`, `schema_version`, `occurred_at`, `producer`, `aggregate_type`, `aggregate_id`, `aggregate_version`, `correlation_id`, `causation_id`, `country_scope` si applicable, `data_classification`, `payload`.

Règles :

- `event_id` est globalement unique et sert de clé d’idempotence.
- `aggregate_version` est monotone pour un agrégat lorsque l’ordre compte.
- le producteur possède le schéma de son événement.
- un consommateur ne déduit jamais une autorité supérieure à celle du producteur.
- livraison logique au moins une fois : tout consommateur doit donc être idempotent.
- les retries utilisent backoff + jitter et finissent en quarantaine/DLQ logique après le seuil du contrat.
- l’expiration indiquée concerne l’utilité opérationnelle du message en transit. Elle ne définit pas la rétention légale ou analytique de la donnée source.
- aucune donnée secrète, credential, mot de passe, token ou document personnel complet dans un événement.
- `PII-min` signifie identifiant pseudonyme ou référence stable, sans profil complet.
- `Sensible` exige chiffrement en transit et au repos, contrôle d’accès et journalisation.

## Versionnement D3

- Version initiale : `1.0`.
- Ajout de champ optionnel compatible : version mineure.
- Suppression, renommage, changement de sens/type ou caractère obligatoire : version majeure.
- Un producteur garde une fenêtre de compatibilité définie avant retrait d’une majeure.
- Les consommateurs ignorent les champs inconnus et refusent une majeure non supportée.
- Un événement historique n’est jamais réécrit. Une correction produit un nouvel événement.

## A. Identité, profils, consentement et configuration

| ID / événement | Producteur | Consommateurs principaux | Payload minimal | Ver. | Idempotence | Retries | Expiration transit | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-IDN-001 `identity.status-changed` | IDN-001 | PRF, SKL-002, ASM, ORI, APP, COM, AUD | identity_ref, old_status, new_status, effective_at | 1.0 | event_id + aggregate_version | backoff, DLQ | 7 j | PII-min | IDN-001 |
| EVT-PRF-001 `profile.changed` | PRF-001 | ORI, REC-001, ORI-002, CAR-002/003/004, CNT-002 | profile_ref, changed_fields, profile_version | 1.0 | event_id/version | backoff, DLQ | 72 h | Sensible/PII-min | PRF-001 |
| EVT-PRF-002 `education-experience.changed` | PRF-002 | SKL-002, ORI, REC-001, OPP-002, CAR | profile_ref, record_refs, change_type, evidence_status | 1.0 | event_id/version | backoff, DLQ | 72 h | Sensible/PII-min | PRF-002 |
| EVT-CNS-001 `consent.changed` | CNS-001 | tout processeur concerné | subject_ref, purpose_ref, old_state, new_state, effective_at | 1.0 | event_id + consent version | priorité élevée, DLQ + alerte | 24 h | Très sensible/PII-min | CNS-001 |
| EVT-CNS-002 `privacy.restriction-changed` | CNS-001 | Data, AI, Analytics, NTF, produits | subject_ref, restriction_type, state, effective_at | 1.0 | event_id/version | priorité élevée, DLQ | 24 h | Très sensible/PII-min | CNS-001 |
| EVT-CNS-003 `privacy-requested` | CNS-001 | domaines détenteurs concernés, AUD | request_ref, subject_ref, request_type, due_at | 1.0 | request_ref | backoff + escalade | jusqu’à due_at | Très sensible | CNS-001 |
| EVT-CFG-001 `country-config.changed` | CFG-001 | domaines pays | country_code, config_version, changed_sections, effective_at | 1.0 | country+version | backoff, DLQ | 7 j | Interne | CFG-001 |
| EVT-AUD-001 `audit.event-recorded` | services producteurs vers AUD | AUD-001 | actor_ref, action, object_ref, outcome, trace_ref | 1.0 | event_id | buffer/retry durable | 30 j transit max | Sensible | producteur du fait; AUD du trail |

## B. Éducation, qualifications, compétences et carrières

| ID / événement | Producteur | Consommateurs principaux | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-EDU-001 `institution.changed` | EDU-001 | EDU-002, SRH, KNW, ANL, INS | institution_ref, change_type, status, campus_refs, version | 1.0 | ref+version | backoff, DLQ | 30 j | Public/Interne | EDU-001 |
| EVT-EDU-002 `program.changed` | EDU-002 | EDU-003, SRH, KNW, ANL, REC, LRN | program_ref, institution_ref, status, qualification_ref, version | 1.0 | ref+version | backoff, DLQ | 30 j | Public/Interne | EDU-002 |
| EVT-EDU-003 `curriculum.published` | EDU-003 | EDU-002, SKL-001, KNW, REC, LRN | curriculum_ref, program_ref, version, module_refs, published_at | 1.0 | ref+version | backoff, DLQ | 30 j | Public/Interne | EDU-003 |
| EVT-EDU-004 `curriculum.skill-evidence` | EDU-003 | SKL-001, KNW | curriculum_ref, module_ref, skill_ref, evidence_type, version | 1.0 | composite+version | backoff | 30 j | Interne | EDU-003 |
| EVT-EDU-005 `qualification.changed` | EDU-004 | EDU-002, PRF-002, CAR-001, SRH, KNW | qualification_ref, framework_ref, level_ref, change_type, version | 1.0 | ref+version | backoff, DLQ | 30 j | Public/Interne | EDU-004 |
| EVT-SKL-001 `skill-taxonomy.changed` | SKL-001 | EDU-003, SKL-002, CAR-001, LRN, RSH, KNW | skill_ref, change_type, taxonomy_version | 1.0 | ref+version | backoff, DLQ | 30 j | Public/Interne | SKL-001 |
| EVT-SKL-002 `user-skill.changed` | SKL-002 | ORI, REC, OPP-002, CAR-002/003/004 | subject_ref, skill_ref, level, evidence_state, skill_state_version | 1.0 | subject+skill+version | backoff, DLQ | 72 h | Très sensible/PII-min | SKL-002 |
| EVT-CAR-001 `occupation.changed` | CAR-001 | CAR-002/003/004, ORI, REC, LAB, SRH, KNW | occupation_ref, change_type, requirement_version | 1.0 | ref+version | backoff, DLQ | 30 j | Public/Interne | CAR-001 |
| EVT-CAR-002 `occupation.skill-evidence` | CAR-001 | SKL-001, KNW | occupation_ref, skill_ref, evidence_type, confidence, observed_at | 1.0 | event_id | backoff | 30 j | Interne | CAR-001 |
| EVT-CAR-003 `career-path.generated` | CAR-002 | CAR-004, ORI | path_ref, subject_ref optional, occupation_refs, input_versions | 1.0 | path_ref | backoff | 72 h | Sensible si subject_ref | CAR-002 |
| EVT-CAR-004 `career-transition.generated` | CAR-003 | CAR-004, ORI | transition_ref, subject_ref, source_occupation_ref, target_ref, gap_refs | 1.0 | transition_ref | backoff | 72 h | Très sensible/PII-min | CAR-003 |
| EVT-CAR-005 `career-simulation.completed` | CAR-004 | ORI, UI/NTF autorisés | simulation_ref, subject_ref, scenario_ref, result_ref, input_versions | 1.0 | simulation_ref | backoff | 72 h | Très sensible/PII-min | CAR-004 |

## C. Évaluation, orientation et recommandation

| ID / événement | Producteur | Consommateurs | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-ASM-001 `assessment.completed` | ASM-001 | ORI, REC-001, SKL-002 autorisé | assessment_session_ref, subject_ref, result_ref, validity_until, confidence | 1.0 | session_ref | backoff, DLQ | jusqu’à validity_until | Très sensible | ASM-001 |
| EVT-ORI-001 `orientation.started` | ORI-001 | AUD, Analytics autorisé | orientation_case_ref, subject_ref, objective_type, started_at | 1.0 | case_ref | backoff | 7 j | Très sensible/PII-min | ORI-001 |
| EVT-ORI-002 `recommendation.requested` | ORI-001 | REC-001 | request_ref, orientation_case_ref, subject_ref, constraint_snapshot_ref, input_versions | 1.0 | request_ref | retry job idempotent | 24 h | Très sensible/PII-min | ORI-001 |
| EVT-REC-001 `recommendation.completed` | REC-001 | ORI-001, ORI-002, NTF autorisé | request_ref, recommendation_set_ref, subject_ref, item_refs+scores, explanation_refs, evidence_snapshot_ref | 1.0 | request_ref + run_ref | backoff, DLQ | 72 h | Très sensible/PII-min | REC-001 |
| EVT-REC-002 `recommendation.failed` | REC-001 | ORI-001, observabilité | request_ref, failure_class, retryable, failed_at | 1.0 | request_ref+attempt class | retry selon flag | 24 h | PII-min | REC-001 |
| EVT-ORI-003 `orientation.completed` | ORI-001 | Analytics, NTF, AUD | orientation_case_ref, subject_ref, decision_record_ref, recommendation_set_ref optional | 1.0 | case_ref+state version | backoff | 7 j | Très sensible/PII-min | ORI-001 |
| EVT-ORI-004 `comparison.saved` | ORI-002 | ORI-001/UI autorisés | comparison_ref, subject_ref, compared_refs, criteria_version | 1.0 | comparison_ref/version | backoff | 72 h | Sensible | ORI-002 |

## D. Data acquisition, provenance et qualité

| ID / événement | Producteur | Consommateurs | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-DAT-001 `source.changed` | DAT-001 | DAT-002/003/004 | source_ref, rights_version, territory_scope, access_state | 1.0 | source+version | priorité élevée, DLQ | 7 j | Interne/confidentiel | DAT-001 |
| EVT-DAT-002 `raw-record.acquired` | DAT-002 | DAT-003, DAT-004 | raw_record_ref, batch_ref, source_ref, content_hash, acquired_at, classification | 1.0 | source+content_hash ou record_ref | backoff, DLQ | 30 j | Selon source, potentiellement très sensible | DAT-002 |
| EVT-DAT-003 `ingestion.completed` | DAT-002 | DAT-003/004, monitoring | batch_ref, source_ref, counts, completed_at | 1.0 | batch_ref | backoff | 7 j | Interne | DAT-002 |
| EVT-DAT-004 `provenance.recorded` | DAT-003 | DAT-004, domaines | provenance_ref, assertion_ref, source_ref, evidence_refs, lineage_version | 1.0 | assertion+lineage version | backoff, DLQ | 30 j | Selon assertion | DAT-003 |
| EVT-DAT-005 `data-validation.completed` | DAT-004 | domaine cible, DAT-003, monitoring | validation_ref, candidate_ref, decision, quality_summary, provenance_ref | 1.0 | validation_ref | backoff, DLQ | 30 j | Selon donnée | DAT-004 |
| EVT-DAT-006 `data-quality.failed` | DAT-004 | DAT-002, domaine cible, monitoring | candidate_ref, rule_refs, severity, anomaly_refs | 1.0 | candidate+quality run | backoff selon severity | 30 j | Selon donnée | DAT-004 |
| EVT-DAT-007 `candidate-domain-record.validated` | DAT-004 | EDU/LAB/EMP/autre domaine cible | candidate_ref, target_domain, source_ref, provenance_ref, validation_ref, normalized_payload_ref | 1.0 | candidate+validation version | backoff, DLQ | 30 j | Selon domaine | DAT-004 |
| EVT-DAT-008 `reference-dataset.changed` | DAT-005 | CFG, EDU, SKL, CAR, LAB, ANL | dataset_ref, version, changed_scope, effective_at | 1.0 | dataset+version | backoff | 30 j | Public/Interne | DAT-005 |

## E. Marché du travail

| ID / événement | Producteur | Consommateurs | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-LAB-001 `labor-signal.published` | LAB-001 | LAB-002, CAR-001, REC, KNW, ANL | signal_ref, signal_type, occupation/skill refs, territory_ref, observed_at, confidence, provenance_ref | 1.0 | signal_ref/version | backoff, DLQ | 30 j ou validity | Interne/agrégé | LAB-001 |
| EVT-LAB-002 `labor-signal.retracted` | LAB-001 | mêmes consommateurs | signal_ref, reason_code, retracted_at, replacement_ref optional | 1.0 | signal_ref+retraction version | priorité élevée | 30 j | Interne | LAB-001 |
| EVT-LAB-003 `labor-indicator.changed` | LAB-002 | LAB-003, REC, CAR, ANL, INT | indicator_ref, territory_ref, period, value_ref, methodology_version, freshness | 1.0 | indicator+period+version | backoff | 90 j | Agrégé | LAB-002 |
| EVT-LAB-004 `labor-forecast.published` | LAB-003 | CAR, ORI/REC autorisés, INT | forecast_ref, scope, horizon, scenario_refs, model_version, confidence | 1.0 | forecast_ref/version | backoff | jusqu’à horizon/retrait | Agrégé/interne | LAB-003 |
| EVT-LAB-005 `labor-forecast.invalidated` | LAB-003 | mêmes consommateurs | forecast_ref, reason, invalidated_at | 1.0 | forecast+version | priorité élevée | 30 j | Interne | LAB-003 |

## F. Opportunités, candidatures, employeurs et recrutement

| ID / événement | Producteur | Consommateurs | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-EMP-001 `employer.changed` | EMP-001 | OPP-001, EMP-002/003, SRH, ANL | employer_ref, verification_state, status, version | 1.0 | ref+version | backoff, DLQ | 30 j | Public/Interne | EMP-001 |
| EVT-OPP-001 `opportunity.published` | OPP-001 | OPP-002, APP-001, SRH, REC, NTF | opportunity_ref, employer_ref, requirement_refs, location_ref, valid_until, version | 1.0 | ref+version | backoff, DLQ | valid_until | Public/Interne | OPP-001 |
| EVT-OPP-002 `opportunity.changed` | OPP-001 | mêmes | opportunity_ref, changed_fields, status, valid_until, version | 1.0 | ref+version | backoff | valid_until | Public/Interne | OPP-001 |
| EVT-OPP-003 `opportunity.expired` | OPP-001 | OPP-002, APP-001, SRH, REC | opportunity_ref, expired_at, reason | 1.0 | ref+state version | priorité élevée | 30 j | Public | OPP-001 |
| EVT-OPM-001 `opportunity-match.completed` | OPP-002 | EMP-002, UI/NTF autorisés | match_ref, subject_ref, opportunity_ref, score, explanation_ref, input_versions | 1.0 | match_ref | backoff | 72 h ou opportunity expiry | Très sensible/PII-min | OPP-002 |
| EVT-APP-001 `application.submitted` | APP-001 | EMP-002/003, NTF, AUD | application_ref, subject_ref, opportunity_ref, employer_ref, submitted_at | 1.0 | application_ref | backoff, DLQ | durée du processus | Très sensible/PII-min | APP-001 |
| EVT-APP-002 `application.status-changed` | APP-001 | EMP-002/003, candidat/NTF, ANL autorisé | application_ref, old_status, new_status, effective_at, reason_code optional | 1.0 | application+state version | backoff, DLQ | durée du processus + politique | Très sensible/PII-min | APP-001 |
| EVT-EMP-002 `recruitment-campaign.changed` | EMP-002 | EMP-003, ANL-003 | campaign_ref, employer_ref, status, opportunity_refs, version | 1.0 | ref+version | backoff | campagne + 30 j | Confidentiel entreprise | EMP-002 |
| EVT-EMP-003 `candidate-selection.decided` | EMP-002 | APP-001, EMP-003, NTF | selection_ref, application_ref, decision_code, actor_ref, decided_at | 1.0 | selection_ref | retry idempotent | durée du processus | Très sensible | EMP-002 |

## G. Contenu, communauté, learning et modération

| ID / événement | Producteur | Consommateurs | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-CNT-001 `content.published` | CNT-001 | CNT-002, SRH, MOD, KNW | content_ref, author_ref, taxonomy_refs, visibility, version | 1.0 | ref+version | backoff | 30 j | Public/PII-min auteur | CNT-001 |
| EVT-CNT-002 `content.retired` | CNT-001 | CNT-002, SRH, MOD | content_ref, reason, retired_at | 1.0 | ref+state version | priorité élevée | 30 j | Interne | CNT-001 |
| EVT-COM-001 `community.activity-created` | COM-001 | CNT-002, MOD | activity_ref, actor_ref, object_ref, activity_type, visibility | 1.0 | activity_ref | backoff | 7 j | PII-min/contenu utilisateur | COM-001 |
| EVT-COM-002 `community-content.reported` | COM-001 | MOD-001 | report_ref, reporter_ref, object_ref, reason_code, created_at | 1.0 | report_ref | priorité élevée | jusqu’à décision | Sensible | COM-001 |
| EVT-MOD-001 `moderation.decided` | MOD-001 | CNT, COM, MKT, SPN, AUD | moderation_case_ref, object_ref, decision, effect, policy_version | 1.0 | case_ref+decision version | priorité élevée, DLQ | jusqu’à application | Sensible | MOD-001 |
| EVT-MOD-002 `moderation-policy.changed` | MOD-001 | domaines modérés | policy_ref, version, effective_at, affected_object_types | 1.0 | policy+version | backoff | 30 j | Interne | MOD-001 |
| EVT-LRN-001 `learning-resource.changed` | LRN-001 | SRH, REC, MKT, KNW | resource_ref, provider_ref, skill_refs, availability, version | 1.0 | ref+version | backoff | 30 j | Public/Interne | LRN-001 |
| EVT-RSH-001 `research-topic.published` | RSH-001 | SRH, CNT, utilisateurs autorisés | topic_ref, domain_refs, skill_refs, validation_state, version | 1.0 | ref+version | backoff | 90 j | Public/Interne | RSH-001 |

## H. Partenaires, ambassadeurs et espaces

| ID / événement | Producteur | Consommateurs | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-PRT-001 `partnership.changed` | PRT-001 | DAT-001, AMB, INS, EMP-003 | partner_ref, agreement_ref, status, role, access_scope_ref, effective_at | 1.0 | agreement+version | priorité selon révocation | 30 j | Confidentiel | PRT-001 |
| EVT-AMB-001 `ambassador-mandate.changed` | AMB-001 | DAT-002, INS, AUD | ambassador_ref, mandate_ref, institution/territory_ref, status, valid_until | 1.0 | mandate+version | backoff | valid_until + 30 j | Sensible/PII-min | AMB-001 |
| EVT-AMB-002 `ambassador-submission.created` | AMB-001 | DAT-002 | submission_ref, ambassador_ref, mandate_ref, source_context, artifact_refs | 1.0 | submission_ref | backoff, DLQ | 30 j | Selon données collectées | AMB-001 |
| EVT-INS-001 `institution-data.submitted` | INS-001 | DAT-002 | submission_ref, institution_ref, submitter_ref, dataset_type, artifact_refs, submitted_at | 1.0 | submission_ref | backoff, DLQ | 30 j | Confidentiel/PII-min | INS-001 |
| EVT-EMPW-001 `employer-workspace.changed` | EMP-003 | AUD/Analytics autorisé | workspace_ref, employer_ref, change_type, version | 1.0 | ref+version | backoff | 7 j | Confidentiel | EMP-003 |

## I. Search, Knowledge et Analytics

| ID / événement | Producteur | Consommateurs | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-SRH-001 `search-index.updated` | SRH-001 | observabilité, AI-002 | index_ref, source_domain, source_version_watermark, completed_at | 1.0 | index+watermark | backoff | 24 h | Interne | SRH-001 |
| EVT-KNW-001 `knowledge-graph.updated` | KNW-001 | REC, AI-002, RSH, Analytics | graph_version, changed_node_types, source_watermarks | 1.0 | graph_version | backoff | 72 h | Interne | KNW-001 |
| EVT-ANL-001 `analytical-snapshot.published` | ANL-001 | ANL-002/003, INT, DPR | snapshot_ref, metric_refs, scope, period, methodology_version, freshness | 1.0 | snapshot_ref | backoff | 90 j | Agrégé/confidentiel selon scope | ANL-001 |
| EVT-ANL-002 `institution-insight.published` | ANL-002 | INS, INT, API autorisé | insight_ref, institution_ref, period, metric_refs, version | 1.0 | insight_ref/version | backoff | 90 j | Confidentiel/agrégé | ANL-002 |
| EVT-ANL-003 `employer-insight.published` | ANL-003 | EMP-003, INT, API autorisé | insight_ref, employer_ref, period, metric_refs, version | 1.0 | insight_ref/version | backoff | 90 j | Confidentiel/agrégé | ANL-003 |

## J. IA et lifecycle des modèles

| ID / événement | Producteur | Consommateurs | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-MLP-001 `model-version.approved` | MLP-001 | AI-001, AI-004 | model_ref, model_version, capability_refs, approval_ref, endpoint_ref | 1.0 | model+version+approval | priorité élevée | jusqu’au retrait | Confidentiel technique | MLP-001 |
| EVT-MLP-002 `model-deployment.changed` | MLP-001 | AI-001/004, observabilité | model_ref, version, deployment_state, endpoint_ref, effective_at | 1.0 | deployment version | priorité élevée | 24 h | Confidentiel technique | MLP-001 |
| EVT-MLP-003 `model-version.retired` | MLP-001 | AI-001/004 | model_ref, version, retired_at, replacement_ref optional | 1.0 | model+version+retirement | priorité élevée | 30 j | Confidentiel | MLP-001 |
| EVT-AI-001 `ai-execution.requested` | AI-001 | AI-004 | ai_request_ref, subject_ref optional, purpose_ref, capability, allowed_model_scope, policy_ref | 1.0 | request_ref | retry idempotent | minutes/heures selon use case | Très sensible selon contexte | AI-001 |
| EVT-AI-002 `ai-workflow.completed` | AI-004 | AI-001, AI-003 si vérification async, caller | workflow_run_ref, request_ref, model_ref/version, output_ref, grounding_bundle_ref | 1.0 | run_ref | backoff | 24 h | Très sensible selon output | AI-004 |
| EVT-AI-003 `ai-verification.completed` | AI-003 | AI-001/004, AUD autorisé | verification_ref, workflow_run_ref, decision, confidence, failed_claim_refs | 1.0 | verification_ref | priorité élevée | 24 h | Sensible | AI-003 |
| EVT-AI-004 `model-operational-evidence.recorded` | AI/observabilité autorisée | MLP-001 | model_ref/version, metric_type, metric_value_ref, period, incident_ref optional | 1.0 | evidence_ref | backoff | 30 j | Confidentiel technique | producteur observation; MLP lifecycle |

## K. Abonnements, facturation, marketplace, sponsoring, API et produits

| ID / événement | Producteur | Consommateurs | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-BIL-001 `subscription.changed` | BIL-001 | BIL-002, API, MKT, DPR, INT, workspaces | subscription_ref, customer_ref, product_ref/version, status, effective_at | 1.0 | subscription+version | backoff, DLQ | 30 j | Confidentiel/PII-min | BIL-001 |
| EVT-BIL-002 `entitlement.changed` | BIL-001 | services protégés | entitlement_ref, subject/customer_ref, capability_ref, state, quota_ref optional, effective_at | 1.0 | entitlement+version | priorité élevée | 24 h | Confidentiel/PII-min | BIL-001 |
| EVT-BIL-003 `billing-state.changed` | BIL-002 | BIL-001, MKT, SPN, workspaces | billing_account_ref, related_object_ref, state, amount_ref optional, occurred_at | 1.0 | provider transaction ref + event_id | retries idempotents, DLQ | 30 j | Financier sensible | BIL-002 |
| EVT-BIL-004 `invoice.issued` | BIL-002 | customer surface, accounting integrations autorisées | invoice_ref, billing_account_ref, amount_ref, currency, due_at | 1.0 | invoice_ref | backoff | due_at + 30 j | Financier sensible | BIL-002 |
| EVT-MKT-001 `marketplace-order.changed` | MKT-001 | BIL-002, LRN, NTF | order_ref, customer_ref, listing_ref, state, commercial_terms_ref | 1.0 | order+version | backoff | durée order + 30 j | Financier/PII-min | MKT-001 |
| EVT-SPN-001 `sponsored-campaign.changed` | SPN-001 | BIL-002, MOD, delivery surfaces | campaign_ref, advertiser_ref, state, placement_scope, budget_ref | 1.0 | campaign+version | backoff | campagne + 30 j | Commercial confidentiel | SPN-001 |
| EVT-SPN-002 `sponsored-placement.delivered` | SPN-001 | BIL-002, ANL | delivery_ref, campaign_ref, placement_ref, occurred_at, billable_unit | 1.0 | delivery_ref | backoff | 30 j | Commercial | SPN-001 |
| EVT-API-001 `api-usage.recorded` | API-001 | BIL-001, ANL, AUD selon besoin | client_ref, api_product_ref, usage_units, period_bucket, technical_quota_state | 1.0 | client+product+bucket+sequence | backoff | 30 j | Confidentiel technique | API-001 |
| EVT-DPR-001 `data-product.released` | DPR-001 | API-001, clients internes, BIL-001 | data_product_ref, release_ref, schema_version, license_ref, privacy_status, source_snapshot_refs | 1.0 | release_ref | backoff | jusqu’au retrait | Agrégé/gouverné | DPR-001 |
| EVT-INT-001 `intelligence-edition.published` | INT-001 | API-001, clients autorisés, BIL-001 | product_ref, edition_ref, scope, period, evidence_refs, access_class | 1.0 | edition_ref | backoff | selon édition | Confidentiel ou public selon produit | INT-001 |

## L. Administration et notifications

| ID / événement | Producteur | Consommateurs | Payload minimal | Ver. | Idempotence | Retries | Expiration | Sensibilité | Owner |
|---|---|---|---|---|---|---|---|---|---|
| EVT-ADM-001 `admin-command.requested` | ADM-001 | domaine cible | admin_case_ref, command_ref, target_ref, actor_ref, reason_code | 1.0 | command_ref | retry idempotent | 24 h ou case SLA | Très sensible | ADM-001 |
| EVT-ADM-002 `admin-command.completed` | domaine cible | ADM-001, AUD | command_ref, target_ref, outcome, resulting_version optional | 1.0 | command_ref+outcome version | backoff | 7 j | Sensible | domaine cible |
| EVT-NTF-001 `notification.requested` | tout domaine autorisé | NTF-001 | notification_request_ref, recipient_ref, template_key, object_ref, priority, purpose_ref | 1.0 | request_ref | backoff, DLQ | selon type, 15 min à 7 j | PII-min | producteur de la demande |
| EVT-NTF-002 `notification.delivery-status` | NTF-001 | producteur demande, Analytics autorisé | request_ref, channel, status, attempt_count, delivered_at optional | 1.0 | request+channel+attempt | backoff pour statut final | 7 j | PII-min | NTF-001 |

## Matrice de sensibilité

| Classe | Contenu autorisé dans l’événement | Règle |
|---|---|---|
| Public | IDs et attributs déjà publiables | diffusion selon contrat |
| Interne | métadonnées métier non publiques | accès service-to-service autorisé |
| Confidentiel | données partenaire, entreprise, techniques ou commerciales | accès restreint + audit |
| Sensible | données individuelles ou décisions concernant une personne | minimisation + chiffrement + purpose |
| Très sensible | évaluations, compétences individuelles, candidatures, orientation, consentements, résultats IA personnels | référence/pseudonyme privilégié, payload minimal, contrôle CNS obligatoire |

## Politique d’idempotence

1. Chaque consommateur maintient une preuve de traitement par `event_id` ou clé métier documentée.
2. Les événements d’état portent `aggregate_version`; une version ancienne ne remplace jamais une version récente.
3. Les commandes événementielles portent un `command_ref` stable.
4. Les paiements utilisent aussi l’identifiant immuable du prestataire externe lorsqu’il existe.
5. Les projections sont reconstruisibles et supportent replay.

## Politique de retry

- erreur transitoire : retry exponentiel avec jitter
- erreur de schéma/version : pas de boucle infinie; quarantaine immédiate
- erreur métier non retryable : enregistrer le rejet et produire le résultat métier adapté
- après seuil : DLQ/quarantaine logique + alerte selon criticité
- consentement/révocation, modération bloquante, état modèle et expiration d’opportunité reçoivent une priorité supérieure aux événements analytiques

## Ordre et concurrence

L’ordre global n’est jamais supposé. Lorsque l’ordre est nécessaire, il est défini par `aggregate_id + aggregate_version`. Deux agrégats différents peuvent être traités en parallèle. Les consommateurs détectent les trous de version et déclenchent réconciliation ou reconstruction de projection.

## Expiration et replay

Un événement expiré pour une action temps réel peut rester exploitable pour reconstruction si la politique de rétention l’autorise. Un replay ne doit jamais réexécuter aveuglément un effet externe tel qu’un paiement, un message utilisateur, une décision de recrutement ou une commande administrative. Ces consommateurs utilisent une clé d’effet idempotente distincte.

## Contrôles D3 obligatoires

- aucun événement ne contient de credential ou secret
- aucun événement personnel sans `purpose_ref` lorsque la finalité n’est pas implicite et documentée par le contrat
- aucun événement de recommandation ne mélange contenu sponsorisé et score organique
- aucune projection Search, Analytics, Knowledge ou AI ne se présente comme source autoritative
- chaque événement possède un owner unique du schéma
- chaque consommateur déclaré doit avoir une stratégie d’idempotence et de panne
- les événements de retrait/révocation doivent pouvoir dépasser les événements ordinaires en priorité opérationnelle

## Incohérences ou décisions encore nécessaires

La carte ne présente plus de collision d’ownership connue. Les paramètres numériques de retry, durée exacte de rétention, SLO de propagation, taille maximale des payloads, fenêtre de compatibilité des versions et classification juridique finale par pays restent volontairement à fixer dans le Contract Registry et les exigences non fonctionnelles. Ils ne doivent pas être inventés au niveau de cette carte.

## Statut

`D3-candidate` — la topologie événementielle est définie. Le passage D3 normatif exige maintenant le Contract Registry, les schémas de contrats candidats, les règles de compatibilité automatisables et les SLO de propagation par classe d’événement.
