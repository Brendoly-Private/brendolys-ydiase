# YDIASE — Target Flow Map

Statut : TARGET-FLOW-BASELINE / NORMATIVE

## Interaction
Client → Edge/API → IDN/Entitlement/Privacy → service owner → réponse. Les lectures massives peuvent utiliser caches/projections gouvernés ; une mutation va au service autoritatif.

## Orientation
PRF/SKL/ASM + EDU/CAR + LAB + ENT + OPP → snapshot ORI → REC ranking explicable → comparaison/décision ORI → progression/feedback autorisé.

## Entrepreneuriat
PRF/SKL/ASM → contexte autorisé ; LAB → signaux économiques ; ENT-002 → hypothèses/opportunités sourcées ; ENT-001/006 → projet/progression ; ENT-003/004 → accompagnement/financement ; ENT-005 → équipe fondatrice ; ORI/REC → comparaison et scénarios ; EMP/OPP → transition entrepreneur-employeur.

## Data
Sources → DAT-001 → DAT-002 → DAT-003 → DAT-004 → owner métier lorsqu'une donnée devient vérité métier. En parallèle, événements/projections autorisés → batch/stream → lakehouse → Analytics/Knowledge/Search/ML.

## IA
Service demandeur → AI Gateway → autorisation → Retrieval/Grounding → orchestration/modèle/outils → Verification → service demandeur. L'IA n'écrit jamais directement dans un datastore métier externe.

## Événements
Commit owner → outbox/équivalent logique → event backbone → consommateurs idempotents → projection/effet gouverné → audit/observabilité. Ordre local par agrégat lorsque requis ; aucun ordre global supposé.

## Hyperscale
Les chemins synchrones restent courts. Les fan-outs lourds utilisent projections, agrégations ou asynchronisme. Chaque hop consomme un budget de latence/disponibilité. Files bornées, backpressure et dégradation sont obligatoires selon risque.
