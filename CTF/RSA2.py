from CTF.RSA import *
# RSA faible par p petit

n = int("0xfc20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000162755d", 16)
e = int("0x10001", 16)
C = int("0x86BF46BE70463B7ABC0DC63724052F3D32461DC871D0BD14F7366612F8665429AA6AB76A9445F53D8892710FF4E1C47EF49CCF0E84B28D1580111257C0345DE78BFB39B82676B112A6CAC16E64E21BA5E0A0CA95FD6C91085E5E08CBEDE6EEDF6C543579D5728A4F81BEADD4A6F0964DA72A773FF3D0F247FBE9634DA8890F33ACDE48CD865C04D9972C4933AF59F485C2E595D37FC676BD773997045D2C667A089EA9F9BDA3EC22983F4EFE9804A9167ADBCCA7423E1A517BD2A07E3449F4D7EFF3B5968867DC249E186B313A8A52972F1AFFFAB4D3A7490DB43A544C6B60C7FEAEDAF316B7821365AD607FAAD9844545B005BE948A9FDFA72F6D8AAC6DEFA6", 16)

#recherche par force brute de factirisation
#i = 2
#while i*i < N:
#    if N%i == 0:
#        print(i)
#    i += 1

p = 2017
q = n//2017

l = (p - 1) * (q - 1)

d = inverse(e, l)

#print("l = ", hex(l))
#print("e = ", hex(e))
d = inverse(e, l)
#print("d = ", hex(d))
#print("(e*d)%l", (e * d) % l)  # verification de l'inverse

print(dechiffreRSA(C, d, n))