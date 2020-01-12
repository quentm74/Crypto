import math
import Fp
def pas_de_bebe_pas_de_geant(p, g, x):
    m = math.ceil(math.sqrt(p-1))
    print("Calcul du logarithme de " + str(x) + " en base " + str(g) + " dans F_" + str(p))
    print("m = sqrt(" + str(p) + "-1) = ", m )
    table = {}
    for j in range(m):
        table[j] = pow(g, j, p)
    sorted_table = {k: v for k, v in sorted(table.items(), key=lambda item: item[1])}
    print("couples j, " +str(g) + "**j :")
    print(sorted_table)
    y = Fp.inverse(g, p)
    print("couples i, " + str(x) + "*" +str(g) + "^{-" + str(m) + "})^ i")
    print({i:(x * ((y ** m))**i)%p for i in range(m)})
    for i in range(m):
        z = (x * ((y ** m))**i)%p
        for (j, v) in sorted_table.items():
            if v == z:
                print("i, j = ", (i, j))
                e1 = Fp.log(((x * (y**m)**i)%p), g, p)
                print(str(x) + " * (" + str(g) + "^{-" + str(m) + "})^" + str(i) + " = " +str(g)+"^" + str(e1))
                print(str(x) + " = " + str(g) + "^{" + str(i) + "*" + str(m) + "+" + str(e1)  + "} = " +str(g) + "^"+ str(i * m + e1))
                return i * m + e1
def test():
    print(pas_de_bebe_pas_de_geant(113, 3, 57)) # Solution exo 51
    print(pas_de_bebe_pas_de_geant(157, 5, 90)) # Solution Annale 2014-2015 exo 3
    print(pas_de_bebe_pas_de_geant(59, 2, 11))  # Solution Annale 2014-2015 exo 3
    return

if __name__ == "__main__":
    test()