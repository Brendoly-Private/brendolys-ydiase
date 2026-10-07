---
document_id: "YD-DOC-PRD-FND-013"
title: "Doctrine de pérennité — BRENDOLYS YDIASE"
document_type: "durability-doctrine"
document_role: "Établit les invariants de pérennité, gouvernance sémantique, migration, réversibilité et transmission institutionnelle de YDIASE."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "normative"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "product"
---

# Doctrine de pérennité — BRENDOLYS YDIASE

> **Rôle du document**
> Établit les invariants de pérennité, gouvernance sémantique, migration, réversibilité et transmission institutionnelle de YDIASE.
> **Usage développement :** référence obligatoire pour les conceptions et décisions relevant de son périmètre.

Statut : `BASELINE-CANDIDATE`
Autorité : fondation produit transverse
Horizon : indéfini

## 1. Objet

YDIASE doit pouvoir survivre à plusieurs générations d'équipes, d'organisations, de technologies, de cadres nationaux et de modèles économiques. Cette doctrine ne prétend pas qu'un logiciel, une base, une architecture ou une interface restera inchangé pendant des siècles. Elle impose au contraire que le produit puisse évoluer, migrer et remplacer ses composants sans perdre son identité fonctionnelle, son historique légitime ni la signification de ses concepts.

La pérennité porte d'abord sur la sémantique, la gouvernance, la traçabilité et la capacité de migration. Elle ne sacralise aucune technologie actuelle.

## 2. Invariants de conception

### 2.1 Métier avant technologie

Un concept YDIASE ne doit pas être défini par Kafka, Kubernetes, REST, SQL, un fournisseur cloud, un moteur IA ou une autre technologie. Les technologies implémentent des décisions métier et peuvent être remplacées.

### 2.2 Sémantique gouvernée

Les notions de personne, institution, formation, qualification, module, compétence, métier, opportunité, territoire, source, décision et autres concepts durables possèdent une définition métier gouvernée séparément de leur représentation informatique.

Un changement de sens exige version, justification, analyse d'impact et règle de compatibilité ou migration.

### 2.3 Identifiants durables

Les entités durables utilisent des identifiants stables qui ne sont pas réutilisés après retrait. Un changement de nom, de code externe, de fournisseur ou de stockage ne doit pas créer artificiellement une nouvelle identité lorsque l'objet métier reste le même.

Les identifiants externes sont des correspondances, pas l'identité interne unique de YDIASE.

### 2.4 Temporalité native

Lorsque le domaine le requiert, YDIASE distingue au minimum :

- période de validité métier
- moment d'observation ou de collecte
- moment d'enregistrement dans YDIASE
- version de la représentation

Le système doit pouvoir répondre à des questions historiques sans présenter une donnée ancienne comme actuelle.

### 2.5 Historique gouverné

Une modification ne doit pas effacer automatiquement l'état antérieur lorsqu'il possède une valeur analytique, probatoire ou métier légitime. La conservation reste soumise aux droits applicables, aux règles de rétention, à la minimisation et aux obligations d'effacement.

### 2.6 Provenance durable

Toute donnée qui influence une décision, une analyse ou une recommandation importante doit pouvoir conserver ou retrouver sa source, son contexte, sa date, sa version, ses transformations pertinentes, ses droits d'usage et son niveau de confiance lorsque ces informations sont requises.

### 2.7 Référentiels évolutifs

Les systèmes éducatifs, métiers, compétences, qualifications, territoires, langues, monnaies et classifications évoluent. YDIASE doit supporter coexistence de versions, équivalences, remplacements, scissions, fusions et correspondances sans réécrire l'histoire.

### 2.8 Multi-pays natif

Aucun concept central ne doit supposer que les structures administratives, diplômes, calendriers, langues, monnaies ou règles du Burkina Faso sont universels. Le Country Framework porte les variations nationales et territoriales.

### 2.9 Interopérabilité sans dépendance identitaire

YDIASE peut mapper ses concepts vers des référentiels, standards et systèmes externes. Aucun référentiel externe ne devient automatiquement l'identité interne définitive d'un concept YDIASE.

### 2.10 Réversibilité technique

Runtime, datastore, broker, moteur de recherche, moteur analytique, infrastructure, protocole, fournisseur, bibliothèque et modèle IA doivent rester remplaçables selon des procédures documentées.

Une décision technique difficilement réversible doit expliciter son coût de sortie, sa stratégie de migration et les données ou contrats concernés.

### 2.11 Contrats évolutifs

