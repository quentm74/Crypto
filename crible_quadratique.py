from numpy import gcd, lcm
from sympy import sieve, sqrt
from math import floor

def crible(n):
    S = [-1]
    sieve.extend(23)
    #print(sieve._list)
    for p in sieve._list:
        #print("p = ", p, "; "+str(n)+ "[" +str(p) + "] = ", pow(n, 1, p))
        x = 1
        while True:
            if pow(n, 1, p) == pow(x, 2, p):
                #print("p = ", p, "; " + str(n) + "[" + str(p) + "] = ", pow(n, 1, p))
                print(str(n) + "["+str(p)+"] = " + str(x) + "² [" + str(p) + "]")
                #print("\n")
                S.append(p)
                break
            if x > sqrt(n):
                break
            x += 1
    print("S = ",S)
    m = floor(sqrt(n))
    results = {}
    print("m = ", m)
    ax = 0
    bx = 0
    vx = 0
    for x in [0, 1, -1, 2, -2, 4, -6]:
        ex = []
        Q = q(x,n)
        if estLisse(Q, S):
            ax = x + m
            bx = Q
            decomposition = primeDecomposition(Q)
            for p in S:
                if p in decomposition:
                    ex.append(decomposition[p])
                else:
                    ex.append(0)
            vx = [exi % 2 for exi in ex]
        results[x] = {'ax' : ax, 'bx' : bx, 'ex' : ex, 'vx' : vx}
    for k, v in results.items():
        print("x = ", k, " | ", v)
    A = 1
    B_dict = {}
    for k in S:
        B_dict[k] = 0
    #print(B_dict)
    for k in [-1, 4, -6]:
        A *= results[k]['ax']
        for i in range(len(S)):
            ex = results[k]['ex']
            B_dict[S[i]] += ex[i]
    for k,v in B_dict.items():
        B_dict[k] = int(v/2)
    B = 1
    B_str = "B² = b-1 * b4 * b-6 = "
    for k,v in B_dict.items():
        B *= k**v
        B_str += str(k) + "^" + str(v) + " . "
    print(B_str[:-1])
    print("B = ", B%n)
    print("A = ", A%n)
    print("A² = B²[n] : ", pow(A, 2, n) == pow(B, 2, n))
    #print(pow(a,2,n) == pow(b, 2,n))
    return gcd(abs(A - B), n), gcd(abs(A + B), n)

def q(x, n):
    m = floor(sqrt(n))
    return (x+m)**2 - n

def estLisse(Q, S):
    facteursPremiers = primeDecomposition(Q)
    for p in facteursPremiers:
        if not (p in S):
            return False
    return True

def primeDecomposition(n):
    ret = {}
    ret[-1] = 0
    if n < 0:
        ret = primeDecomposition(abs(n))
        ret[-1] = 1
        return ret
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


if __name__ == "__main__":
    n = 24961
    print(crible(n))