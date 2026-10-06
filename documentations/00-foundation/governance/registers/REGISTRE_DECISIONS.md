# Registre des décisions — BRENDOLYS YDIASE

Statut : `ACTIVE`

Ce registre indexe les décisions structurantes déjà présentes dans le corpus. Une ligne ne remplace pas le document de décision détaillé.

| ID | Décision | Niveau | Alternatives principales | Conséquence | Source documentaire | Statut |
|---|---|---|---|---|---|---|
| YD-ADR-0001 | Le Knowledge Graph n'est pas la source opérationnelle unique des faits métier. | Architecture | Graphe comme source unique | Les domaines conservent leur autorité; le graphe reste DERIVED | `03-systems/microservices/YD-MS-KNW-001/` | ACTIVE |
| YD-ADR-GOV-001 | Les fondations produit et domaines métier ont autorité sur les choix techniques dérivés. | Gouvernance | Architecture comme référence supérieure | Une évolution métier peut rouvrir les décisions techniques impactées | `00-foundation/governance/standards/NIVEAUX_AUTORITE.md` | ACTIVE |
| YD-ADR-ARC-001 | Les 61 services logiques ne correspondent pas automatiquement à 61 microservices. | Architecture | 1 service logique = 1 microservice | Fusion DDD avant frontière physique | `03-systems/architecture/reviews/MICROSERVICE_BOUNDARY_REVIEW.md` | ACTIVE |
| YD-ADR-ARC-002 | La cible D3 comporte 47 microservices métier et 4 composants plateforme comme `STABLE-CANDIDATE`. | Architecture | conserver 61 frontières physiques | 51 frontières autonomes documentées; réexamen possible par impact métier | `03-systems/architecture/matrices/AUTONOMY_CLOSURE_MATRIX.md` | ACTIVE |
| YD-ADR-DATA-001 | Les données autoritatives et les données DERIVED suivent des politiques de reprise distinctes. | Data/Architecture | backup uniforme | DERIVED doit prouver reconstruction/replay | `03-systems/architecture/standards/MICROSERVICE_AUTONOMY_STANDARD.md` | ACTIVE |
| YD-ADR-DATA-002 | Les cinq frontières SRH, CNT-002, KNW, ANL-001 et AI-002 sont DERIVED au niveau D3. | Data/Architecture | les rendre propriétaires métier | Aucun fait métier irremplaçable ne doit y résider | `03-systems/architecture/registers/DERIVED_RECOVERY_REGISTER.md` | ACTIVE |
| YD-ADR-IAM-001 | BRENDOLYS Identity fournit l'identité externe avec trois realms séparés. | Sécurité | IAM propre à YDIASE | YDIASE ne devient pas source des mots de passe; autorisation métier reste locale | `03-systems/architecture/standards/MICROSERVICE_AUTONOMY_STANDARD.md` | ACTIVE |
| YD-ADR-IAM-002 | `brendolys-internal`, `brendolys-networks` et `brendolys-customers` ne sont pas interchangeables. | Sécurité | realm unique | chaque contrat déclare les realms admis | `05-decisions/architecture/closure/D3_BLOCKING_CLOSURE_DECISIONS.md` | ACTIVE |
| YD-ADR-DPR-001 | DPR ne peut pas décider seul qu'un dataset est distribuable. | Data/Conformité | décision DPR seule | CNS reste autorité privacy; droits source et entitlement restent requis | `05-decisions/architecture/closure/D3_BLOCKING_CLOSURE_DECISIONS.md` | ACTIVE |
| YD-ADR-CTR-001 | Le Contract Registry peut commencer en candidat après fermeture D3, mais ne devient pas stable par cette seule décision. | Architecture | attendre tous les paramètres préproduction | contrats fonctionnels peuvent être documentés avant choix physiques | `03-systems/architecture/matrices/AUTONOMY_CLOSURE_MATRIX.md` | ACTIVE |

## Décisions non encore converties en ADR détaillées

Les lignes `YD-ADR-*` ci-dessus doivent recevoir un document ADR dédié lorsqu'une alternative, un coût, une réversibilité ou un seuil d'activation nécessite une décision technique formelle. Le registre ne doit pas inventer le contenu manquant.
