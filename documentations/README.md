# BRENDOLYS YDIASE — Documentation

Cette documentation définit BRENDOLYS YDIASE avant sa réalisation. Elle décrit la cible panafricaine complète, puis organise son activation progressive, notamment le pilote Burkina. La documentation sépare strictement vision cible, domaine métier, service logique, frontière physique, implémentation, déploiement et activation.

## Ordre de lecture

1. `01-fondations-produit/CHARTE_FONDATRICE.md`
2. `GLOSSAIRE_METIER.md`
3. `00-gouvernance-documentaire/CHARTE_DOCUMENTAIRE.md`
4. `REGISTRE_DOCUMENTAIRE.md`
5. cartes des domaines `02` à `11`
6. `12-data-knowledge-analytics-ai/`
7. `13-architecture/ARCHITECTURE_CIBLE.md`
8. `13-architecture/SERVICE_MAP.md`
9. `13-architecture/DDD_REVIEW.md`
10. `13-architecture/DATA_OWNERSHIP_MATRIX.md`
11. `13-architecture/DEPENDENCY_MAP.md`
12. `13-architecture/EVENT_MAP.md`
13. `13-architecture/MICROSERVICE_BOUNDARY_REVIEW.md`
14. `13-architecture/SENSITIVE_MERGER_REVIEW.md`
15. `13-architecture/MICROSERVICE_AUTONOMY_STANDARD.md`
16. sécurité, exploitation, country frameworks et roadmap `14` à `17`

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

Le dossier `13-architecture/services/` documente les services logiques. `13-architecture/microservices/` documente les frontières métier physiques. `13-architecture/platform-components/` documente les composants autonomes transverses.

## États documentaires

`DRAFT → IN_REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Les états `REJECTED` et `SUPERSEDED` terminent ou remplacent une proposition. Un élément remplacé doit lier son successeur.

## Principe directeur

Documenter la cible ne signifie pas la construire immédiatement. YDIASE connaît les capacités, services logiques et frontières physiques qu’il vise, puis décide séparément quand les spécifier davantage, les développer, les déployer et les activer.
