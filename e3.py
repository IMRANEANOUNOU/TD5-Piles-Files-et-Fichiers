def creer_file():
    return [] 

def deposer_dans_queue(file, element, priorite):
    while len(file) <= priorite:
        file.append([])
    file[priorite].append(element)


def retirer_de_queue(file):
    for p in range(len(file) - 1, -1, -1):
        if len(file[p]) > 0:
            return file[p].pop(0)
    return None   

def file_vide(file):
    for sous_file in file:
        if len(sous_file) > 0:
            return False
    return True



def afficher(f):
    while not file_vide(f):
        print(retirer_de_queue(f), end=" ")

        
f = creer_file()
deposer_dans_queue(f, "A", 0)
deposer_dans_queue(f, "B", 2)
deposer_dans_queue(f, "C", 1)
deposer_dans_queue(f, "D", 2)
deposer_dans_queue(f, "E", 0)


afficher(f)
