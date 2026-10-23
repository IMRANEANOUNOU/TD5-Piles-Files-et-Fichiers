import csv

FICHIER = "utilisateurs.csv"
JEUX = ["score_1", "score_2"]


def importer(nom_fichier):
    with open(nom_fichier, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=","))


utilisateurs = importer(FICHIER)


def moins_de_300_jeu1(table):
    return [u for u in table if int(u["score_1"]) < 300]


def filles(table):
    return [u for u in table if u["genre"] == "F"]


def domaine_example(table):
    return [u for u in table if u["email"].endswith("@example.fr")]


def projection_scores(table, jeu):
    return [{"email": u["email"], "score": int(u[jeu])} for u in table]


def meilleurs_scores(table):
    return {
        jeu: sorted(projection_scores(table, jeu), key=lambda d: d["score"])
        for jeu in JEUX
    }


def score_moyen(table, jeu):
    scores = [d["score"] for d in projection_scores(table, jeu)]
    return sum(scores) / len(scores)


def projection_mails(table):
    return [{"email": u["email"]} for u in table]


def mails_pires_joueurs(table, n=10):
    resultat = []
    for jeu in JEUX:
        pires = sorted(projection_scores(table, jeu), key=lambda d: d["score"])[:n]
        resultat += [{"email": d["email"]} for d in pires]
    return resultat


def sans_doublons(table):
    vus = set()
    resultat = []
    for d in table:
        if d["email"] not in vus:
            vus.add(d["email"])
            resultat.append(d)
    return resultat

print(len(utilisateurs))
print(moins_de_300_jeu1(utilisateurs))
print(filles(utilisateurs))
print(domaine_example(utilisateurs))
classement = meilleurs_scores(utilisateurs)
for jeu in JEUX:
 print(jeu, classement[jeu]) 
 print(jeu, "score moyen :", score_moyen(utilisateurs, jeu))
print(projection_mails(utilisateurs))
pires = mails_pires_joueurs(utilisateurs)
print(pires)
print(sans_doublons(pires))
