---
document_id: "YD-DOC-POL-CFG-001-COUNTRY-CONFIGURATION"
title: "YD-MS-CFG-001 — Country Configuration Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de country configuration pour YD-MS-CFG-001."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "policy"
---

# YD-MS-CFG-001 — Country Configuration Policy

> **Rôle du document**
> Établit les règles normatives de country configuration pour YD-MS-CFG-001.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / COUNTRY-EVIDENCE-PENDING`
Nature : `AUTH`
Criticité : `C1`

## 1. Mission

CFG-001 est l'autorité interne sur la configuration opérationnelle multi-pays de YDIASE. Il permet aux domaines de savoir **dans quel contexte gouverné ils opèrent** sans dupliquer une vérité pays dans chaque microservice.

CFG représente une configuration YDIASE validée ; il ne devient jamais l'auteur d'un texte officiel, d'une loi, d'un diplôme, d'une taxe ou d'une règle métier appartenant à un autre domaine.

## 2. Agrégats

CFG possède :
- `CountryConfiguration` ;
- `Territory` ;
- `LanguageConfiguration` ;
- `CurrencyConfiguration` ;
- `CountryFrameworkBinding` ;
- `LocalPolicyParameter`.

Chaque objet est versionné, daté, sourcé et possède un état de publication.

## 3. CountryConfiguration

Une version publiée conserve au minimum :
- country_code stable ;
- config_version ;
- effective_from/effective_until ;
- status ;
- territory hierarchy/version ;
- langues configurées ;
- monnaie(s) et rôle opérationnel ;
- framework bindings ;
- paramètres locaux explicitement gouvernés ;
- provenance/evidence refs ;
- approbation/change refs.

États minimaux : `DRAFT`, `UNDER-REVIEW`, `SCHEDULED`, `ACTIVE`, `SUPERSEDED`, `SUSPENDED`, `RETIRED`.

Une version historique n'est jamais modifiée pour refléter silencieusement une règle nouvelle.

## 4. Frontière d'autorité

CFG peut dire **quel cadre/version s'applique**. Le domaine propriétaire interprète ensuite ce cadre pour ses invariants métier.

Exemples :
- CFG lie un pays à un Qualification Framework ; EDU-004 possède Qualifications, niveaux et équivalences YDIASE.
- CFG fournit territoire/langue/contexte ; LAB possède ses signaux et indicateurs.
- CFG fournit les bindings pays nécessaires ; CNS possède PrivacyDecision et ses règles opérationnelles Privacy.
- CFG fournit monnaie/contexte ; Billing possède factures et transactions.
- CFG référence DAT-005 ; DAT-005 possède taxonomies/référentiels transversaux.

Aucun domaine ne crée une `CountryConfiguration` parallèle.

## 5. Framework Binding

Un `CountryFrameworkBinding` lie :
- country/territory scope ;
- framework_type ;
- framework_ref/version ;
- authority/source attribution ;
- effective dates ;
- validation/provenance refs ;
- status.

Le binding ne copie pas nécessairement le contenu intégral du framework.

Une règle ne peut être appliquée hors de son scope territorial/temporel sans binding explicite.

## 6. LocalPolicyParameter

Les paramètres locaux sont réservés aux valeurs réellement transversales ou nécessaires à plusieurs domaines.

Chaque paramètre conserve : key stable, type/unité, scope, value/version, effective dates, source/provenance, owner fonctionnel, validation state.

Interdiction de transformer CFG en "table de settings universelle". Une règle propre à EDU, LAB, Billing, Privacy ou un autre domaine reste dans son domaine, même si elle varie par pays.

## 7. Héritage territorial

L'héritage country → région/province/territoire n'est autorisé que pour des paramètres déclarés héritables. Une valeur locale explicite peut surcharger uniquement si la policy du paramètre l'autorise.

Aucune règle n'est héritée par défaut parce que deux territoires sont voisins ou membres d'un même bloc régional.

UEMOA, CEDEAO, OHADA, ZLECAf ou tout autre cadre supranational est représenté comme référence/binding explicite lorsque pertinent ; l'appartenance ne signifie pas que toutes ses règles s'appliquent à tous les domaines.

## 8. Langues

CFG décrit langues supportées/actives et leurs scopes opérationnels. Il ne traduit pas les contenus métier.

Absence de traduction n'autorise pas l'invention d'une valeur. Les objets métier gardent leurs propres règles de localisation.

## 9. Monnaies

CFG décrit monnaie(s), codes et contexte opérationnel. Il ne possède ni taux de change, ni prix, ni fiscalité, ni comptabilité.

Toute conversion monétaire exige une source/timestamp/policy dédiée ; aucune conversion implicite n'est créée dans CFG.

## 10. UNKNOWN et absence de configuration

`UNKNOWN`, `NOT-CONFIGURED`, `NOT-APPLICABLE` et `KNOWN` sont distingués.

Une absence de configuration ne vaut jamais valeur par défaut africaine.

Si une écriture métier nécessite une config non disponible/expirée/non validée, elle est gelée ou refusée selon contrat. Les lectures historiques peuvent utiliser la version alors applicable.

## 11. Changement et rollout

Toute modification à impact élevé suit : draft → review → approval → scheduled/effective → propagation.

Le changement publie `country-config.changed` avec country_code, config_version, changed_sections et effective_at.

Les consommateurs conservent leur watermark de version et n'appliquent jamais une version plus ancienne sur une version plus récente.

Les breaking changes nécessitent migration/compatibilité explicite ; un changement CFG ne réécrit pas silencieusement les objets métier historiques.

## 12. Provenance

Toute configuration substantielle doit référencer sa provenance : source officielle/référence, DAT provenance/quality si utilisée, date de vérification et validation YDIASE.

Une source externe reste attribuée à sa source ; CFG n'en devient pas l'auteur.

## 13. Bootstrap Burkina Faso

Le pilote Burkina est une **première instance de CountryConfiguration**, jamais le template implicite de l'Afrique.

Avant activation Burkina, les sections réellement nécessaires au pilote doivent être complètes, validées et sourcées. Toute section non nécessaire peut rester NOT-CONFIGURED si ses consommateurs ne la requièrent pas.

Aucune valeur Burkina n'est copiée automatiquement vers un nouveau pays.

## 14. Gates

`DEFINED` : autorité CFG, versionnement temporel, framework binding, local parameters, héritage explicite, frontières EDU/CNS/DAT/LAB/Billing, langues, monnaies, UNKNOWN, rollout, provenance, principe bootstrap Burkina.

`TBD-COUNTRY-EVIDENCE` : contenu réel Burkina et futurs pays, sources officielles, validations métier/juridiques correspondantes.

`TBD-PREPROD` : IAM/approbations physiques, contrats/schema, cache/freshness, BIA/RPO/RTO/SLO, backup/restore et tests de propagation.

Statut final : `COUNTRY-CONFIG-SEMANTICS-CLOSED / BURKINA-EVIDENCE-AND-PREPROD-PENDING`.
