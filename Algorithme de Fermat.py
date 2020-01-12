#Algorithme de Fermat
#Permet de factoriser n quand p et q sont proches

import math
import decimal
from mpmath import *

mp.dps = 1000

def fermat(n, gap):
    """
    :param n: nombre n a factoriser
    :param gap: ecart maximal entre p et q tels que p*q = n
    :return: p,q ou 0,0 sinon
    """
    mp.dps = 1000
    t = int(mp.ceil(mp.sqrt(n)))
    i = 0
    print("ceil(sqrt(n)) = ", t)
    while i < gap:
        print("t = ", t)
        S = mp.sqrt(t**2-n)
        for s in [int(mp.floor(S)), int(mp.ceil(S))]:
            s = int(s)
            p, q = t + s, t - s
            print("p, q = ", p, q)
            if t**2 - s**2 == n:
                print("t, s = ",t,s)
                p, q = t+s, t-s
                print("p, q = ", p, q)
                print("p*q = ", p*q, p*q == n)
                return p,q
            else:
                print("couple non valide\n")
        i += 1
        t = t + 1
    print("not found")
    return 0,0


if __name__ == "__main__":
    n = 23360947609
    print(fermat(n, 100))

    n = 129247  # Annale 2014-2015 Exo 4
    print(fermat(n, 100))

    n = 6231991  # Annale 2016-2017 Exo 3
    print(fermat(n, 100))
    #n = int("72713263660449766426608472549507391910999231006859839072293277211930474062452754509693703175926555293299615412074270543861769008088604572463948342869508637021419474076427241206437944938376717240291129686364152028622782491945894451364135712261571383558808703167081686346497045755967398069366992898028843416326594059159360945225284437265452305026530558851261461407313179909199142952410034771259750893821607265895711622021931476259859521140803686769209181624642002505705545369907574213821797166658086604390026010586426855858307310109286968521620565824527905076885825311366304226821384729621409305187812305643335912249991", 10)
    #print(fermat(n, 100))

