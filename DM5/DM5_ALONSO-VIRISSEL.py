# ALONSO-VIRISSEL Sam DM 5

import numpy as np
import matplotlib.pyplot as plt

# Constante :

alpha = -30
y0 = 10

# A.1

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



# A.1
X1 = np.linspace(0, 5, 200)
Y1 = [Solution(t) for t in X1]
plt.figure("figure_A1.pdf")
plt.plot(X1, Y1)
plt.savefig("figure_A1.pdf")

# A.2
plt.figure("figure_A2.pdf")

# Comme c'est pas noté, petite entorce à la consigne pour que ce soit plus clair (il y a plus de graphique que demander)
for i in range(10, 0, -1):
    X2, Y2 = EulerExplicite(F, 0, 5, y0, i/100)
    plt.subplot(2, 5, 11-i)
    plt.plot(X2, Y2, label="pas = "+str(i/100))
    plt.title("Pas = "+str(i/100))
    plt.legend()

plt.savefig("figure_A2.pdf")

# On remarque l'apparition d'une sinusoide. En diminuant le pas la sinusoide évolue; elle se retrouve au début puis
# disparait. (On remarque qu'elle est très jolie pour h = 0.07 !)
