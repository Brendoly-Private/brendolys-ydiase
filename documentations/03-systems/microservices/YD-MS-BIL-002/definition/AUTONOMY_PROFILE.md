---
document_id: "YD-DOC-AUTO-9BA7D555FBB60D02"
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

# YD-MS-BIL-002 — Billing

Statut : `autonomy-profile-draft`

- Autorité : comptes de facturation, factures, opérations et références de transaction; provider reste source de ses confirmations externes.
- C1, backup AUTH. C payeur, I finance autorisée, M2M.
- Dépendances : payment providers, BIL-001.
- Panne : idempotence, queue et réconciliation; jamais double débit; état ambigu non converti en succès.
- Sécurité : données de paiement minimisées/tokenisées via provider, secrets isolés, audit financier.
- Repo : `brendolys-ydiase-billing`.
- Gate : providers, ledger/invariants, réconciliation, SLO/RPO/RTO, restore, exigences réglementaires pays.