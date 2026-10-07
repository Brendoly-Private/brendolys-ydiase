# YD-MS-PRF-002 — Privacy Requirements Map

Statut : GOVERNANCE-MAP / PREPROD-CLOSURES-PENDING

CNS-001 reste l'autorité des décisions Privacy. Cette carte ne crée aucune règle concurrente.

| ID | Exigence | État |
|---|---|---|
| PRF2-PRIV-001 | finalité/décision CNS déterminable | DEFINED |
| PRF2-PRIV-002 | fail-closed si décision obligatoire non vérifiable | DEFINED |
| PRF2-PRIV-003 | minimisation des projections et preuves diffusées | DEFINED |
| PRF2-PRIV-004 | contrôle horizontal/self | DEFINED / PHYSICAL-TEST-PENDING |
| PRF2-PRIV-005 | séparation déclaration/vérification/support | DEFINED / PHYSICAL-TEST-PENDING |
| PRF2-PRIV-006 | audit des accès et mutations sensibles | DEFINED / IMPLEMENTATION-PENDING |
| PRF2-PRIV-007 | rectification sans réécriture silencieuse | DEFINED |
| PRF2-PRIV-008 | réapplication Privacy après restore | DEFINED / DR-TEST-PENDING |
| PRF2-PRIV-009 | non-réactivation durable après suppression/restriction | DEFINED / DR-TEST-PENDING |
| PRF2-PRIV-010 | rétention par catégorie/pays/finalité | TBD-PREPROD |
| PRF2-PRIV-011 | portabilité/export gouvernés | TBD-PREPROD |
| PRF2-PRIV-012 | règles mineurs/représentation | TBD-PREPROD |
| PRF2-PRIV-013 | conflit conservation probatoire/effacement | TBD-PREPROD |
| PRF2-PRIV-014 | destruction/rétention des backups | TBD-PREPROD |
| PRF2-PRIV-015 | minimum nécessaire pour consommateurs | DEFINED |

## Gate
Avant activation, les TBD-PREPROD doivent être fermés ou recevoir une non-applicabilité formellement justifiée. Les contrôles physiques sont vérifiés à K5/PREPROD.

Une réussite de restore sans réapplication Privacy ne peut pas constituer un PASS de résilience PRF-002.

## Verdict
La Privacy est intégrée à la frontière, aux contrats et au recovery. Les gaps restants portent principalement sur rétention, portabilité, règles pays/mineurs et preuves d'exécution.
