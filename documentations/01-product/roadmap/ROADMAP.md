# Roadmap de référence

## Principe

La roadmap décrit l’ordre logique d’activation de YDIASE. Elle ne réduit pas l’architecture cible aux seules capacités de la phase courante.

Les phases expriment des paliers de capacité. Elles ne constituent pas des dates contractuelles. Une phase ne démarre que lorsque ses critères d’entrée sont satisfaits.

## Phases

| Phase | But | Sortie attendue |
|---|---|---|
| P0 | Fondation documentaire | Vision, gouvernance, domaines, capacités, architecture cible, Service Map et règles de traçabilité cohérentes |
| P0.1 | Architecture fonctionnelle cible | Inventaire des capacités, bounded contexts, produits/interfaces, moteurs d’intelligence, modèle Data conceptuel, services candidats, dépendances et phases cibles |
| P1 | Pilote Burkina | Socle identité, référentiels prioritaires, données Burkina validées, sécurité, Country Framework et premières fonctions utilisables |
| P2 | Orientation et compétences | Capacités d’orientation, compétences, programmes et relations principales suffisamment stabilisées pour les usages retenus |
| P3 | Carrières et signaux du marché | Référentiels métiers, trajectoires et signaux du marché reliés aux compétences et formations |
| P4 | Opportunités et recrutement | Opportunités, employeurs, candidatures et capacités de mise en relation selon les décisions produit validées |
| P5 | Learning et contenus | Capacités de contenus, apprentissage et interactions associées selon les frontières métier retenues |
| P6 | Intelligence et Data Products | Analytics, moteurs d’intelligence, produits Data, API et services institutionnels ou employeurs validés |
| P7 | Extension multi-pays | Country Framework éprouvé, nouvelles juridictions et sources intégrées sans duplication de la logique centrale |
| P8 | Infrastructure panafricaine | Fédération multi-pays, gouvernance Data étendue, exploitation à grande échelle et capacités panafricaines validées |

## Règles de phase

- Une capacité peut être documentée plusieurs phases avant son activation.
- Un service peut appartenir à l’architecture cible sans être développé dans la phase courante.
- Chaque service de `SERVICE_MAP.md` porte une phase cible ou `TBD` avec une condition de décision.
- Les phases P2 à P8 restent révisables tant que les décisions produit correspondantes ne sont pas `ACTIVE`.
- Une phase ne doit pas imposer une technologie. Les choix techniques passent par ADR.
- Le pilote Burkina valide des hypothèses et des capacités. Il ne doit pas créer des règles impossibles à généraliser par le Country Framework.

## Axes suivis séparément

La phase produit, la maturité documentaire, la maturité opérationnelle et la couverture géographique ne doivent pas être confondues.

- phase : `P0–P8`
- documentation service : `D0–D6`
- maturité : `M0–M5`
- couverture : `G0–G4`

## Gate P0.1

Avant de considérer l’architecture cible comme suffisamment définie, P0.1 doit fournir au minimum :

1. inventaire des capacités YDIASE
2. carte des bounded contexts
3. catalogue des produits et interfaces
4. catalogue des moteurs d’intelligence
5. modèle Data conceptuel global
6. modèle Knowledge conceptuel
7. catalogue des pipelines Data
8. architecture Labor Market Intelligence
9. Service Map cible
10. fiche documentaire pour chaque service cible
11. Dependency Map globale
12. Event Map conceptuelle
13. rattachement des services aux phases
14. rattachement des produits et interfaces Web, mobile, desktop, portails et API
15. traçabilité entre capacités, services et modèles économiques lorsque ces derniers sont validés

La fin de P0.1 ne signifie pas que tous les contrats techniques sont figés. Elle signifie que la cible fonctionnelle et ses frontières principales sont suffisamment définies pour contrôler les décisions suivantes.
