# EXO 4

import numpy as np

def chiffre(M, K):
    return np.dot(K, M)

def dechiffre(C, K):
    inv_K = np.linalg.inv(K)
    print(np.dot(K, inv_K))
    return np.dot(inv_K, C)

def findKey(M_cat, C_cat):
    return np.dot(C_cat, np.linalg.inv(M_cat))



def test():
    M = np.array([[10],[21]])
    K = np.array([[5, 12], [1, 3]])
    print("message : \n", M)
    C = chiffre(M, K)
    print("chiffré : \n", C)
    print("déchiffré : \n", dechiffre(C, K))

    print('recherche de clé \n')
    M_cat = np.array([[2, 7], [9, 3]])
    C_cat = np.array([[11, 11], [11, 23]])
    key = findKey(M_cat, C_cat)

    print("Clé trouvée")
    print(key)

    print("Verification")
    print(np.dot(key, np.array([[2], [9]])))
    print(np.dot(key, np.array([[7], [3]])))

if __name__ == "__main__":
    test()