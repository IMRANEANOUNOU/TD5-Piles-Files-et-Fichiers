def PileVide():
    return []

def EstVide(pile):
    return len(pile) == 0

def Empiler(pile, x):
    pile.append(x)

def Depiler(pile):
    return pile.pop()

def SommetPile(pile):
    return pile[-1]

def EstChiffre(c):
    if '0' <= c <= '9':
        return 1
    return 0



def Convertir(c):
    return ord(c) - ord('0')


def Evaluer(expression):
    pile = PileVide()
    for c in expression:
        if c == ' ':                     
            continue
        if EstChiffre(c):
            Empiler(pile, Convertir(c))
        else:                             
            b = Depiler(pile)            
            a = Depiler(pile)            
            if c == '+':
                r = a + b
            elif c == '-':
                r = a - b
            elif c == '*':
                r = a * b
            elif c == '/':
                r = a / b
            else:
                return f"Opérateur inconnu : {c}"
            Empiler(pile, r)
    return Depiler(pile)



def EvaluerTexte(Fsrc, Fdest):
    with open(Fsrc, 'r') as src, open(Fdest, 'w') as dest:
        for ligne in src:
            ligne = ligne.strip()
            if ligne == "":
                continue
            try:
                resultat = Evaluer(ligne)
            except Exception:
                resultat = "Erreur"
            dest.write(str(resultat) + "\n")

EvaluerTexte("src.txt","dest.txt")

print(Evaluer("96*7-"))
