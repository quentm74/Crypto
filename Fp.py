#Groupe multiplicatif

def inverse(x, p):
    print("Calcul de l'inverse de" + str(x) + " dans F_" + str(p))
    for y in range(1, p):
        if (x * y)%p == 1:
            return y
    print("inverse not found")
    return 0

def log(z, g, p):
    "brute force"
    print("Calcul du logarithme de " + str(z) + " en base " + str(g) + " dans F_" + str(p))
    i = 0
    while (g ** i)%p != z:
        i += 1
    return i

def estGenerateur(g, n):
    dict = engendre(g, n)
    L = []
    for k, v in dict.items():
        if v in L:
            return False
        else:
            L.append(v)
    return True

def engendre(g,n):
    dict = {}
    print_dict = {}
    for i in range(0, n-1):
        dict[i] = pow(g, i, n)
        print_dict[str(g) + "^" + str(i)] = pow(g, i, n)
    print(print_dict)
    return dict

def generateurs(n):
    L = []
    for g in range(1, n):
        if estGenerateur(g,n):
            L.append(g)
    return L

if __name__ == "__main__":
    #print(log(3, 3, 113))
    print(generateurs(19))