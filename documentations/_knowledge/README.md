# YDIASE Knowledge Architecture

Ce répertoire porte la couche structurée de connaissance de BRENDOLYS YDIASE.

## Rôle

La couche `_knowledge` complète la documentation existante sans déplacer, supprimer ni renommer les documents actuels pendant K1.

Elle fournit :

- une ontologie commune pour les objets YDIASE
- des relations contrôlées entre ces objets
- un cycle de vie commun
- des schémas destinés à la validation future du catalogue
- une base exploitable par les humains, les outils et les agents IA

## Règle d'autorité

Un objet structuré ne remplace pas automatiquement une source normative existante. Tant que la migration n'a pas été validée, les documents existants conservent leur autorité. Les entrées `_knowledge` référencent ces sources et préparent leur transformation en vues structurées ou générées.

## Niveaux

- L0 Organisation : vision, principes, objectifs, parties prenantes
- L1 Métier : domaines, concepts, capacités, règles, cas d'usage
- L2 Systèmes : regroupements cohérents de capacités et responsabilités
- L3 Composants : services logiques, microservices, composants plateforme, applications et pipelines
- L4 Contrats et runtime : API, événements, commandes, requêtes et protocoles
- Gouvernance transverse : exigences, décisions, politiques, risques, contrôles et preuves

## K1

K1 crée uniquement la fondation : ontologie, relations, cycle de vie et premiers schémas. Aucun découpage physique existant n'est modifié par cette étape.

## Étapes suivantes

K2 enregistrera les domaines, systèmes, services logiques, microservices et composants plateforme. Le domaine Education servira de première preuve avant généralisation.