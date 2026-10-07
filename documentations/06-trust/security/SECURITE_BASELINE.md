---
document_id: "YD-DOC-TRU-SEC-SECURITE-BASELINE"
title: "Sécurité et conformité — Baseline BRENDOLYS YDIASE"
document_type: "governance-baseline"
document_role: "Établit une règle ou baseline normative de gouvernance, confidentialité ou sécurité."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "trust"
---

# Sécurité et conformité — Baseline BRENDOLYS YDIASE

> **Rôle du document**
> Établit une règle ou baseline normative de gouvernance, confidentialité ou sécurité.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `D3-security-baseline`

## 1. Objet

Ce document porte les politiques transversales de sécurité, privacy et conformité de YDIASE. `MICROSERVICE_AUTONOMY_STANDARD.md` impose leur application par frontière. Le présent dossier définit les règles communes; les `AUTONOMY_PROFILE.md` déclareront leur application concrète.

## 2. Classification des informations

Classification minimale :

1. `PUBLIC` — publication autorisée
2. `INTERNAL` — usage interne YDIASE/BRENDOLYS autorisé selon fonction
3. `CONFIDENTIAL` — accès explicitement autorisé et tracé selon risque
4. `PERSONAL` — donnée personnelle identifiante ou liée à une personne
5. `PERSONAL_SENSITIVE` — donnée personnelle dont l’exposition ou l’usage abusif produit un risque élevé
6. `SECRET` — secrets techniques, clés, credentials et éléments de sécurité

Une donnée hérite du niveau le plus protecteur requis par son contenu et sa finalité. Les datasets, événements, logs, backups et projections conservent leur classification.

## 3. Privacy et finalités

Tout traitement de données personnelles possède une entrée dans le registre des finalités avec : finalité, catégories de personnes, catégories de données, source, base juridique applicable, consommateurs autorisés, territoires, durée de rétention, règle d’effacement, partage, sous-traitants le cas échéant, owner et preuve de revue.

Aucun microservice ne collecte une donnée personnelle « au cas où ». Les contrats diffusent le minimum nécessaire. Analytics, AI, Search et recommandations n’obtiennent pas automatiquement l’intégralité des profils.

## 4. BRENDOLYS Identity

BRENDOLYS Identity reste l’IAM utilisateur de référence. YDIASE ne stocke aucun mot de passe utilisateur.

Realms :

- `brendolys-internal` — employés et équipe interne
- `brendolys-networks` — ambassadeurs et acteurs externes des réseaux
- `brendolys-customers` — utilisateurs et organisations clientes

Issuer : `https://sso.godinfradsby.xyz/realms/{realm}/protocol/openid-connect`.

Chaque frontière déclare les realms acceptés, audience, scopes, rôles, claims minimaux et politiques d’autorisation métier. L’authentification ne remplace pas l’autorisation.

## 5. Identités machine

Chaque workload autonome reçoit une identité machine distincte. Les secrets permanents partagés entre plusieurs services sont interdits. Les permissions machine suivent least privilege et les relations de `DEPENDENCY_MAP.md`.

Le mécanisme technique final de workload identity est fixé par ADR.

## 6. Autorisation

Les décisions d’accès combinent selon besoin : identité, rôle, scope, organisation/tenant, ownership de l’objet, finalité, état métier et contexte de sécurité.

Les contrôles objet empêchent l’accès horizontal. Les contrôles de privilège empêchent l’accès vertical. Les fonctions administratives ne contournent pas les owners métier.

## 7. Secrets et clés

Les secrets sont stockés hors code et hors configuration versionnée. Chaque secret possède owner, consommateurs, date de création, rotation, révocation et audit. Les secrets globaux YDIASE sont interdits lorsqu’une identité ou un secret par workload suffit.

Les clés de chiffrement suivent séparation des responsabilités et politique de rotation proportionnée au risque.

## 8. Chiffrement

Les données non publiques utilisent un transport chiffré. Les données au repos sont chiffrées selon classification, stockage et threat model. Les backups héritent au minimum des exigences de la donnée source.

## 9. Réseau

Le réseau suit `deny-by-default`. Un service n’obtient que les flux entrants et sortants nécessaires à ses contrats. Les bases et stockages internes ne sont jamais rendus publics pour simplifier une intégration.

Les flux interservices, IAM, broker, observabilité, stockage, DNS et services externes sont inventoriés.

## 10. API et protection contre abus

