def chiffre(m, k):
    c = ""
    for x in m.lower():
        c += chr(((ord(x) - 97) + k)%26 + 97)
    return c

def dechiffre(c, k):
    return chiffre(c, -1*k)

def dechiffreSansCle(c):
    """approche simple : analyse frequentielle en supposant que la lettre la plus fréquente correspond au e dans le clair
       valable sur des messages en français suffisament longs
    """
    k = 0
    max = 0
    dict = {}
    for x in c:
        if not(x in dict):
            dict[x] = 0
        dict[x] += 1
        if dict[x] > max:
            max = dict[x]
            k = ord(x)-ord('e')
    return dechiffre(c, k)

def findKey(c):
    k = 0
    max = 0
    dict = {}
    for x in c:
        if not(x in dict):
            dict[x] = 0
        dict[x] += 1
        if dict[x] > max:
            max = dict[x]
            k = ord(x)-ord('e')
    while k < 0:
        k += 26
    return k



def test():
    m = "je veux une enorme epee"
    print("message :", m)
    c = chiffre(m, 1)
    print("chiffré : ", c)
    print("déchiffré :", dechiffre(c, 1))

    print("déchiffré par analyse fréquentielle", dechiffreSansCle(c))

if __name__ == "__main__":
    test()