# YD-MS-DAT-002 — Data Governance — Baseline C2

Statut : `DOCUMENTATION-BASELINE-C2 / ACQUISITION-RAW-SEMANTICS-CLOSED`

## Politique normative
Voir `DATA_GOVERNANCE_POLICY.md`.

## Chaîne de confiance
DAT-001 gouverne source/droits ; DAT-002 capture acquisition/raw ; DAT-003 porte provenance/lineage ; DAT-004 évalue qualité/validation ; DAT-005 gouverne les référentiels transversaux. Aucun de ces services ne devient par copie owner des objets EDU, SKL, CAR, LAB ou autres domaines.

## Invariants
- versionnement et historique non destructif ;
- provenance/attribution préservée ;
- UNKNOWN/NOT-ASSESSABLE ne deviennent jamais validation positive ;
- absence d'autorisation requise bloque la nouvelle acquisition ;
- raw n'est jamais vérité métier ;
- validation ne transfère pas l'ownership métier ;
- projections/consommateurs ne sont jamais backups de l'autorité DAT.

## Avant ACTIVE
connecteurs réels, quotas, politique raw/replay/rétention, SLO/RPO/RTO et restore.

Statut final : `C2-BASELINE-ESTABLISHED — ACQUISITION-RAW-SEMANTICS-CLOSED / IMPLEMENTATION-AND-EVIDENCE-PENDING`.
