# Capacités produit — BRENDOLYS YDIASE

Statut : `REVIEWED-CANDIDATE`

## 1. Règle

Ce catalogue décrit des capacités métier ou produit durables. Une capacité n'est ni un écran, ni une API, ni un microservice, ni une technologie. Toute capacité doit être reliée à au moins un problème, une population, une valeur et un domaine principal.

Les anciennes capacités 035 à 055 ont été revues pour retirer les formulations techniques ou de gouvernance qui ne constituent pas, seules, une capacité métier. Elles restent documentées dans les dossiers Data, Architecture, Sécurité, Exploitation ou Gouvernance lorsqu'elles représentent une exigence transversale.

## 2. Capacités cibles revues

| ID | Capacité cible | Domaine principal | Problème(s) | Population/acteur principal | Valeur |
|---|---|---|---|---|---|
| YD-CAP-001 | profil, situation, objectifs et préférences | Identity | 004,005 | individus | contexte personnel gouverné pour les décisions |
| YD-CAP-002 | établissements, centres et implantations | Education | 001,007 | individus, établissements | identifier et comparer l'offre éducative |
| YD-CAP-003 | formations, filières, diplômes et certifications | Education | 001,002 | individus, établissements | comprendre les options de formation |
| YD-CAP-004 | curricula, programmes, modules et contenus de cursus | Education | 001,002 | individus, établissements | comparer le contenu réel des formations |
| YD-CAP-005 | conditions d'accès, admissions, coûts et prérequis publiables | Education | 001,004 | individus, établissements | évaluer la faisabilité d'une option |
| YD-CAP-006 | référentiel de compétences et niveaux | Skills | 002,005 | tous | langage commun pour relier études, personnes et métiers |
| YD-CAP-007 | acquis, expériences, preuves et compétences déclarées/évaluées | Skills | 004,005 | individus, recruteurs | représenter les capacités d'une personne avec leur niveau de preuve |
| YD-CAP-008 | métiers, fonctions, familles et activités professionnelles | Careers | 002,005 | individus, organisations | comprendre les métiers et leurs relations |
| YD-CAP-009 | débouchés et relations formation-compétence-métier | Careers | 002 | individus, établissements | relier études et possibilités professionnelles |
| YD-CAP-010 | transitions, passerelles et trajectoires professionnelles | Careers | 002,005 | individus | comprendre les changements de métier possibles |
| YD-CAP-011 | observation des offres et demandes déclarées | Labor | 003 | individus, organisations, institutions | signal observable sur le travail |
| YD-CAP-012 | enquêtes et sources institutionnelles du travail | Labor | 003,010 | institutions, analystes | compléter les observations avec des sources structurées |
| YD-CAP-013 | signaux économiques, territoriaux et activité informelle qualifiée | Labor | 003,008 | individus, organisations, institutions | mieux représenter les réalités peu structurées |
| YD-CAP-014 | indicateurs et analyses du marché du travail | Labor | 003,010 | individus, organisations, institutions | interpréter les signaux sans les confondre avec une vérité exhaustive |
| YD-CAP-015 | évaluations d'intérêts, objectifs, acquis ou aptitudes selon méthode validée | Guidance | 004,005 | individus | fournir des éléments structurés pour l'orientation |
| YD-CAP-016 | orientation scolaire et universitaire | Guidance | 001,002,004 | élèves, étudiants | comparer des options d'études cohérentes avec le contexte |
| YD-CAP-017 | orientation professionnelle | Guidance | 002,004 | étudiants, diplômés, professionnels | comparer des options professionnelles |
| YD-CAP-018 | reconversion professionnelle | Guidance | 005 | professionnels | identifier des transitions réalistes et leurs écarts |
| YD-CAP-019 | adéquation profil-formation | Guidance | 004 | individus | comparer profil et exigences de formation |
| YD-CAP-020 | adéquation profil-métier | Guidance | 004,005 | individus | comparer profil et exigences métier |
| YD-CAP-021 | adéquation profil-opportunité | Guidance | 004,006 | individus | prioriser des opportunités pertinentes |
| YD-CAP-022 | recommandations, alternatives et scénarios explicables | Guidance | 004,009 | individus | décider avec raisons, limites et alternatives |
| YD-CAP-023 | écarts de compétences | Guidance/Skills | 005 | individus, organisations | identifier ce qui manque pour un objectif |
| YD-CAP-024 | plans d'évolution et de progression | Guidance/Content | 005 | individus | ordonner des actions de progression |
| YD-CAP-025 | catalogue, recherche et qualification des opportunités | Opportunities | 006 | individus | regrouper des opportunités dispersées |
| YD-CAP-026 | stages, emplois et missions | Opportunities | 006 | candidats, recruteurs | mettre en relation besoins et candidatures |
| YD-CAP-027 | bourses, concours, programmes et opportunités de développement | Opportunities | 006 | individus, partenaires | élargir les possibilités au-delà de l'emploi |
| YD-CAP-028 | candidature, dossier, statuts et suivi | Opportunities | 006 | candidats, recruteurs | suivre une démarche d'opportunité |
| YD-CAP-029 | gestion des besoins et opportunités par les organisations | Opportunities | 006,010 | recruteurs, organisations | publier et gérer les besoins selon l'offre activée |
| YD-CAP-030 | contenus éducatifs, métiers et professionnels | Content | 001,002,004 | individus, partenaires | informer et contextualiser les décisions |
| YD-CAP-031 | sélection personnalisée de contenus et opportunités | Content | 004,006 | individus | réduire le bruit informationnel |
| YD-CAP-032 | communauté, échanges et interactions | Content | 004,008 | individus, partenaires | échange d'expérience sous règles de modération |
| YD-CAP-033 | ressources de progression et apprentissage | Content | 005 | individus, partenaires formation | agir sur les écarts identifiés |
| YD-CAP-034 | sujets académiques/professionnels reliés aux compétences et objectifs | Education/Guidance | 002,004 | étudiants, établissements | choisir des travaux cohérents avec un objectif |
| YD-CAP-035 | recherche et exploration transversales des informations YDIASE | Content | 001,006 | tous | retrouver une information à travers plusieurs domaines |
| YD-CAP-036 | compréhension des relations entre entités éducatives, compétences, métiers et opportunités | Data/Knowledge | 002,010 | individus, analystes, organisations | exploiter les relations validées entre concepts |
| YD-CAP-037 | tableaux de bord, indicateurs et analyses décisionnelles | Data/Analytics | 003,010 | organisations, institutions, équipes autorisées | exploiter des mesures gouvernées |
| YD-CAP-038 | assistance intelligente contextualisée et fondée sur les connaissances autorisées | Guidance/Content | 004,009 | individus, organisations | obtenir une aide contextualisée avec sources et limites |
| YD-CAP-039 | collecte, contribution, vérification et mise à jour multi-source | Partners/Data | 008 | établissements, ambassadeurs, terrain, partenaires | constituer et maintenir des données utilisables |
| YD-CAP-040 | gestion de la relation avec les établissements et organismes de formation | Partners | 001,008 | établissements | organiser contribution, validation et collaboration |
| YD-CAP-041 | gestion de la relation avec entreprises et recruteurs | Partners | 003,006,010 | entreprises | organiser besoins, opportunités et collaboration |
| YD-CAP-042 | réseau de contributeurs, ambassadeurs et vérificateurs | Partners | 008 | réseaux terrain | étendre la collecte et la validation territoriale |
| YD-CAP-043 | adaptation fonctionnelle par pays, territoire, langue et classification | transversal | 007 | tous | utiliser YDIASE dans des contextes nationaux différents |
| YD-CAP-044 | offres, abonnements, accès et droits commerciaux | Economy | 010 | individus, organisations | proposer des niveaux de service contrôlés |
| YD-CAP-045 | commandes, facturation, paiements et suivi commercial | Economy | 010 | clients, BRENDOLYS INTELLIGENCE | opérer les revenus du produit |
| YD-CAP-046 | sponsoring et visibilité commerciale gouvernés | Economy | 010 | partenaires commerciaux | monétiser des emplacements sans modifier les résultats organiques |
| YD-CAP-047 | accès organisationnel et intégrations externes gouvernées | Economy/Partners | 010 | organisations clientes | utiliser certaines capacités YDIASE dans leurs systèmes |
| YD-CAP-048 | produits analytiques et produits de données autorisés | Economy/Data | 010 | organisations, institutions | fournir des produits dérivés compatibles avec droits et privacy |
| YD-CAP-049 | notifications et communications liées aux actions produit | transversal | 004,006 | tous | suivre les changements qui concernent l'utilisateur |
| YD-CAP-050 | gestion des interactions et contenus à risque | Content | 009 | communauté, équipes autorisées | appliquer les règles de publication et d'interaction |
| YD-CAP-051 | administration fonctionnelle des référentiels, règles pays et paramètres produit | transversal | 007,008 | équipes autorisées | administrer les variations fonctionnelles sans modifier le code métier pour chaque cas |
| YD-CAP-056 | comparaison structurée d'options éducatives et professionnelles | Guidance | 001,002,004 | individus | comparer plusieurs options sur des critères explicites |
| YD-CAP-057 | suivi longitudinal des objectifs, décisions et progression de la personne | Guidance/Identity | 004,005 | individus | mesurer l'évolution entre intention, action et résultat |
| YD-CAP-058 | compétences transférables et équivalences fonctionnelles | Skills/Careers | 005,007 | individus | identifier ce qui reste réutilisable lors d'une transition |
| YD-CAP-059 | résultats et devenir après formation ou transition lorsque des données légitimes existent | Education/Labor | 002,003,010 | individus, établissements, institutions | mieux estimer les issues observées sans promettre un résultat individuel |
| YD-CAP-060 | accessibilité et modes d'usage adaptés aux contraintes de connectivité et de terminal | transversal | 008 | individus, terrain | rendre les fonctions essentielles utilisables dans des contextes contraints |
| YD-CAP-061 | feedback, contestation et correction des informations ou recommandations | transversal | 008,009 | individus, partenaires | signaler une erreur, demander correction et enrichir la qualité |
| YD-CAP-062 | portabilité, export et récupération des informations personnelles autorisées | Identity | 004,007 | individus | conserver la maîtrise des informations personnelles selon les droits applicables |

