# Charte documentaire — BRENDOLYS YDIASE

Statut : `ACTIVE`

## 1. Objet

Cette charte gouverne tout le corpus YDIASE. La documentation doit permettre de retrouver pourquoi une capacité existe, qui possède une règle ou une donnée, quelles décisions la traduisent et comment leur conformité est vérifiée.

## 2. Principes

- séparer produit, domaine, capacité, bounded context, microservice et infrastructure
- séparer faits, hypothèses, décisions et projections
- conserver provenance, version et historique lorsque nécessaires
- ne jamais transformer une duplication en nouvelle source autoritative
- ne jamais utiliser l'IA conversationnelle comme source de vérité
- ne jamais imposer une technologie sans décision justifiée
- concevoir la cible panafricaine tout en distinguant le pilote Burkina
- traiter la pérennité comme capacité d'évolution, de migration et de transmission, et non comme conservation indéfinie d'une implémentation

## 3. Identifiants

La nomenclature normative est définie dans `CONVENTION_IDENTIFIANTS.md`. Un identifiant n'est jamais réutilisé.

## 4. Autorité

`NIVEAUX_AUTORITE.md` définit l'autorité documentaire. Un document plus technique ne peut modifier implicitement une intention produit, une règle métier ou une politique transverse de niveau supérieur.

## 5. Traçabilité

Chaîne cible :

`vision → domaine → capacité → exigence/règle métier → bounded context → frontière autonome → donnée → contrat → vérification`.

Les liens deviennent obligatoires selon la maturité. Un objet qui atteint un gate sans les liens requis ne passe pas ce gate.

## 6. Services et frontières

- chaque service candidat possède une définition
- chaque microservice autonome et composant plateforme possède son profil d'autonomie
- une frontière future peut être documentée sans être implémentée
- la documentation ne crée pas une frontière uniquement pour compléter un catalogue
- une modification métier peut provoquer une revue d'une frontière déjà stabilisée

## 7. États non résolus

Les états autorisés sont :

- `DEFINED`
- `TBD-PREPROD`
- `ADR-REQUIRED`
- `NOT-APPLICABLE`

`TBD-BLOCKING` peut être utilisé uniquement lorsqu'un gate est réellement bloqué et doit identifier la condition de fermeture. Un `TBD` générique est interdit dans les nouveaux documents normatifs.

## 8. Cycle de vie

Le cycle est défini dans `CYCLE_VIE_DOCUMENTAIRE.md`. Les états documentaire, implémentation, déploiement et activation restent séparés.

## 9. Revue et approbation

Les règles sont définies dans `POLITIQUE_REVUE_APPROBATION.md`. Tout document normatif actif possède un owner, un suppléant ou un gate explicite pour les nommer, ainsi qu'un déclencheur de revue.

## 10. Contradictions

Toute contradiction suit `POLITIQUE_CONTRADICTIONS.md`. Aucune correction silencieuse n'est admise.

## 11. Changement et impact

Tout changement normatif suit `POLITIQUE_CHANGEMENT_IMPACT.md`. Une modification de fondations ou de domaine doit évaluer ses impacts sur les décisions techniques existantes.

## 12. Doctrine de pérennité

`../../01-product/foundation/vision-strategy/DOCTRINE_PERENNITE.md` constitue une contrainte fondatrice transverse dès sa validation avec le dossier `01-product/`.

Toute création ou révision importante de domaine, capacité, modèle de données, frontière, contrat, infrastructure, politique de sécurité, procédure d'exploitation ou Country Framework doit évaluer les gates de pérennité pertinents.

En particulier :

- une implémentation ne devient jamais un invariant produit par simple ancienneté
- une décision technique structurante doit examiner sa réversibilité et sa stratégie de sortie
- un changement sémantique doit rester versionné et traçable
- les identifiants durables ne sont pas réutilisés
- l'historique utile doit rester interprétable après migration, sous réserve des obligations de suppression et rétention
- les 51 frontières D3 ne bénéficient d'aucune protection contre une correction métier justifiée
- le coût déjà engagé n'est pas une preuve de validité architecturale

Une exception qui crée une dépendance durable doit être explicitement documentée et gouvernée.

## 13. Prudence

La documentation n'invente pas API, événement, seuil, technologie, obligation réglementaire, donnée, owner ou dépendance pour remplir un modèle. Les choix non décidés restent gouvernés selon leur nature.

## 14. Critère de validité

Un document est utilisable comme référence uniquement si son statut, son autorité, sa version et son périmètre permettent cet usage. La présence dans le dépôt ne suffit pas.