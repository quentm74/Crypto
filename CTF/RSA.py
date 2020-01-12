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

def dechiffreRSA(C,d,n):
    m = pow(C, d, n)  # dechiffrage
    #print("m = ", bytearray.fromhex(hex(m)[2:]).decode())  # conversion
    return bytearray.fromhex(hex(m)[2:]).decode()

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True