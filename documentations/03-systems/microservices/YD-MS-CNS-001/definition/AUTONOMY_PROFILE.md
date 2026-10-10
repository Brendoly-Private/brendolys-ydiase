---
document_id: "YD-DOC-AUTO-2C038CC2FA94CDA9"
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
status: "IN_REVIEW"
---

# YD-MS-CNS-001 — Consent & Privacy

Statut : `C1-BASELINE / PRIVACY-SEMANTICS-DEFINED`

- Données possédées : PurposeGrant, consent/restriction state, privacy requests, retention rules et références de finalité. Données très sensibles.
- Datastore : autoritatif privé, migrations privées, historique nécessaire aux preuves; aucun accès DB externe.
- Backup/restore : chiffré, indépendant, test obligatoire. Une restauration doit préserver l’ordre des révocations et déclencher réconciliation des consommateurs.
- IAM : `brendolys-customers` pour droits/demandes du sujet, `brendolys-internal` pour fonctions privacy strictement autorisées, M2M pour décisions de traitement. `brendolys-networks` uniquement si une finalité réseau documentée l’exige.
- API/événements : PrivacyDecision, ConsentChanged, PrivacyRestrictionChanged, PrivacyRequested. Révocations prioritaires.
- Réseau : DNS interne; endpoints sujet via edge. Flux sortants minimaux vers Audit/Notification selon finalité. Aucun datastore public.
- Sécurité : fail-closed pour traitements non indispensables lorsque décision requise indisponible; chiffrement et audit renforcés; aucune donnée personnelle complète dans événements.
- Résilience : haute criticité candidate C1. Cache de décision révocable seulement avec borne de fraîcheur définie. Aucun fail-open par défaut.
- Scaling : clé `subject/purpose`; lectures décisionnelles séparables sans dupliquer l’autorité.
- Repo candidat : `brendolys-ydiase-consent-privacy`; workload identity, secrets, certificats et pipeline propres.
- Runbook/DR : corruption de grants, retard de révocation, indisponibilité IAM, replay d’événements, restauration et propagation des restrictions.
- Politiques normatives : `PRIVACY_DECISION_POLICY.md` et `REVOCATION_RETENTION_RECOVERY_POLICY.md`.
- Gates restant : validation juridique par pays des bases applicables/finalités, seuils mineurs, durées de rétention, RPO/RTO/SLO, audience/scopes/rôles, test restore et SLO de propagation de révocation.