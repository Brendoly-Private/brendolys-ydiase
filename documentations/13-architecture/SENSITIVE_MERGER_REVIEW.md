# Sensitive Merger Review — BRENDOLYS YDIASE

Statut : `D3-reviewed`

## Objet

Revue contradictoire des fusions retenues dans `MICROSERVICE_BOUNDARY_REVIEW.md`. Une fusion n’est conservée que si elle respecte les bloqueurs du `MICROSERVICE_AUTONOMY_STANDARD.md` et ne détruit ni ownership, ni sécurité, ni capacité d’extraction future.

## Verdict

| Fusion | Verdict | Risque principal | Condition |
|---|---|---|---|
| PRF-001 + PRF-002 | VALIDÉE SOUS CONTRÔLE | croissance du profil éducation/expérience et sensibilité accrue | modules, agrégats, tables/schémas logiques et permissions internes distincts; extraction si charge, équipe, rétention ou sécurité divergent |
| CAR-002 + CAR-003 | VALIDÉE | Career Path et Transition peuvent devenir algorithmiquement différents | contrats internes distincts et aucun accès direct aux données CAR-001; extraction si scaling/modèles/SLO divergent |
| ORI-001 + ORI-002 | VALIDÉE FORTE | comparaison pourrait devenir un produit transversal | Decision Support reste module sans autorité indépendante; extraction si utilisé massivement hors dossier Orientation |
| REC-001 + RSH-001 logical | VALIDÉE TEMPORAIRE | Academic Research Topic peut devenir une capacité produit autonome | namespace/module propre, métriques propres, aucun agrégat autoritatif indépendant; revue avant activation multi-pays/marketplace académique |
| EMP-003 Workspace en BFF | VALIDÉE | risque de déplacer de la logique métier dans le BFF | zéro agrégat autoritatif, zéro écriture directe en DB métier, orchestration seulement via contrats |
| INS-001 Workspace en BFF | VALIDÉE SOUS CONTRÔLE | les soumissions institutionnelles ont un workflow durable | le BFF ne devient pas owner EDU; si le workflow de soumission acquiert états/invariants propres, créer une frontière workflow dédiée plutôt que grossir le BFF |
| ADM-001 en Admin plane | VALIDÉE | risque de super-service privilégié | aucune DB métier, aucune écriture directe; commandes autorisées, auditées et routées vers owners |

## Points surveillés

### PRF-001 + PRF-002
C’est la fusion la plus sensible côté données personnelles. Elle reste acceptable parce que les deux responsabilités décrivent le même sujet et participent au même dossier utilisateur. Elle ne doit pas produire un « profil géant ». Les sous-modèles Education/Experience gardent leurs invariants, rétention et permissions documentés.

### CAR-002 + CAR-003
La fusion est cohérente tant que Transition reste une vue/calcul spécialisé des trajectoires. Si les transitions utilisent demain des modèles, datasets ou cycles de calcul différents, elles devront être extraites.

### ORI-001 + ORI-002
La comparaison sert directement la décision d’orientation. Une séparation immédiate ajouterait du chatter et une frontière sans ownership distinct. Le module doit toutefois rester extractible.

### RSH-001 dans Recommendation
Cette fusion est la moins définitive. Elle évite aujourd’hui un microservice dont la responsabilité est essentiellement une variante de recommandation. Une évolution vers gestion de sujets, validation académique, encadrement, soutenance ou marketplace de recherche obligera une nouvelle revue DDD.

### Workspaces et Administration
EMP-003, INS-001 et ADM-001 ne sont pas des owners métier. Cette règle est stricte. Si l’un commence à posséder des états métier durables, la frontière doit être réévaluée plutôt que de cacher le domaine dans une façade.

## Conclusion

Aucune fusion actuelle ne doit être annulée immédiatement. Deux éléments exigent une surveillance renforcée : `PRF-002` et `RSH-001`. `INS-001` doit être réévalué dès que le workflow institutionnel durable est spécifié. La cible de 47 microservices métier reste cohérente à ce stade.
