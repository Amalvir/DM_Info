# ALONSO-VIRISSEL Sam DM 5

# Si vous avez des questions, hésitez pas. J'ai du demandé à Mme Long pour la complexité notamment, je vous réexplique.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
from time import perf_counter  # Remplace clock en 3.8

## Constante :

alpha = -30
y0 = 10


## A.1

def Solution(t):
    """Solution trouvé par résolution mathématique d'équa diff (chap 4)"""
    return y0*np.exp(alpha*t)


def F(t, y):
    """Retorune y' = alpha*y"""
    return alpha*y


def EulerExplicite(F, a, b, y0, h):
    """Méthode d'Euler vu en cours"""
    t = a
    y = y0
    les_t = [a]
    les_y = [y0]
    while t + h <= b:
        y = y + h*F(t, y)
        t = t + h
        les_t.append(t)
        les_y.append(y)
    return les_t, les_y


def A1():
    """Ce qui est demandé à la question A.1"""
    X = np.linspace(0, 5, 200)
    Y = [Solution(t) for t in X]
    plt.figure("figure_A1")
    plt.plot(X, Y)
    plt.savefig("figure_A1.pdf")

## A.2

def A2():
    """Ce qui est demandé à la question A.2"""
    plt.figure("figure_A2", figsize=[14.2, 8])  # Permet d'enregistrer en plus grand sinon on voit rien sur le pdf
    
    # Comme c'est pas noté, petite entorce à la consigne pour que ce soit plus clair (il y a plus de graphique que
    # demandé)
    for i in range(10, 0, -1):
        X, Y = EulerExplicite(F, 0, 5, y0, i/100)
        plt.subplot(2, 5, 11-i)
        plt.plot(X, Y, label="pas = "+str(i/100))
        plt.title("Pas = "+str(i/100))
        plt.legend()
    
    plt.savefig("figure_A2.pdf")

# On remarque l'apparition d'une sinusoide. En diminuant le pas la sinusoide évolue; elle se retrouve au début puis
# disparait. (On remarque qu'elle est très jolie pour h = 0.07 !)

## A.3

# F(ytk, tk) = alpha*ytk
# D'où, y(tk+1) = y(tk)*(1 + alpha*h) = -2*y(tk)
# Dans le cas où alpha = -30 et h = 0,1; la suite {y(tk)} est une suite géométrique de raison négative inférieur à -1.
# Par conséquent, ses valeurs sont tantôt positive, tantôt négative ce qui conduit à cette divergence.

## A.4

# Rappel : y(tk+1) = y(tk)*(1 - 30*h)
# {y(tk)} converge vers 0 si 1 - 30*h > 0 i.e h < 1/30
hmin = 1/30


def A4():
    """Ce qui est demandé à la question A.4"""
    plt.figure("figure_A4", figsize=[14.2, 8])
    
    X, Y = EulerExplicite(F, 0, 5, y0, hmin-0.01)
    plt.subplot(131)
    plt.plot(X, Y, label="pas = hmin - 0.01")
    plt.legend()
    plt.title("Pas = hmin - 0,01")
    
    X, Y = EulerExplicite(F, 0, 5, y0, hmin)
    plt.subplot(132)
    plt.plot(X, Y, label="pas = hmin")
    plt.legend()
    plt.title("Pas = hmin")
    
    X, Y = EulerExplicite(F, 0, 5, y0, hmin+0.01)
    plt.subplot(133)
    plt.plot(X, Y, label="pas = hmin + 0.01")
    plt.legend()
    plt.title("Pas = hmin + 0,01")
    
    plt.savefig("figure_A4.pdf")



## B.1

# newton(func, x0) Résoue une équation du type func(x) = 0 par une méthode approchée de la méthode de Newton en partant
# de x0

def EulerImplicite(F, a, b, y0, h):
    """Méthode d'Euler Implicite. Bien trop longue à exécuter pour son interêt"""
    t = a
    y = y0
    les_t = [a]
    les_y = [y0]
    while t + h <= b:
        y = newton(lambda Y: Y - y - h*F(t, Y), y)  # Très long à éxécuter
        t = t + h
        les_t.append(t)
        les_y.append(y)
    return les_t, les_y


## B.2

def B2():
    """Ce qui est demandé à la question B.2"""
    plt.figure("figure_B2", figsize=[14.2, 8])

    # Dure de faire quelque chose de clair cette fois vu qu'il n'y a que peu de difference
    for i in range(1, 11):
        X, Y = EulerImplicite(F, 0, 5, y0, i/100)
        plt.subplot(2, 5, i)
        plt.plot(X, Y, label="pas = "+str(i/100))
        plt.title("Pas = "+str(i/100))
        plt.legend()

    plt.savefig("figure_B2.pdf")

# On remarque que le résultat est celui estompé et que si l'on augmente le pas cela ne fait que diminuer la qualité de
# la courbe

## B.3

# F(y(tk+1), tk+1) = alpha*ytk+1
# D'où, y(tk+1) = y(tk)/(1 - alpha*h)
# Dans le cas où alpha = -30 et h = 0,1; la suite {y(tk)} est une suite géométrique de raison comprise entre 1 et -1.
# Par conséquent, cette suite converge vers 0 et la méthode implicite est stable. Néanmoins, le cas où alpha*h = 1 peut
# poser problème. Seulement, dans le cas présent alpha est négatif et comme h ne peut être négatif, alpha*h ne peut être
# égale à 1.


## C.1

