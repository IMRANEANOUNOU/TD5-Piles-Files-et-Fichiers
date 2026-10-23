from math import factorial


def Empiler_Fat(n,P1) :
    P1 = [ factorial(i) for i in range(n+1)]
    return P1

def Empiler_Puiss(n,x,P2):
    P2 = [x**i for i in range(n+1)]
    return P2
    
def Empiler_Frac(P1,P2):
    return [i/j for i,j in zip(P1,P2)]

def Somme(n ,x):
    P1 = Empiler_Fat(n,[])
    P2 = Empiler_Puiss(n,x,[])
    P3 = Empiler_Frac(P1,P2)
    somme = 0
    for i in P3 :
        somme+=i
    return somme
    
P1 = Empiler_Fat(5,[])
P2=Empiler_Puiss(5,2,[])
P3 = Empiler_Frac(P1,P2)

print(list(P1))
print(list(P2))
print(list(P3))
print(Somme(5,2))
