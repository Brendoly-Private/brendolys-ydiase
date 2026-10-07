---
document_id: "YD-DOC-DOM-ORIENTATION-RECOMMENDATION-GATES-ET-INCONNUES"
title: "Gates et inconnues — Orientation et recommandation"
document_type: "domain-knowledge"
document_role: "Documente la connaissance métier et les frontières applicables au domaine concerné."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "domain"
---

# Gates et inconnues — Orientation et recommandation

Statut : `DOMAIN-REVIEW-CANDIDATE`

| Gate | ASM-001 | ORI-001 + ORI-002 | REC-001 |
|---|---|---|---|
| ownership | DEFINED | DEFINED | DEFINED |
| criticité | C1 | C1 | C1 |
| séparation Assessment/UserSkill | DEFINED | N/A | N/A |
| fusion ORI-001/ORI-002 | N/A | VALIDATED | N/A |
| ORI vs REC | N/A | DEFINED | DEFINED |
| boucle ORI/REC | N/A | ASYNC/NON-CIRCULAR | ASYNC/NON-CIRCULAR |
| méthodologie/version | TBD-BEFORE-IMPLEMENTATION | input version required | **RANKING-POLICY-DEFINED** |
| validité/confiance résultat | TBD-BEFORE-IMPLEMENTATION | consommée explicitement | consommée explicitement |
| workflow de décision | N/A | TBD-BEFORE-IMPLEMENTATION | N/A |
| explicabilité | méthodologie | TBD-BEFORE-ACTIVE | **DEFINED** |
| mineurs/représentation | TBD-BEFORE-ACTIVE | TBD-BEFORE-ACTIVE | TBD-BEFORE-ACTIVE |
| Privacy/rétention | TBD-BEFORE-ACTIVE | TBD-BEFORE-ACTIVE | TBD-BEFORE-ACTIVE |
| IAM/IDOR | TBD-PREPROD | TBD-PREPROD | TBD-PREPROD |
| BIA/RPO/RTO/restore | TBD-C1 | TBD-C1 | TBD-C1 |
| biais/équité | N/A | N/A | **METRICS-DEFINED / THRESHOLDS-PENDING** |
| anti-influence sponsoring | N/A | N/A | **TEST-SUITE-DEFINED / EXECUTION-PENDING** |

## Prochaine fermeture sémantique

ASM-001 doit définir la structure d'une méthodologie, la validité, confiance, correction et versionnement des résultats.

ORI-001 doit définir le cycle du dossier, critères/contraintes, comparaison, décision enregistrée, réouverture et traçabilité.

REC-001 dispose désormais de `../../03-systems/policies/YD-MS-REC-001/RECOMMENDATION_RANKING_POLICY.md` : pipeline eligibility/scoring/ranking/presentation, evidence snapshot, abstention, explicabilité, incertitude, principes d'équité et séparation absolue du sponsoring sont définis. Les coefficients, métriques d'équité et preuves préproduction restent à valider.

Statut : `DOMAIN-BASELINE-CANDIDATE / REC-RANKING-FAIRNESS-SPONSOR-GUARDS-DEFINED`.
