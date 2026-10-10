---
document_id: "YD-DOC-AUTO-4E8B5066562CD139"
title: "AUTONOMY PROFILE"
document_type: "documentation-reference"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
product: "BRENDOLYS YDIASE"
---

# YD-MS-DPR-001 — Data Product

Statut : `autonomy-profile-draft`

- Autorité : releases Data Product, manifests, licences et état de publication; données sources restent chez leurs owners.
- Owner métier du catalogue commercial : fonction Product & Commercial YDIASE. DPR contrôle release/manifest/licence/publication; ANL/DAT gardent les sources; CNS garde privacy; BIL garde abonnement/facturation/entitlement.
- Criticité : C1. Reprise AUTH.
- Licence : chaque release possède un `LicenseManifest` versionné/immuable avec license/version, product/release, catégories de consommateurs, finalités, territoires, durée, droits lecture/export/redistribution/dérivation, sous-licence, entitlement BIL, décision CNS, obligations retrait/suppression, provenance et statut.
- Statuts licence : `DRAFT`, `APPROVED`, `SUSPENDED`, `REVOKED`, `EXPIRED`. Une release ne devient `PUBLISHED` que si licence, entitlement et décision privacy sont compatibles.
- Privacy : DPR ne décide pas seul de la distribution. Chaque release référence un `PrivacyDistributionDecision` CNS.
- Classes de sortie : `PUBLIC-NONPERSONAL`, `AGGREGATED`, `ANONYMIZED`, `RESTRICTED-DERIVED`, `NOT-DISTRIBUTABLE`.
- PrivacyDistributionDecision : finalité, catégories sources, territoires, méthode de transformation, quasi-identifiants examinés, généralisation/suppression, tests de réidentification applicables, restrictions, validité, décision CNS et version.
- Règle : données personnelles brutes, identifiants directs, données sensibles et datasets sans droits suffisants sont `NOT-DISTRIBUTABLE` par défaut. L’agrégation seule ne change pas automatiquement le statut privacy.
- IAM : organisations autorisées, interne contrôlé et M2M. Exposition EXT gouvernée; entitlement BIL obligatoire lorsque prévu.
- Dépendances : ANL/DAT, BIL, CNS.
- Panne : fail-closed si licence, privacy ou entitlement non vérifiable; release publiée reste immuable mais son accès peut être suspendu/révoqué.
- Sécurité : aucune commercialisation de données personnelles; provenance et manifest obligatoires.
- Repo : `brendolys-ydiase-data-product`.
- Gates Contract Registry : `CLOSED` pour DPR-LICENSING et DPR-PRIVACY-AGGREGATION.
- Gates préproduction/release : nomination nominative owner/suppléant, paramètres statistiques propres au dataset, validation Country Framework, SLO/RPO/RTO et restore test.