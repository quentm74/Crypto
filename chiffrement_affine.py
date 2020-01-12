#exo 3

def chiffre(m, a, b):
    if a % 2 == 0 or a % 13 == 0:
        print("argument a = "+str(a)+" invalide")
        return m
    c = ""
    for x in m.lower():
        c += chr((a*(ord(x) - 97) + b)%26 + 97)
    return c

def inverse(x):
    """0 <= x <= 25"""
    for y in range(1, 26):
        if x*y %26 == 1:
            return y
    print('inverse non trouvé')
    return y

def dechiffre(m, a, b):
    if a == 0:
        print("argument a = 0 invalide")
        return m
    inv_a = inverse(a)
    c = ""
    for x in m.lower():
        c += chr((inv_a*(ord(x) - 97 - b))%26 + 97)
    return c

def test():
    m = "jesuisalondres"
    print("clair : ", m)
    c = chiffre(m, 5, 1)
    print("chiffré : ", c)
    print("dechiffré : ", dechiffre("mprvxrhqjuacprahurvupaprc", 15, 7))

if __name__ == "__main__":
    test()