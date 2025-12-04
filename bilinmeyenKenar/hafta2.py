import math

def kisa_kenar_hesapla(hipotenus, diger_kenar):
    return math.sqrt(hipotenus**2 - diger_kenar**2)

def hipotenus_hesapla(kenar1, kenar2):
    return math.sqrt(kenar1**2 + kenar2**2)

def kenarlari_al():
    kenarlar = input("Kenarları virgülle ayırarak girin: ")
    a, b, c = kenarlar.split(",")

    a = None if a.strip() == "?" else float(a)
    b = None if b.strip() == "?" else float(b)
    c = None if c.strip() == "?" else float(c)

    return a, b, c

def bilinmeyeni_hesapla():
    a, b, c = kenarlari_al()

    if a is None:
        return kisa_kenar_hesapla(c, b)
    elif b is None:
        return kisa_kenar_hesapla(c, a)
    elif c is None:
        return hipotenus_hesapla(a, b)
    else:
        return None

sonuc = bilinmeyeni_hesapla()
print("Bilinmeyen kenar:", sonuc)


