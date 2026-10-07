# YDIASE — Protocole de profondeur documentaire et Development Readiness

Statut : NORMATIVE-GOVERNANCE

## Objet
Éviter de confondre fermeture de frontière pré-implémentation et conception complète d'un microservice.

DOCUMENTATION-READY signifie que la frontière, K3/K4 et le plan de preuve sont suffisamment cadrés pour poursuivre la conception. Cela ne signifie pas que toutes les fonctionnalités sont prêtes à coder.

## Profondeur obligatoire
Chaque microservice cible progresse par couches :
1. frontière et ownership ;
2. modules/capacités internes ;
3. fonctionnalités ;
4. cas d'usage et scénarios ;
5. données, entrées/sorties et contrats ;
6. méthodes/algorithmes lorsque la logique le justifie ;
7. exigences non fonctionnelles et capacité ;
8. architecture technique cible ;
9. sécurité, Privacy et résilience ;
10. observabilité/opérations ;
11. stratégie de tests et critères d'acceptation ;
12. plan d'implémentation et dépendances.

Une simple opération CRUD n'exige pas artificiellement un document d'algorithme. Une fonction de scoring, matching, recommandation, détection, optimisation, ranking ou inférence doit expliciter méthode, entrées, sorties, paramètres, limites, métriques et tests.

## Spécification d'une fonctionnalité
Chaque fonctionnalité documente au minimum : objectif, acteurs, préconditions, entrées, validations, règles métier, traitement, état lu/écrit, sorties, événements, erreurs, autorisation, Privacy, idempotence/concurrence si applicable, observabilité, dépendances et tests d'acceptation.

## Architecture technique
La technologie vient après le besoin. La séquence normative est :
fonctionnel → données/flux → NFR/capacité/sécurité → alternatives → ADR → architecture cible → contrats physiques → plan d'implémentation.

Aucune technologie Big Data n'est imposée uniquement pour paraître scalable.

## Readiness incrémentale
FEATURE-READY-FOR-DEVELOPMENT : fonctionnalité sans UNKNOWN bloquant dans son périmètre, contrats/données nécessaires définis, décisions techniques applicables acceptées, sécurité/Privacy traitées, tests d'acceptation définis et dépendances identifiées.

MODULE-READY-FOR-DEVELOPMENT : toutes les fonctionnalités nécessaires au module pour le scope considéré sont ready et leurs interactions sont cohérentes.

MICROSERVICE-READY-FOR-DEVELOPMENT : architecture interne, modules du scope cible, contrats, NFR, sécurité, opérations, tests et séquence d'implémentation sont cohérents et sans gap bloquant.

TARGET-DESIGN-COMPLETE : tous les microservices/capacités de la cible produit ont atteint le niveau de conception exigé, y compris ceux dont l'activation est différée.

## Activation
L'activation est un axe séparé. Une fonctionnalité peut être CONCEIVED puis IMPLEMENTED/DEPLOYED tout en restant INACTIVE. Le mécanisme d'activation doit être gouverné, observable, réversible lorsque possible et ne jamais contourner IAM, Privacy ou les contrats.

## Traçabilité
Besoin/domaine → microservice → module → fonctionnalité → use case → contrat/donnée → ADR/architecture → test → preuve.

La duplication de vérité métier entre ces couches est interdite : les documents détaillés référencent les sources canoniques.

## Relation K0-K6
K0-K6 mesure la maturité de connaissance et de preuve. Les statuts READY-FOR-DEVELOPMENT mesurent la complétude nécessaire au développement. Ils sont complémentaires et ne se remplacent pas.

K5/K6 ne sont jamais attribués parce qu'une spécification est détaillée. Inversement, DOCUMENTATION-READY de frontière ne vaut pas MICROSERVICE-READY-FOR-DEVELOPMENT.
