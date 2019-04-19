# ALONSO-VIRISSEL Sam DM 5

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

## Constante :

alpha = -30
y0 = 10

## A.1

def Solution(t):
    return np.exp(alpha*t)


def F(t, y):
    return alpha*y


def EulerExplicite(F, a, b, y0, h):
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
    X = np.linspace(0, 5, 200)
    Y = [Solution(t) for t in X]
    plt.figure("figure_A1.pdf")
    plt.plot(X, Y)
    plt.savefig("figure_A1.pdf")

## A.2

def A2():
    plt.figure("figure_A2.pdf", figsize=[14.2, 8])
    
    # Comme c'est pas noté, petite entorce à la consigne pour que ce soit plus clair (il y a plus de graphique que demander)
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
    plt.figure("figure_A4.pdf", figsize=[14.2, 8])
    
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
    t = a
    y = y0
    les_t = [a]
    les_y = [y0]
    while t + h <= b:
        y = newton(lambda Y: Y - y - h*F(t, Y), y)
        t = t + h
        les_t.append(t)
        les_y.append(y)
    return les_t, les_y


## B.2

def B2():
    plt.figure("figure_B2.pdf", figsize=[14.2, 8])

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

# A1()
# A2()
# A4()
B2()
