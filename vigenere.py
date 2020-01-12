from numpy import gcd
import cesar


def chiffre(m, k):
    kchain = ""
    i = 0
    while len(kchain) < len(m):
        kchain += k[i%len(k)]
        i += 1
    c = ""
    for i in range(len(m)):
        c += chr(((ord(m[i]) - 97) + (ord(kchain[i]) - 97) )%26 + 97)
    return c

def dechiffre(c, k):
    kchain = ""
    i = 0
    while len(kchain) < len(c):
        kchain += k[i % len(k)]
        i += 1
    m = ""
    for i in range(len(c)):
        m += chr(((ord(c[i]) - 97) - (ord(kchain[i]) - 97)) % 26 + 97)
    return m

def test():
    m = "abcdefghifklmnopqrstuvwxyz"
    k = "aabzgeuvb"
    c = chiffre(m, k)
    m = dechiffre(c, k)
    print(m)

def findKeyLen(c, seuil=10):
    dict = {}
    for i in range(len(c) - 2):
        for j in range(i+1, len(c) - 2):
            if (c[i: i+3] == c[j: j+3] ):
                if j-i in dict:
                    dict[j - i] += 1
                else:
                    dict[j-i] = 1
    print("couples (écart, nb_occurences) avec nb_occurences > " + str(seuil))
    print({k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse= True)})
    l = []
    for k,v in dict.items():
        if v > seuil:
            l.append(k)
    print(l)
    if(len(l) == 1):
        return l[0]
    elif len(l) < 2:
        print("veuillez choisir un seuil plus petit")
        return 1
    #print("la longueur de clé est vraisemblablement le PGCD des ecarts les plus fréquents")
    return gcd.reduce(l)

def find_key(c, l):
    #l = findKeyLen(c)
    Y = [""]*l
    k = ""
    for i in range(l):
        Y[i] = c[i: : l]
        k += chr(cesar.findKey(Y[i]) + 97)
    return k

def MIC(x, y):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    Fx = {}
    Fy = {}
    for c in alphabet:
        Fx[c] = 0
        Fy[c] = 0
    for c in x:
        Fx[c] += 1
    for c in y:
        Fy[c] += 1
    res = 0
    for letter in alphabet:
        res += Fx[letter]*Fy[letter]
    return res/(len(x)*len(y))

def IC(x):
    return MIC(x,x)


def findKeyLen2(m, seuil = 0.03):
    l = 1
    valide = 0
    while valide < l and l < 10:
        #print("dans la boucle l = ", l)
        Y = [""] * l
        valide = 0
        for i in range(l):
            Y[i] = c[i::l]
            #print(i, IC(Y[i]))
            if abs(IC(Y[i]) - 0.0778) < seuil : #seul a ajuster selon la longueur du texte
                valide += 1
        if valide == l:
            return l
        l += 1
    print("longueur non trouvée")
    return 0

def findKey2(m, l, seuil = 0.025):
    Y = [""] * l
    DELTA = [0] * l
    valide = 0
    Y[0] = m[::l]
    for i in range(1, l):
        Y[i] = c[i::l]
        for delta in range(26):
            if abs(MIC(Y[0], cesar.chiffre(Y[i], delta)) - 0.0778) < seuil:
                DELTA[i] = (26 - delta) % 26
                break
    #print(DELTA)
    k = cesar.findKey(Y[0])
    key = ""
    for delta in DELTA:
        key += chr( (k + delta)% 26 +97)

    return key

if __name__ == "__main__":
    #test()
    c = """
        aejifurocdjabmwrncgxvrjifjpolwvrrywceqixderoyvbwyyriaypuubytefwxpceihpwizfpsishgzvohevqicdvrsppzlzyl
        uegfpedsglzngkfzcvuykebndfugfpjozytccsmevlzybleziydahllhuskfvlchafufmfzteopcobncrqiynvshywceeotjegif
        cejybligifwffypkssgpkebacvvswpjtsfwvqiiyvmdltjobhphucheiavcehuchlsabxzenskfzncoduobhpvnjcpuejcgieeot
        uobhpvnjcpuezudlijlpaugkfrupifkjimblaivzltxygfurllzsguyjlohzdmslwlifyyursbzdmoapaozcpwlsocuuaitjdsgl
        zoizclihmllvoaplnsjwrnhymzebjwrnhypjufmpjdsoiaaavpjehkfztfuteeshwzbslevoivzelicdvmpfptegnpclskfvlchx
        rtfubleeopcobjzlrgotkqiywfnhllhuswpjtsfwvqicdvscowvvskfzscoqwrsyejeayevnulpmeqydkezfphuchpdpfcdfnbyb
        lobncrhwnblobumrnriyeeeoteoimofnbypevwyovvwpcvqicofnbypevwyovlomfzvfyulseollbcoeaugkfrupifkjspzldfut
        jsohdcabixdefpzlsduccefxpclsvtvnocxvecoxrlocxvesfwvegnqzdsfpvtgcgfugpzllstblexygfugflgrsmpetsiycadjp
        clslpmoZoeZobjpimohpetswpjtsfwvqiywfnaueiaeophusfzepcocjuwnbleziykrokfvcsmevlzybligydfuzygvqicdfutzc
        vehmpdehyyxrspptegnpclskffnsgai
        """.lower()
    c = c.replace('\n', '')
    c = c.replace(' ', '')
    l = findKeyLen2(c)
    print("l = ", l)
    key = findKey2(c,l)
    print("key = ", key)
    print("déchiffré :\n", dechiffre(c, key))

    #m = "ceciestletexteclairavecbeaucoupdelettresepourquelanalysefrequentiellemarcheeeeeeeeeeeeeeeeeeeeeeee"
    #c = chiffre(m, "secret")
    #l = findKeyLen(c, 1)
    #l = gcd.reduce([109, 218, 1])
    #print("(guess) l = ", l)
    #key = find_key(c, l)
    #print("(guess) key = ", key)
    #print(dechiffre(c, key))

