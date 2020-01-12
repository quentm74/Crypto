from numpy import gcd, lcm
from sympy import sieve

def Pollard(n, B, a):
    "renvoie un diviseur non trivial de n"
    if(gcd(n, a) == 1):
        print("a et n premiers entre eux")
    sieve.extend(B)
    puissances = []
    for p in sieve._list:
        k = 0
        while p ** (k+1) < n:
            k += 1
        puissances.append((p, k))
    Q = 1
    for p, k in puissances:
        Q *= p**k
    print("Q = ", Q)
    print("a^Q mod n = ", pow(a,Q,n))
    print("a^Q - 1 mod n = ", pow(a,Q,n) - 1)
    print(gcd(pow(a,Q,n) - 1, n))


if __name__ == "__main__":
    n = 19048567
    B = 19
    a = 3
    Pollard(n, B, a)
