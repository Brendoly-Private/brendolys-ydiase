# YD-SVC-NTF-001 — Notification Service

`domain: plateforme` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Notification`, `DeliveryAttempt`, `NotificationPreferenceProjection`, `NotificationTemplate`.

## Source autoritative
YD-SVC-NTF-001 pour notification/livraison; préférences maîtres restent PRF/CNS selon type.

## Données consommées
Identity/contact route, user preferences/consent, événements des domaines producteurs.

## Incohérences
`NotificationPreferenceProjection` doit rester une projection et ne jamais concurrencer PRF/CNS.
