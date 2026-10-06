# BRENDOLYS YDIASE — Documentation

Cette documentation définit BRENDOLYS YDIASE avant sa réalisation. Elle décrit la cible panafricaine complète, puis organise son activation progressive, notamment le pilote Burkina. La documentation sépare strictement vision cible, domaine métier, service logique, frontière physique, implémentation, déploiement et activation.

## Ordre de lecture

1. `00-foundation/`
2. `01-product/`
3. `02-domains/`
4. `03-systems/architecture/`
5. `04-contracts/`
6. `05-decisions/`
7. `06-trust/`
8. `07-operations/`
9. `08-countries/`
10. `_meta/` pour les mécanismes de validation et de connaissance.

## Règles de référence

- Seul un document `ACTIVE` sert de référence normative finale.
- Toute exigence, décision, risque, hypothèse, source, capacité, domaine, service logique, frontière physique, événement et API porte un identifiant stable lorsqu’un registre correspondant existe.
- Un document `SUPERSEDED` pointe vers son successeur. Un brouillon ne constitue jamais une référence normative.
- L’architecture cible reste indépendante du périmètre activé à court terme.
- Tout service logique cible reçoit une fiche documentaire minimale, même si son implémentation intervient plus tard.
- Toute frontière physique confirmée reçoit un profil d’autonomie distinct de la fiche du service logique.
- Les API, événements et workflows deviennent progressivement normatifs lorsque frontières et dépendances sont validées.
- Aucun choix technologique lourd n’est imposé sans ADR, justification et conditions d’activation.

## Distinction obligatoire

`Domaine métier ≠ capacité ≠ service logique ≠ microservice physique ≠ composant de plateforme ≠ infrastructure`.

Le dossier `03-systems/services/` documente les services logiques. `03-systems/microservices/` documente les frontières métier physiques. `03-systems/platform-components/` documente les composants autonomes transverses.

## États documentaires

`DRAFT → IN_REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Les états `REJECTED` et `SUPERSEDED` terminent ou remplacent une proposition. Un élément remplacé doit lier son successeur.

## Principe directeur

Documenter la cible ne signifie pas la construire immédiatement. YDIASE connaît les capacités, services logiques et frontières physiques qu’il vise, puis décide séparément quand les spécifier davantage, les développer, les déployer et les activer.
