import Fp
from sympy import sieve
from math import sqrt
import numpy as np

def primeDecomposition(n):
    ret = {}
    k = int(sqrt(abs(n)))
    sieve.extend(k)
    for p in sieve._list:
        if n % p == 0: # p divise n
            # recherche de la puissance dans le decomposition
            k = 1
            while n % (p ** k) == 0:
                k +=1
            ret[p] = k-1
    return ret

def log_discret(g, n):
    """recherche du log discret en base g dans Fn"""
    B = [2, 3, 5, 7, 11] # base
    I = [12, 18, 62, 100, 143, 206] #donné dans l'énoncé
    Sys = {}
    for i in I:
        x = pow(g, i, n)
        #testList = [(k in B) for k in primeDecomposition(x)]
        print("i = ", i)
        print(str(g) + "^" + str(i) + " = ", x)
        decomp = primeDecomposition(x)
        test = contains(list(decomp.keys()), B)
        print(list(primeDecomposition(x).keys()), " in ", B, " : ", test)
        if test:
            Sys[i] = {}
            for p in B:
                if p in decomp:
                    Sys[i][p] = decomp[p]
                else :
                    Sys[i][p] = 0
    print("Système linéaire")
    M = np.zeros((len(I), len(B)))
    Y = np.zeros((len(I), 1))
    X = []
    i = 0
    for key, val in Sys.items():
        Y[i, 0] = key
        equation = str(key) + " = "
        ligne = []
        for p, l in val.items():
            ligne.append(l)
            equation += str(l) + ".log_" + str(g) + "(" +str(p)+ ") +"
        M[i] = ligne
        i += 1
        print(equation[: -2])

    for p in B:
        log_str = "log_" + str(g) + "(" + str(p) + ")"
        X.append(log_str)
    print("Y = ")
    print(Y)
    print("M = ")
    print(M)
    print("transposée de X = ")
    print(X)
    print("On cherche X tel que Y = M*X")

    print("Faire du pivot de Gauss")


def contains(L1, L2):
    "test si L1 est inclus dans L2"
    for l1 in L1:
        if not (l1 in L2):
            return False
    return True

if __name__ == "__main__":
    log_discret(6, 229)