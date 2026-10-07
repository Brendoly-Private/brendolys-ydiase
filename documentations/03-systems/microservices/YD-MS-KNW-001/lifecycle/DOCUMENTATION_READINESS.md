# YD-MS-KNW-001 — Documentation Readiness

Statut : `DOCUMENTATION-READY / K5-EXECUTION-BLOCKED-BY-IMPLEMENTATION`

## Objet

Déterminer si la connaissance nécessaire à l'implémentation de KNW-001 est suffisamment structurée pour qu'une équipe puisse commencer le développement sans inventer ses frontières métier, ses invariants ou ses obligations de gouvernance.

Ce document n'autorise ni production ni déclaration K5.

## État des niveaux

| Niveau | État | Référence |
|---|---|---|
| K0 — Identifié | CLOSED | identité stable YD-MS-KNW-001 |
| K1 — Cadré | CLOSED | AUTONOMY_PROFILE |
| K2 — Relié | CLOSED | relations/dépendances canoniques |
| K3 — Contractualisé | PASS | K3_CONTRACT_BASELINE |
| K4 — Gouverné | PASS | K4_GOVERNANCE_BASELINE |
| K5 — Vérifié | NOT-YET-PASS | K5_EVIDENCE_MATRIX |
| K6 — Opérationnel | NOT-APPLICABLE-YET | nécessite implémentation/déploiement applicable |

## Paquet documentaire disponible

### Définition système
- profil d'autonomie ;
- lifecycle/phase closure ;
- politique de projection Knowledge Graph ;
- ADR de nature DERIVED.

### Contrats
- baseline K3 ;
- contrat KNW vers Search ;
- spécification des contract tests K5.

### Trust et gouvernance
- baseline K4 ;
- spécification de vérification sécurité K5.

### Opérations
- runbook ;
- protocole FULL_REBUILD ;
- plan d'exécution K5.

### Preuves
- matrice K5 ;
- modèle Evidence Record ;
- harness logique initial.

## Ce qu'une implémentation ne doit pas réinventer

- KNW reste DERIVED et reconstructible ;
- aucune vérité métier primaire n'est créée par KNW ;
- les IDs métier sources restent canoniques ;
- provenance et versions sont conservées ;
- SOURCE-ASSERTED, DETERMINISTIC-DERIVED, INFERRED et CURATED-GRAPH restent distingués ;
- DELETE/WITHDRAW/REVOKE se propagent ;
- PII absente du graphe partagé par défaut ;
- Search primaire ne dépend pas de KNW ;
- FULL_REBUILD, PARTIAL_REBUILD et CATCH_UP restent des capacités requises ;
- un cache/consommateur ne devient jamais autorité de secours.

Toute modification de ces invariants exige une décision/ADR et une analyse d'impact documentaire.

## Décisions laissées à l'implémentation

Les choix suivants restent ouverts tant qu'ils respectent les invariants :
- datastore graphe ;
- broker/transport ;
- format physique des contrats ;
- langage/framework ;
- orchestration des rebuilds ;
- mécanisme IAM ;
- observabilité technique ;
- stratégie physique snapshot/replay ;
- seuils numériques de performance, freshness, RTO/RPO et rétention.

Ces choix ne doivent pas être introduits dans les documents métier comme s'ils étaient déjà décidés.

## Conditions avant K5 PASS

L'équipe d'implémentation devra fournir les représentations contractuelles testables, les contrôles de sécurité réels, un environnement de test, des fixtures/datasets versionnés et les mécanismes de reconstruction. Les protocoles K5 seront alors exécutés et les Evidence Records remplis.

## Verdict

La documentation de KNW-001 est suffisamment structurée pour un handoff vers l'implémentation :

`DOCUMENTATION-READY`.

Le niveau de connaissance reste :

`K4-PASS / K5-NOT-YET-PASS`.

Aucune documentation supplémentaire ne doit être créée uniquement pour simuler des preuves qui dépendent du logiciel. Les prochains documents KNW doivent répondre soit à une décision réelle d'implémentation, soit à une preuve K5 exécutée, soit à un changement de périmètre.
