#Groupe multiplicatif

def inverse(x, p):
    print("Calcul de l'inverse de" + str(x) + " dans F_" + str(p))
    for y in range(1, p):
        if (x * y)%p == 1:
            return y
    print("inverse not found")
    return 0

def log(z, g, p):
    print("Calcul du logarithme de " + str(z) + " en base " + str(g) + " dans F_" + str(p))
    i = 0
    while (g ** i)%p != z:
        i += 1
    return i

if __name__ == "__main__":
    print(log(3, 3, 113))