Les APIs déclarent exposition, authentification, autorisation, validation, quotas, rate limiting, limites de payload, timeout et journalisation. Les interfaces publiques reçoivent une protection contre automatisation abusive, enumeration et attaques de disponibilité proportionnée au risque.

## 11. Sécurité des événements

Un événement ne contient que les données nécessaires aux consommateurs légitimes. Les topics/streams appliquent ACL, chiffrement, rétention et audit. Les données sensibles ne sont pas propagées uniquement pour éviter un appel API.

## 12. Logs, traces et télémétrie

Les logs n’enregistrent jamais tokens, mots de passe, secrets ou payloads sensibles complets sans justification approuvée. Les identifiants techniques pseudonymisés sont préférés lorsqu’ils suffisent.

Les accès sensibles, changements de permission, actions administratives, opérations privacy et événements de sécurité produisent une preuve d’audit.

## 13. Audit transverse

`YD-PLT-AUD-001` reçoit les faits d’audit transverses. Il ne devient pas source autoritative du fait métier. Les événements d’audit sont protégés contre modification non autorisée et disposent d’une rétention adaptée à leur finalité.

## 14. Secure SDLC et supply chain

Chaque repository autonome applique : revue de code, contrôle des dépendances, SBOM, SAST, SCA, scan d’image/artefact lorsque pertinent, gestion des vulnérabilités et traçabilité build→commit→release.

Les dépendances non maintenues ou vulnérables ne passent pas en production sans dérogation documentée, compensations et date d’expiration.

## 15. Threat modeling

Chaque frontière possède un threat model proportionné à sa criticité. Le minimum couvre : usurpation, élévation de privilèges, accès inter-tenant, fuite, altération, suppression, injection, abus d’API, compromission de dépendance, supply chain et indisponibilité volontaire.

Les services Profile, Consent & Privacy, Application, Billing, Audit, Admin plane, Data Acquisition et AI reçoivent une revue renforcée avant production.

## 16. Sécurité AI

Les composants AI séparent données sources, contexte récupéré, instructions, sorties et preuves. Les contrôles couvrent prompt injection, data exfiltration, outils non autorisés, hallucination décisionnelle, contamination du contexte et divulgation inter-utilisateur.

`AI Verification` reste indépendant des mécanismes qu’il vérifie. Une sortie IA n’est jamais source de vérité par sa seule génération.

## 17. Sécurité multi-pays

L’arrivée dans un pays exige une revue du Country Framework : catégories de données, exigences locales, localisation/transfert, consentement ou autre base applicable, droits des personnes, conservation, mineurs et obligations sectorielles.

Aucune règle juridique d’un pays n’est généralisée automatiquement à tout le continent.

## 18. Mineurs

YDIASE pouvant servir des élèves, les flux concernant des mineurs sont identifiés explicitement. Les données, consentements/autorisations applicables, exposition sociale, messagerie, profilage, publicité/sponsoring et recommandations reçoivent des règles renforcées avant activation.

## 19. Incident de sécurité

Tout service définit détection, qualification, confinement, révocation, préservation des preuves, restauration et escalade. Les responsabilités de notification juridique seront définies dans les Country Frameworks applicables.

## 20. Effacement, rétention et sauvegardes

Une demande ou règle d’effacement doit traiter source autoritative, projections, index, caches, datasets dérivés et backups selon politique documentée. Les backups ne deviennent pas une exception permanente à la rétention. Leur restauration doit inclure une procédure de réapplication des suppressions nécessaires.

## 21. Gates production

Aucun service traitant des données personnelles ou confidentielles ne passe production sans : classification, finalité, owner, accès, rétention, suppression, threat model, flux réseau, IAM, audit, secrets, chiffrement, tests d’autorisation et procédure d’incident documentés.

## 22. Articulation documentaire

- `03-systems/architecture/standards/MICROSERVICE_AUTONOMY_STANDARD.md` — exigences d’autonomie par frontière
- `03-systems/architecture/target/DEPENDENCY_MAP.md` — flux autorisés candidats
- `04-contracts/events/EVENT_MAP.md` — événements et données propagées
- `14-securite-conformite/` — politiques transversales de sécurité/privacy
- `15-exploitation-resilience/` — continuité, SLO, backup, restore et DR
- futurs `AUTONOMY_PROFILE.md` — application spécifique à chaque frontière
- futurs contrats — surface exacte d’échange
