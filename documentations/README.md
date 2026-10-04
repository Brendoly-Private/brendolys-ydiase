# BRENDOLYS YDIASE — Documentation

Cette documentation définit BRENDOLYS YDIASE avant sa réalisation. Elle décrit la cible panafricaine complète, puis organise son activation progressive, notamment le pilote Burkina. La documentation sépare strictement la vision cible, la maturité documentaire, l’implémentation, le déploiement et l’activation.

## Ordre de lecture

1. `01-fondations-produit/CHARTE_FONDATRICE.md`
2. `GLOSSAIRE_METIER.md`
3. `00-gouvernance-documentaire/CHARTE_DOCUMENTAIRE.md`
4. `REGISTRE_DOCUMENTAIRE.md`
5. Les cartes des domaines `02` à `11`
6. `13-architecture/ARCHITECTURE_CIBLE.md`
7. `13-architecture/SERVICE_MAP.md`
8. Les capacités transversales et la roadmap `12` à `17`

## Règles de référence

- Seul un document `ACTIVE` peut servir de référence normative.
- Toute exigence, décision, risque, hypothèse, source, capacité, domaine, service, événement et API porte un identifiant stable lorsqu’un registre correspondant existe.
- Un document `SUPERSEDED` pointe vers son successeur. Un brouillon ne constitue jamais une référence normative.
- L’architecture cible est documentée indépendamment du périmètre activé à court terme.
- Tout service cible identifié reçoit immédiatement une fiche documentaire minimale, même si son implémentation ou son activation intervient plusieurs années plus tard.
- Un service candidat peut être identifié après définition de son domaine, de sa responsabilité principale, de ses frontières initiales et de l’ownership de ses données. Les contrats détaillés ne sont pas un prérequis à son identification.
- Les API, événements et workflows deviennent progressivement normatifs lorsque les frontières et dépendances du service sont validées.
- Aucun choix technologique lourd n’est imposé sans ADR, justification et conditions d’activation.

## États documentaires

`DRAFT → IN_REVIEW → APPROVED → ACTIVE → DEPRECATED → RETIRED`

Les états `REJECTED` et `SUPERSEDED` terminent ou remplacent une proposition. Un élément remplacé doit lier son successeur.

## Principe directeur

Documenter la cible ne signifie pas la construire immédiatement. YDIASE doit connaître les capacités et services qu’il vise à terme, puis décider séparément quand les documenter davantage, les développer, les déployer et les activer.
