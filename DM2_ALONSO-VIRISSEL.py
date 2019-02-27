# Alonso-Virissel Sam  |  PCS3

import math as m
import numpy as np
import matplotlib.pyplot as plt

A=m.pi/3
ndef=1.5

## 1.

    # Arcsinus = asin(x)

## 2.

def angle_r(i,n):
    '''Retourne l'angle de réfraction r correspondant à l'angle incident i traversant un milieu d'indice n. Les angles sont en radians.'''
    r=m.asin(m.sin(i)/n)
    return r

## 3.

def angle_iprime(rprime,n):
    '''Retourne la valeur de l'angle i' en radian s'il y a réfraction en J et False sinon. Le tout en fonction de r' et de l'indice n.'''
    if m.sin(rprime) > 1/n :
        return False
    else :
        iprime=m.asin(n*m.sin(rprime))
        return iprime

## 4.

def deviation(i,n):
    '''Renvoie l'angle de déviation D en radian si il y a réfraction en J, False sinon. Le tout en fonction de l'angle incident i et de l'indice n.'''
    rprime=A-angle_r(i,n)
    iprime=angle_iprime(rprime,n)
    if iprime == False :
        return False
    else :
        return i+iprime-A

## 5.

L_in=np.linspace(0,m.pi/2,100)

## 6.

def emergence(L_in,n):
    '''Renvoie le couple (L_emerg, L_dev) en fonction de L_in et de l'indice n avec :
    L_emerg la liste des angles d'incidence pour lesquels il y a réfraction en J.
    L_dev la liste des angles de déviations D correspondant à ces angles d'incidences.'''
    L_emerg=[]
    L_dev=[]
    for i in range(len(L_in)):
        if deviation(L_in[i],n) != False :
            L_emerg.append(L_in[i])
            L_dev.append(deviation(L_in[i],n))
    return (L_emerg,L_dev)

## 7.

def trace(L_in,n):
    '''Trace la courbe D en fonction de i.'''
    (L_emerg,L_dev)=emergence(L_in,n)
    plt.subplot(211)
    plt.title("D en fonction de i")
    plt.plot(L_emerg,L_dev)
    plt.show()
trace(L_in,ndef)
## 8.

def dev_min(L_in,n):
    '''Renvoie la valeur minimale de D.'''
    (L_emerg,L_dev)=emergence(L_in,n)
    i=0
    while L_dev[i]>L_dev[i+1]: # L_dev décroit puis croit. On peut donc se contenter de cet algorithme.
        i+=1
    return L_dev[i]

## 9.

def cauchy(lmu):
    '''Renvoie l'indice n correspondant à la longueur d'onde lmu.'''
    alpha=1.4906
    beta=0.00679350
    return alpha+beta/lmu**2

def CL_dmin(L_in):
    '''Renvoie la liste L_dmin des valeurs de Dm pour une série de 100 longueurs régulièrement espacées et trace Dm en fonction de lmu'''
    L_dmin=[]
    L_lmu=np.linspace(0.4,0.8,100)
    for i in range(len(L_lmu)):
        n=cauchy(L_lmu[i])
        L_dmin.append(dev_min(L_in,n))
    plt.subplot(212)
    plt.title("Dm en fonction de lmu")
    plt.plot(L_lmu,L_dmin)
    plt.show()
    return L_dmin
CL_dmin(L_in)

## Exercice 2 :

def triplets_pythagoriciens(n):
    L=[]
    (a,b,c)=(0,0,0)
    for i in range(1,n+1):
        for p in range(1,n+1):
            c=m.sqrt(i**2+p**2)
            if int(c) == c and i<=p:
                L.append([i,p,int(c)])
    return L
                
            