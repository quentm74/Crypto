def chiffre(m, n, e):
    return pow(m, e, n)

def chiffre(c, n, d):
    return pow(c, d, n)

def inverse(a, n):
    t = 0
    newt = 1
    r = n
    newr = a
    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)
    if r > 1:
        return "a is not invertible"
    if t < 0:
        t = t + n
    return t

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    pass