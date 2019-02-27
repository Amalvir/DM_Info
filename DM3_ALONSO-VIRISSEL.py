import matplotlib.pyplot as plt
import numpy as np
#import scipy.optimize   # Uniquement pour le "Pour aller plus loin"

## Exo 1
def fact(k):
    """ D'un entier k, retourne k! """
    p = 1
    for i in range(k):
        p = p*(k - i)
    return p

def expo_tronq(x, n):
    """Des paramêtres x, n renvoie fn(x)"""
    s = 0
    for i in range(n + 1):
        s += (x**i)/fact(i)
    return s

def trace(N):
    """Trace fn(x) pour tout x allant de 0 à 5 et pour tout n allant de 0 à N
    ainsi que la fonction exponentiel."""
    X = np.linspace(0, 5)
    plt.plot(X, np.exp(X), 'r--', label = "exp(x)")
    for i in range(N + 1):
        plt.plot(X, expo_tronq(X, i))
    plt.xlim(0, 5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Exercice 1 : Exponentielles tronquées')
    plt.show()
    
## Exo 2
def suivant(sn):
    """Du terme sn sous forme de liste, renvoie le terme sn+1 sous forme de liste
    aussi où (sn) est la suite de Conway."""
    sn1 = []  # Terme suivant
    count = 0  # Compteur
    actuel = sn[0]  # Chiffre qu'on compare actuellement
    for i in sn:
        if i == actuel:  # On parcourt les termes de sn, si pareil qu'actuel on
            count += 1   # rajoute 1 au compteur
        else:
            sn1.append(count)  # Sinon on append le compteur puis le chiffre actuel
            sn1.append(actuel)
            actuel = i  # et on change d'actuel et on reinitialise le compteur
            count = 1
    sn1.append(count)
    sn1.append(actuel)
    return sn1

def liste_terme(n):
    """Renvoie le terme d'indice n sous forme de liste."""
    sn = [1]
    for i in range(n):
        sn = suivant(sn)
    return sn

def convertir_liste(S):
    """D'une liste, renvoie l'entier correspondant."""
    string = ''
    for i in S:
        string += str(i)
    return int(string)

def conway(n):
    """Renvoie l'entier d'indice n de la suite de Conway."""
    return convertir_liste(liste_terme(n))

## Pour aller plus loin

def trace_longueur_exp(n):
    """On voit ici que le nombre de chiffres des termes de la suite de Conway augmente de façon exponentielle. Ceci trace donc le nombre de terme en fonction de n et l'interpolation exponentielle de la courbe. Renvoie aussi A et B tel que y = A*exp(B*x)"""
    X = [k for k in range(n)]
    Y = [len(liste_terme(i)) for i in range(n)]
    X1 = np.linspace(0, n - 1, 100)
    V = scipy.optimize.curve_fit(lambda t,a,b: a*np.exp(b*t),  X,  Y,  p0=(4, 0.1))
    plt.plot(X1, V[0][0]*np.exp(X1*V[0][1]), 'r--', label = "Aexp(Bx)")
    plt.plot(X, Y)
    plt.legend()
    plt.show()
    print(m.exp(V[0][1])) #On tend vers la constante de Conway quand n est grand, 1,303 577 269
    
def trace_longueur_log(n):
    """Comme avant mais en echelle log"""
    X = [k for k in range(n)]
    Y = [len(liste_terme(i)) for i in range(n)]
    X1 = np.linspace(0, n - 1, 100)
    V = scipy.optimize.curve_fit(lambda t,a,b: a*np.exp(b*t),  X,  Y,  p0=(4, 0.1))
    plt.plot(X1, V[0][0]*np.exp(X1*V[0][1]), 'r--', label = "Aexp(Bx)")
    plt.plot(X, Y)
    plt.legend()
    plt.yscale('log')
    plt.show()

    