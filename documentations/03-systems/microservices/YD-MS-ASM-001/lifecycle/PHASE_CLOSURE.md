# YD-MS-ASM-001 — Baseline C1

Statut : `DOCUMENTATION-BASELINE-C1 / SEMANTICS-DEFINED`
Nature : `AUTH`
Criticité : `C1`

## Autorité
Assessment possède sessions/réponses/résultats et méthodologies versionnées. Un résultat n'est ni UserSkill ni diagnostic universel.

## Politique normative
Voir `ASSESSMENT_RESULT_POLICY.md`.

## Invariants C1
- données de profilage minimisées et finalisées ;
- contrôle objet/horizontal obligatoire ;
- support interne explicitement autorisé et audité ;
- CNS fail-closed lorsque la finalité exige une décision Privacy vérifiable ;
- historique/versionnement non destructif ;
- services sources/consommateurs ne sont jamais des backups ;
- backup/restore propre au microservice.

## Avant ACTIVE
- méthodes/pondérations métier réellement validées selon le service ;
- règles mineurs/représentation ;
- Privacy/rétention ;
- IAM physique et tests IDOR ;
- BIA, RPO/RTO/SLO ;
- backup/restore policy et restore test ;
- contrats physiques ;
- audit et runbooks liés à l'implémentation.

Statut final : `C1-BASELINE-ESTABLISHED — ASSESSMENT-SEMANTICS-CLOSED / VALIDATION-PRIVACY-PREPROD-PENDING`.
