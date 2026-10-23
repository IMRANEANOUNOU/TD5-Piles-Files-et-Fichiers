import random

INTERVALLE_MAX = 120 
DUREE_TRAITEMENT_MAX = 180  
HEURE_DEBUT = 8 * 3600 

def CreerListeClients():
    n = int(input("Nombre de clients : "))
    file = []
    arrivee = HEURE_DEBUT
    fin_precedent = HEURE_DEBUT

    for i in range(1, n + 1):
        if i > 1:
            arrivee += random.randint(0, INTERVALLE_MAX)

        duree = random.randint(0, DUREE_TRAITEMENT_MAX)
        debut = max(arrivee, fin_precedent)
        fin = debut + duree

        client = {
            "numero": i,
            "arrivee": arrivee,
            "duree": duree,
            "debut": debut,
            "fin": fin,
            "attente": debut - arrivee
        }
        file.append(client)
        fin_precedent = fin

    return file
    
def Formater(secondes):
    h = secondes // 3600
    m = (secondes % 3600) // 60
    s = secondes % 60
    return f"{h}h {m}min {s}s"


def Afficher(file):
    for c in file:
        print(f"Client {c['numero']:3d} | "
              f"arrivée : {Formater(c['arrivee'])} | "
              f"fin de traitement : {Formater(c['fin'])} | "
              f"attente : {Formater(c['attente'])}")


clients = CreerListeClients()
Afficher(clients)
