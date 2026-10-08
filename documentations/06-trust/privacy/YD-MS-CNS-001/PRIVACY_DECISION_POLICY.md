---
document_id: "YD-DOC-TRU-CNS-001-PRIVACY-DECISION-POLICY"
title: "YD-MS-CNS-001 — Privacy Decision Policy"
document_type: "trust-policy"
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
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-CNS-001 — Privacy Decision Policy

> **Rôle du document**
> Établit une règle ou baseline normative de gouvernance, confidentialité ou sécurité.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / LEGAL-COUNTRY-VALIDATION-PENDING`
Nature : `AUTH`
Criticité : `C1`

## 1. Autorité

CNS-001 est l'autorité YDIASE sur :
- références de finalité (`PurposeRef`) et leur version gouvernée ;
- `PurposeGrant` lorsqu'un grant/consentement est applicable ;
- restrictions Privacy ;
- demandes Privacy et leur workflow ;
- règles/instructions de rétention applicables ;
- `PrivacyDecision` rendue aux processeurs.

CNS ne possède pas les données métier traitées par PRF, SKL, ASM, ORI, REC ou autres domaines.

## 2. Finalité avant traitement

Tout traitement personnel gouverné porte un `purpose_ref` explicite. Une finalité décrit au minimum : usage, catégories de données nécessaires, catégories de processeurs/consommateurs, contexte/pays applicable, conditions d'autorisation, règles de rétention et version/effective dates.

Un service consommateur ne crée pas sa propre interprétation concurrente d'une finalité CNS.

## 3. Consentement et autres autorisations

Un consentement n'est pas supposé être la base applicable à tout traitement. CNS représente la décision autorisée selon la règle juridique/policy applicable et son contexte.

Lorsqu'un consentement explicite est requis, il doit être spécifique, traçable, versionné et révocable. L'absence de consentement requis n'est jamais interprétée comme accord.

La validation juridique réelle par pays reste un gate ; cette baseline n'invente aucune base légale nationale.

## 4. PurposeGrant

Un PurposeGrant lie au minimum : subject_ref, purpose_ref/version, scope, state, source/mode d'autorisation, effective_at, expiry si applicable et version.

États minimaux : `PENDING`, `GRANTED`, `DENIED`, `REVOKED`, `EXPIRED`, `RESTRICTED`, `SUPERSEDED`.

Une version plus ancienne ne peut jamais remplacer un état plus récent.

## 5. PrivacyDecision

Pour une demande de traitement, CNS retourne une décision minimale :
- `ALLOW` ;
- `DENY` ;
- `ALLOW-WITH-RESTRICTIONS` ;
- `NOT-DETERMINABLE`.

La décision conserve subject/context ref, purpose/version, processor/capability, restrictions, decision_version, evaluated_at, valid_until/freshness bound et reason codes non sensibles.

`NOT-DETERMINABLE` n'est jamais équivalent à `ALLOW`.

## 6. Fail-closed et modes dégradés

Lorsqu'une PrivacyDecision est obligatoire et n'est pas vérifiable, le traitement concerné est refusé, suspendu ou mis en attente. Aucun cache expiré ne devient autorisation par défaut.

Un mode non personnalisé ou anonyme peut continuer uniquement s'il possède sa propre finalité/autorisation et ne réutilise pas silencieusement les données du traitement refusé.

Les traitements strictement nécessaires dont le comportement dégradé diffère doivent être explicitement classifiés avant implémentation ; aucun service ne s'auto-déclare indispensable.

## 7. Restrictions

Une restriction peut réduire catégories de données, capacités, destinataires, canaux, durée ou autres scopes gouvernés. Elle prévaut sur un grant plus large lorsqu'elle est applicable et plus récente selon l'ordre autoritatif.

Les processeurs appliquent la décision CNS ; ils ne reconstruisent pas localement une politique Privacy concurrente.

## 8. Révocation

Une révocation prend effet à `effective_at` et crée une nouvelle version autoritative. Elle déclenche `consent.changed` et/ou `privacy.restriction-changed` selon le cas.

Les consommateurs doivent invalider les caches/projections concernés dans une borne de propagation à définir par SLO. Une révocation ne supprime pas la preuve historique nécessaire ; elle interdit les traitements futurs couverts et déclenche les actions correctives prévues.

## 9. Rétention et effacement

CNS gouverne l'instruction Privacy ; chaque domaine reste responsable de l'exécution sur les données qu'il possède.

Une instruction de rétention/effacement doit être versionnée, scoped, traçable et propagée aux détenteurs concernés. Un domaine ne peut ni conserver indéfiniment "au cas où", ni déclarer l'effacement CNS accompli avant confirmation des détenteurs requis.

Les sauvegardes suivent une politique de suppression logique/expiration compatible avec les obligations applicables ; une restauration ne doit pas réactiver durablement une donnée ou autorisation qui avait été révoquée/effacée.

## 10. Privacy Requests

Une PrivacyRequest conserve request_ref, subject_ref, request_type, scope, received_at, due_at si applicable, state, vérifications nécessaires et résultats/références d'exécution.

États minimaux : `RECEIVED`, `IDENTITY-VERIFICATION-PENDING`, `IN-PROGRESS`, `WAITING-ON-DOMAIN`, `COMPLETED`, `PARTIALLY-COMPLETED`, `REJECTED-WITH-REASON`.

Les délais légaux réels sont configurés/validés par juridiction ; ils ne sont pas inventés ici.

## 11. Mineurs et représentation

Le modèle doit pouvoir représenter sujet, représentant/guardian autorisé, portée, durée et preuve de représentation sans supposer un âge universel de consentement.

Les seuils d'âge et règles nationales restent liés au Country Framework/validation juridique.

## 12. Minimisation des contrats

Les événements CNS transportent des références et états minimaux, jamais un dossier Privacy complet.

Les consommateurs ne reçoivent que la décision/restriction nécessaire à leur finalité. Les données d'audit et de preuve restent fortement contrôlées.

## 13. Correction

Une correction n'écrase jamais silencieusement l'historique. Elle crée version/correction reliée, préserve la chronologie probante et déclenche réconciliation si des décisions consommateurs ont été affectées.

## 14. Gates

`DEFINED` : ownership, purpose-first, PurposeGrant, PrivacyDecision, fail-closed, restrictions, révocation, rétention/effacement distribué, PrivacyRequest, correction/versionnement, principe mineurs/représentation.

`TBD-LEGAL/COUNTRY` : bases applicables, âges/seuils, délais, durées de rétention et exigences territoriales.

`TBD-PREPROD` : IAM/scopes, SLO propagation révocation, cache TTL, BIA/RPO/RTO, backup/restore, tests IDOR, audit, contrats physiques.

Statut final : `PRIVACY-SEMANTICS-CLOSED / LEGAL-COUNTRY-AND-PREPROD-VALIDATION-PENDING`.