Les API, événements, projections, formats d'échange et schémas doivent prévoir versionnement, compatibilité, dépréciation et retrait. Une évolution incompatible exige une stratégie de migration et une période de coexistence lorsque le contexte l'exige.

### 2.12 Domaines remplaçables et frontières révisables

Les domaines métier constituent la référence fonctionnelle. Les bounded contexts, microservices et composants plateforme sont des traductions architecturales révisables.

Aucun nombre de microservices, de capacités ou de composants n'est un invariant produit.

### 2.13 IA non autoritative et remplaçable

Aucun modèle IA ne constitue la mémoire institutionnelle ou la source de vérité de YDIASE. Modèles, fournisseurs, techniques de retrieval, prompts et méthodes d'évaluation peuvent être remplacés.

Les sorties importantes doivent rester rattachables aux données, politiques, modèles et versions nécessaires à leur audit selon le niveau de risque.

### 2.14 Reconstruction et migration

Les mécanismes de reconstruction, export, import, migration, archivage, restauration et retrait sont des préoccupations normales du cycle de vie. Une donnée ou projection critique ne doit pas dépendre d'un format impossible à extraire ou à reconstruire sans justification approuvée.

### 2.15 Dégradation contrôlée

Une panne d'une capacité non indispensable ne doit pas rendre tout YDIASE inutilisable. Les domaines et services critiques définissent leur comportement dégradé, leurs dépendances minimales et leurs conditions de reprise.

### 2.16 Transmission institutionnelle

Une équipe future doit pouvoir comprendre la finalité d'une capacité, la signification d'une donnée, l'origine d'une décision et les conséquences d'un changement sans dépendre de la mémoire orale des fondateurs ou développeurs initiaux.

La documentation, les registres, décisions et contrats constituent une mémoire institutionnelle gouvernée.

## 3. Invariants qui ne doivent pas être confondus avec des implémentations

Sont durables : finalités produit validées, définitions métier gouvernées, provenance requise, règles d'autorité, identité stable, temporalité, droits, décisions documentées et capacité de migration.

Ne sont pas durables par défaut : nombre de microservices, langage de programmation, base de données, orchestration, bus d'événements, format d'API, modèle IA, fournisseur, structure d'écran ou topologie d'hébergement.

## 4. Gates de pérennité

Toute décision structurante doit répondre, selon son impact, aux questions suivantes :

1. Quel concept métier cette décision sert-elle ?
2. Quel élément deviendrait difficile à remplacer ?
3. Les données restent-elles exportables et interprétables ?
4. L'historique reste-t-il compréhensible après migration ?
5. Les identifiants restent-ils stables ?
6. Les contrats peuvent-ils évoluer sans rupture incontrôlée ?
7. La décision suppose-t-elle à tort un pays, une langue ou une classification universelle ?
8. Existe-t-il une stratégie de sortie ou reconstruction ?
9. Quelles preuves et métadonnées doivent survivre au remplacement ?
10. Une équipe future peut-elle comprendre la décision sans connaître ses auteurs ?

Une décision qui échoue à un gate pertinent doit être corrigée, justifiée par ADR ou classée `TBD-BLOCKING` lorsque le risque empêche réellement la suite.

## 5. Application aux couches YDIASE

- `00-foundation/governance` gouverne la transmission, les décisions et l'historique documentaire.
- `01-product/foundation` protège les invariants produit et cette doctrine.
- `02` à `11` définissent des concepts métier durables et leurs évolutions.
- `12-data-knowledge-intelligence` porte provenance, temporalité, reconstruction, connaissance et évolution des modèles analytiques/IA.
- `03-systems` traduit les domaines en frontières révisables et technologies remplaçables.
- `14-securite-conformite` encadre les droits, restrictions et évolutions réglementaires.
- `15-exploitation-resilience` définit sauvegarde, restauration, migration, continuité et retrait.
- `16-country-frameworks` isole les variations nationales.
- `01-product/roadmap` décide quand une capacité est activée sans modifier sa définition cible.

## 6. Effet sur D3

Les 51 frontières D3 restent `STABLE-CANDIDATE`. Elles ne deviennent pas des invariants de long terme. Les revues des domaines 02 à 11 peuvent imposer une fusion, une scission, une création ou un retrait si la sémantique métier ou la pérennité le justifie.

Le coût du travail déjà réalisé ne constitue jamais un motif suffisant pour conserver une frontière incorrecte.

## 7. Validation

Cette doctrine devient `ACTIVE` avec la validation du dossier 01. Toute exception future doit être documentée, limitée dans le temps ou le périmètre, et accompagnée d'une stratégie de sortie lorsqu'elle crée une dépendance durable.