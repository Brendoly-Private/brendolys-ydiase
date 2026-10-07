# Architecture cible documentaire

## Principe

YDIASE est défini selon la chaîne :

`Vision → domaines → capacités → bounded contexts → services cibles → dépendances → contrats → phases → activation`.

La cible décrit ce que YDIASE doit pouvoir devenir. Elle ne constitue pas un ordre de développement immédiat.

Un service documenté n’est ni développé, ni déployé, ni activé par défaut. Ces états sont suivis séparément.

## Règles d’architecture

- Les domaines métier restent la référence fonctionnelle.
- Chaque donnée possède un domaine ou système autoritatif explicite.
- Les autres services consomment des contrats, événements ou projections gouvernées au lieu de devenir propriétaires de copies concurrentes.
- Un bounded context peut contenir un ou plusieurs services. La séparation en microservices doit répondre à une frontière métier, de données, de sécurité, de scalabilité, de cycle de vie ou d’équipe identifiable.
- Aucun microservice ne doit exister uniquement pour reproduire une couche technique ou une table de base de données.
- Tout service cible identifié possède une documentation dès son entrée dans la Service Map.
- Un service futur reste documenté même si sa phase d’activation est éloignée.
- Les frontières conceptuelles précèdent les contrats détaillés. Les contrats deviennent plus précis à mesure que la maturité documentaire augmente.
- La cible panafricaine et le pilote Burkina sont deux vues du même système. Le pilote ne doit pas devenir la définition permanente de la cible.

## États indépendants

Chaque service suit au minimum quatre dimensions indépendantes :

| Dimension | Exemple |
|---|---|
| Documentation | `D0` à `D6` |
| Implémentation | `not-started`, `in-development`, `implemented` |
| Déploiement | `not-deployed`, `staging`, `production` |
| Activation | `inactive`, `pilot`, `active`, `retired` |

Un service peut donc être documenté à `D2`, rester `not-started`, `not-deployed` et `inactive`.

## Niveaux de documentation

| Niveau | Contenu minimum |
|---|---|
| D0 | Service identifié, domaine, raison d’existence et phase cible |
| D1 | Mission, responsabilités, exclusions, bounded context et frontières initiales |
| D2 | Capacités, données possédées, système autoritatif, données consommées, dépendances et criticité |
| D3 | API, commandes, queries, événements, workflows et règles d’intégration |
| D4 | Sécurité, confidentialité, résilience, observabilité, disponibilité et objectifs de performance |
| D5 | Contrats stabilisés, critères d’acceptation, stratégie de tests, migration et conditions de mise en œuvre |
| D6 | Service en production, runbook, SLO mesurés, incidents, exploitation et cycle d’évolution |

## Documentation minimale obligatoire

Dès qu’un service apparaît dans `SERVICE_MAP.md`, sa fiche doit préciser au minimum :

- identifiant stable
- nom
- domaine
- bounded context initial
- statut architectural
- phase cible
- mission
- responsabilités principales
- exclusions principales
- données dont il est propriétaire ou indication explicite qu’il n’en possède aucune
- dépendances déjà connues
- condition générale d’activation
- états documentation, implémentation, déploiement et activation

L’absence de détail futur doit être écrite comme `TBD` avec une condition de résolution. Elle ne doit pas être remplacée par une décision inventée.

## Condition de passage au développement

Un service ne passe pas au développement uniquement parce qu’il figure dans l’architecture cible. Son passage exige au minimum une maturité documentaire compatible avec le risque, des frontières validées, les dépendances nécessaires, les exigences de sécurité applicables et une décision de phase explicite.


## Baseline cible complète

La définition détaillée de la cible est désormais portée par :
- `TARGET_ARCHITECTURE_BLUEPRINT.md` — domaines, frontières, microservices, flux, dépendances, Data/IA et activation ;
- `HYPERSCALE_CAPACITY_BASELINE.md` — cible 5 à 15 millions d'utilisateurs simultanément actifs et Capacity Profiles ;
- `DATA_AI_PLATFORM_ARCHITECTURE.md` — plans Data, Knowledge, Analytics, ML et IA ;
- `TARGET_FLOW_MAP.md` — flux transactionnels, événementiels, Data, IA, orientation et entrepreneuriat ;
- `SERVICE_MAP.md` — inventaire des services logiques cibles, incluant Entrepreneurship.

L'entrepreneuriat est un domaine de premier rang et non une extension informelle d'Orientation ou Employment.

## Condition de conception complète

Le statut `TARGET-DESIGN-COMPLETE` exige la conception A–Z des capacités retenues, y compris celles non activées : modules, fonctionnalités, cas d'usage, contrats, données, algorithmes applicables, NFR, Capacity Profiles, architecture technique, sécurité, résilience, opérations, tests et plan d'implémentation.