def Erreur(h, type):
    """Renvoie l'écart par rapport à la valeur exacte (Solution(t)) en fonction du pas h et du type de résolutio """
    if type == "EulerExplicite":
        les_tk, ynum = EulerExplicite(F, 0, 5, y0, h)
    elif type == "EulerImplicite":
        les_tk, ynum = EulerImplicite(F, 0, 5, y0, h)
    elif type == 'EulerHeun':
        les_tk, ynum = EulerHeun(F, 0, 5, y0, h)
    else:
        # Lève une erreur si le mauvais type est renseigné
        raise ValueError("'EulerExplicite', 'EulerImplicite' ou 'EulerHeun' attendu")
    yvrai = [Solution(t) for t in les_tk]
    return np.max([np.abs(yvrai[k] - ynum[k]) for k in range(len(les_tk))])


## C.2

def C2():
    """Ce qui est demandé à la question C.2"""
    plt.figure("figure_C2", figsize=[14.2, 8])
    les_h = np.linspace(1e-3, 1e-2, 10)

    Expl = [Erreur(h, 'EulerExplicite') for h in les_h]
    plt.plot(les_h, Expl, 'bo', label="Euler Explicite")
    p = np.polyfit(les_h, Expl, 1)  # Regression polynomiale d'ordre 2
    Y = np.poly1d(p)
    lbl = "Modèle Explicite : y = " + str(p[0]) + "X + " + str(p[1])
    plt.plot(les_h, Y(les_h), 'r-', label=lbl)

    Impl = [Erreur(h, 'EulerImplicite') for h in les_h]
    plt.plot(les_h, Impl, 'go', label="Euler Implicite")
    p = np.polyfit(les_h, Impl, 1)  # Regression polynomiale d'ordre 1
    Y = np.poly1d(p)
    lbl = "Modèle Implicite : y = " + str(p[0]) + "X + " + str(p[1])
    plt.plot(les_h, Y(les_h), 'm-', label=lbl)

    plt.legend()
    plt.savefig("figure_C2.pdf")

    # Les 2 epsilon admettent un modèle affine et sont donc des O(h)


## C.3

def EulerHeun(F, a, b, y0, h):
    """Méthode d'Euler Heun. Plutôt rapide mais erreur croissante en O(h**2) donc utiliser des petits pas"""
    t = a
    y = y0
    les_t = [a]
    les_y = [y0]
    while t + h <= b:
        yp = y + h*F(t, y)
        y = y + h/2*(F(t, y) + F(t+h, yp))
        t = t + h
        les_t.append(t)
        les_y.append(y)
    return les_t, les_y

def C3():
    """Ce qui est demandé à la question C.3"""
    plt.figure("figure_C3")
    X, Y = EulerHeun(F, 0, 5, y0, 0.01)
    plt.plot(X, Y)
    plt.title("Résolution par la méthode de Heun")
    plt.savefig("figure_C3.pdf")


## C.4

def C4():
    """Ce qui est demandé à la question C.4"""
    plt.figure("figure_C4", figsize=[14.2, 8])

    les_h = np.linspace(1e-3, 1e-2, 10)
    Heun = [Erreur(h, 'EulerHeun') for h in les_h]

    p = np.polyfit(les_h, Heun, 2)  # Regression polynomiale d'ordre 2
    Y = np.poly1d(p)  # Crée un polynôme avec les carac de p

    plt.plot(les_h, Heun, 'bo', label="Epsilon par la méthode de Heun")

    lbl = "Modèle : y = "+str(p[0])+"X**2 + "+str(p[1])+"X + "+str(p[2])
    plt.plot(les_h, Y(les_h), 'r-', label=lbl)

    plt.legend()
    plt.title("Résolution par la méthode de Heun")
    plt.savefig("figure_C4.pdf")

    # Epsilon peut s'exprimer comme un polynome de degré 2. Par conséquent, Epsilon = O(h**2)


## D.1

def complexite(n):
    """Renvoie les temps d'exécution de chaque méthode comme suit : tps Expl, tps Impl, tps Heun"""
    h = (5 - 0)/n

    t0 = perf_counter()
    EulerExplicite(F, 0, 5, y0, h)
    t1 = perf_counter()
    tps_Expl = t1 - t0

    t0 = perf_counter()
    EulerImplicite(F, 0, 5, y0, h)
    t1 = perf_counter()
    tps_Impl = t1 - t0

    t0 = perf_counter()
    EulerHeun(F, 0, 5, y0, h)
    t1 = perf_counter()
    tps_Heun = t1 - t0

    return tps_Expl, tps_Impl, tps_Heun

## D.2

def D2():
    """/!\\ Méthode très longue !! ~15s"""
    Y1, Y2, Y3 = [], [], []
    X = [i for i in range(1000, 20001, 1000)]
    for x in [complexite(j) for j in X]:
        y1, y2, y3 = x
        Y1.append(y1)
        Y2.append(y2)
        Y3.append(y3)

    plt.figure("figure_D2", figsize=[14.2, 8])

    plt.subplot(131)
    plt.title("Euler explcite, eps = O(h)")
    plt.xlabel("Nombre points")
    plt.ylabel("Temps de calcul en s")
    plt.plot(X, Y1)
    plt.subplot(132)
    plt.title("Euler Implicite, eps = O(h)")
    plt.xlabel("Nombre points")
    plt.ylabel("Temps de calcul en s")
    plt.plot(X, Y2)
    plt.subplot(133)
    plt.title("Euler Heun, eps = O(h**2)")
    plt.xlabel("Nombre points")
    plt.ylabel("Temps de calcul en s")
    plt.plot(X, Y3)
    plt.savefig("figure_D2.pdf")


A1()
A2()
A4()
B2()
C2()
C3()
C4()
D2()
