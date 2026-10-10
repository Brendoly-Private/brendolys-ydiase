---
document_id: "YD-DOC-FND-POL-002"
title: "Politique de gestion des contradictions"
document_type: "documentation-policy"
document_role: "Gouverne la détection, l’arbitrage et la conservation des contradictions documentaires et de données."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "foundation"
  - "documentation-governance"
---

# Politique de gestion des contradictions

Statut : `ACTIVE`

## Détection

Une contradiction existe lorsque deux assertions applicables au même périmètre ne peuvent être vraies simultanément ou imposent des comportements incompatibles.

## Interdictions

Il est interdit de supprimer silencieusement une assertion, choisir la plus récente sans vérifier son autorité, fusionner deux sens incompatibles ou utiliser l'IA pour arbitrer automatiquement.

## Traitement

1. enregistrer les assertions séparément
2. identifier leurs sources, versions, owners et niveaux d'autorité
3. déterminer le périmètre exact du conflit
4. suspendre la propagation de la valeur contestée si le risque l'exige
5. créer une décision d'arbitrage
6. identifier les documents et contrats affectés
7. appliquer la décision et conserver l'historique

## Données

Pour les données contradictoires, conserver provenance, date d'observation, période de validité, niveau de confiance et statut de corroboration. Une valeur contestée ne devient pas référence uniquement parce qu'elle apparaît dans plusieurs copies dérivées.

## Architecture

Une contradiction métier découverte après D3 peut rouvrir une frontière. La fermeture documentaire D3 n'interdit pas une correction justifiée.