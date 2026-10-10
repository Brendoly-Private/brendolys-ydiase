---
document_id: "YD-DOC-AUTO-65BA70130920CDEB"
title: "AUTONOMY PROFILE"
document_type: "documentation-reference"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
product: "BRENDOLYS YDIASE"
document_role: "Autonomie et ownership."
authority_level: "canonical-source"
development_usage: "mandatory-reference"
canonical: true
status: "DRAFT"
---

# YD-MS-ASM-001 — Assessment

Statut : `autonomy-profile-draft`

- Autorité : sessions, réponses, résultats, validité et confidence des évaluations.
- C1, backup AUTH; données de profilage sensibles.
- IAM : C sujet, I support autorisé, M2M.
- Dépendances : Identity, CNS, CFG; publie AssessmentCompleted vers ORI/REC.
- Panne : reprise de session selon règles; calcul/stockage sensible suspendu si privacy requise non vérifiable.
- Sécurité : contrôle objet strict, audit, minimisation, version de méthodologie liée au résultat.
- Repo : `brendolys-ydiase-assessment`.
- Gate : méthodologies, rétention, règles mineurs, scopes, SLO/RPO/RTO, restore et tests sécurité.