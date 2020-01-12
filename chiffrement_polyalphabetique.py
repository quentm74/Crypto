# Exo 5
#que des minuscules

def dictK(K):
    dict = {}
    for i in range(0,26):
        #dict[i] = (K*i)%26
        dict[chr(i+97)] = chr((K*i)%26+97)
    return dict

def isValid(dict):
    L = []
    for k, v in dict.items():
        if v in L:
            return False
        else:
            L.append(v)
    return True


def validKeys():
    for i in range(1, 26):
        dict = dictK(i)
        if isValid(dict):
            print(i)

def chiffre(K, IV, m):
    c = str(IV)
    IV = ord(IV)-97
    dict = {}
    for i in range(0,26):
        #dict[i] = (K*i)%26
        dict[chr(i+97)] = chr((K*i)%26+97)
    #print(dict)
    for i in range(0,len(m)):
        #index = (ord(c[i]) - 97 + ord(m[i+1]) - 97)%26
        #print(chr(index+97))
        c += dict[chr((ord(c[i]) - 97 + ord(m[i]) - 97)%26+97)]
    return c

def inv_dict(dict):
    new_dict = {}
    for k, v in dict.items():
        new_dict[v] = k
    return new_dict

def dechiffre(c, K):
    IV = ord(c[0])-97
    m = ""
    dict = inv_dict(dictK(K))
    #print(dict)
    for i in range(1, len(c)):
        m += chr((ord(dict[c[i]]) - ord(c[i-1]))%26 + 97)

    return m
if __name__ == "__main__":
    #validKeys()
    K = 19

    m = "jevoudraisquemonamourmeure"
    print("clair : ", m)
    c = chiffre(K, 'm', m)
    print("chiffré : ", c)
    print('\n')
    m =  "heureuxquicommeulysseafaitunbeauvoyage"
    print("clair : ", m)
    print("chiffré : ", chiffre(K, 'h', m))
    print("déchiffré : ", dechiffre("hgimfppuimqeesymkjdjtvjgkevzujnndomiwms", K))
    print('\n')
    m =  "etlesruellesoujevaispleurantcellequicrutmaimer"
    print("clair : ", m)
    print("chiffré : ", chiffre(K, 'h', m))
    print("déchiffré : ", dechiffre("waxwaejfpabrpfhscvjlfqtvzselyaypaygaworbqmumoej", K))