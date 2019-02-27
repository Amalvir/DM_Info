# Alonso-Virissel Sam DM n°4

from math import cos, pi
import matplotlib.pyplot as plt


def dv(t):
    """v sans l'intégral en fonction de t"""
    return cos(pi*t/8)


## Rectangle
def rectangles(a, b, f, n):
    """Retourne le calcul approché de l'intégrale de f de a à b par la méthode des
    rectangles avec un pas de n"""
    Rn = 0
    for i in range(n):
        ai = a + i*(b - a)/n
        Rn = Rn + f(ai)
    return ((b - a)/n)*Rn

# 2. n = 100    2.5664267293774436
#    n = 10000  2.5466790842343427
#    n = 10**6  2.5464810894698378


def cv_rectangles(a, b, f, n):
    """Plot les valeurs de Rn en fonction du pas k variant de 1 à n."""
    # R contient les valeurs de Rk pour où k est le pas variant de 1 à n
    R = [rectangles(a, b, f, k) for k in range(1, n + 1)]
    
    # N contient tous les entiers compris entre 1 et n
    N = [k for k in range (1, n + 1)]
    
    plt.plot(N, R, '.', color = 'blue', label = 'Rectangle')
    return None


## Trapèzes
def trapezes(a, b, f, n):
    """Retourne le calcul approché de l'intégrale de f de a à b par la méthode des
    trapèzes avec un pas de n"""
    Tn = 0
    for i in range(1, n):
        ai = a + i*(b - a)/n
        Tn = Tn + f(ai)
    return ((b - a)/n)*((f(a) + f(b))/2 + Tn)

# 2. n = 100    2.546426729377443
#    n = 10000  2.5464790842343428
#    n = 10**6  2.5464790894698375


def cv_trapezes(a, b, f, n):
    """Plot les valeurs de Tn en fonction du pas k variant de 1 à n."""
    # T contient les valeurs de Tk pour où k est le pas variant de 1 à n
    T = [trapezes(a, b, f, k) for k in range(1, n + 1)]
    
    # N contient tous les entiers compris entre 1 et n
    N = [k for k in range(1, n + 1)]
    
    plt.plot(N, T, '.', color='red', label='Trapezes')
    return None


## Simpson
def simpson(a, b, f, n):
    """Retourne le calcul approché de l'intégrale de f de a à b par la méthode de
    Simpson avec un pas de n > 0"""
    if n <= 0:
        raise ValueError("Le pas doit être strictement positif")
    Sn = 0
    for i in range(1, n+1):
        ai_1 = a + (i - 1)*(b - a)/n
        ai = a + i*(b - a)/n
        Sn = Sn + f(ai_1) + 4*f((ai_1 + ai)/2) + f(ai)
    return ((b - a)/(6*n))*Sn

# 2. n = 100    2.5464790895241523
#    n = 10000  2.546479089470363
#    n = 10**6  2.5464790894700537


def cv_simpson(a, b, f, n):
    """Plot les valeurs de Sn en fonction du pas k variant de 1 à n."""
    # S contient les valeurs de Sk pour où k est le pas variant de 1 à n
    S = [simpson(a, b, f, k) for k in range(1, n + 1)]
    
    # N contient tous les entiers compris entre 1 et n
    N = [k for k in range (1, n + 1)]
    
    plt.plot(N, S, '.', color='green', label='Simpson')
    return None


def main():
    """Fonction principale"""
    cv_rectangles(0, 4, dv, 200)
    cv_trapezes(0, 4, dv, 200)
    cv_simpson(0, 4, dv, 200)
    #plt.xscale('log')
    plt.legend()
    plt.title("Comparaison des différentes méthodes de calcul d\'intégrale")
    plt.show()


main()
# La méthode de Simpson converge la plus vite vers la valeur finale. Elle est la
# plus efficace.
# La méthode des trapèzes 