# Gates et inconnues — Identité et profils

Statut : `DOMAIN-REVIEW-CANDIDATE`

## Gates avant activation du domaine

| Gate | État | Condition |
|---|---|---|
| sémantique Person/Profile | `DEFINED` | modèle durable documenté |
| identité interne stable | `DEFINED` | `PersonRef` indépendant des identifiants externes |
| temporalité | `DEFINED` | validité, observation, enregistrement et version distingués |
| provenance/preuve | `DEFINED` | déclaration, preuve, vérification et contradiction distinguées |
| visibilité vs privacy | `DEFINED` | responsabilités séparées |
| cycle de vie | `DEFINED` | fermeture IAM ≠ suppression métier |
| PRF-001 / PRF-002 physique | `DEFINED` | deux frontières autonomes confirmées par ADR le 2026-10-05 |
| mineurs et représentation | `TBD-PREPROD` | Country Framework Burkina + conformité |
| règles de rétention par catégorie | `TBD-PREPROD` | politique Privacy/Conformité |
| méthode de fusion/séparation de personnes | `TBD-PREPROD` | seuils de preuve et procédure opérationnelle |
| export/portabilité | `TBD-PREPROD` | formats et périmètre après Privacy + Contracts |
| modèle de décès/incapacité | `TBD-PREPROD` | uniquement si besoin métier/juridique validé |

## Décision PRF

`PRF-001` et `PRF-002` restent deux responsabilités logiques et deviennent deux frontières physiques cibles : `YD-MS-PRF-001` et `YD-MS-PRF-002`.

Le gate `ADR-REQUIRED` est fermé. Toute future fusion exige un nouvel ADR.

## Inconnues acceptées

- technologie de stockage
- modèle physique des tables/documents
- protocole d'API
- mécanisme d'événement
- format d'export final
- fournisseur IAM futur
- nombre physique final de microservices du domaine après évolutions futures

Ces inconnues ne bloquent pas la définition métier.

## Blocage actuel

Aucun `TBD-BLOCKING` n'est ouvert pour poursuivre la documentation des domaines.

## Condition de validation du domaine 02

Le domaine peut passer `ACTIVE` après confrontation avec Education, Skills, Guidance et Privacy. Jusque-là, il reste `DOMAIN-BASELINE-CANDIDATE`.