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


def main():
    # A.1
    X1 = np.linspace(0, 5, 200)
    Y1 = [Solution(t) for t in X1]
    plt.figure("figure_A1.pdf")
    plt.plot(X1, Y1)
    plt.savefig("figure_A1.pdf")

    # A.2
    plt.figure("figure_A2.pdf")
    for i in [-1, -2, -3]:
        X2, Y2 = EulerExplicite(F, 0, 5, y0, 10**i)
        plt.plot(X2, Y2, label="pas = "+str(10**i))
    plt.legend()
    plt.savefig("figure_A2.pdf")

    #plt.show()
main()