## 3. Éléments retirés du catalogue comme capacités autonomes

Les anciens éléments suivants restent obligatoires mais deviennent des exigences ou capacités de support plutôt que des capacités produit autonomes :

- ancien `YD-CAP-039` contrôle des sorties IA → exigence AI/Safety liée à `YD-CAP-038`
- ancien `YD-CAP-044` qualité/provenance/corroboration/temporalité → exigences Data transversales liées à toutes les capacités alimentées par des données
- ancien `YD-CAP-053` consentements/finalités/droits de données → exigences Privacy/Conformité et capacités internes du domaine Identity/Consent
- ancien `YD-CAP-054` audit/traçabilité → exigence de gouvernance, sécurité et exploitation

Leurs anciens IDs ne sont pas réutilisés pour un autre sens. Le registre documentaire doit conserver cette évolution.

## 4. Résultat de la revue

- 51 capacités existantes sont conservées ou reformulées comme capacités métier/produit.
- 4 formulations techniques ou de gouvernance ne restent plus des capacités produit autonomes.
- 7 capacités manquantes sont ajoutées sous IDs 056 à 062.
- le catalogue contient désormais 58 capacités actives/revues.
- aucun nombre cible n'est figé.

## 5. Gate suivant

Les domaines 02 à 11 doivent maintenant confirmer, fusionner, scinder ou rejeter ces capacités. Une capacité ne devient `ACTIVE` que lorsque son domaine principal confirme sa responsabilité, ses règles métier, ses données principales et ses critères de valeur.