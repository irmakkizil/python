import random
renkler=["turuncu","kırmızı","mavi","siyah"]
okey_tasları=[(renk,sayi)for renk in renkler for sayi in range(1,14)]*2

def tasCek(taslar):
    while taslar: 
        secilen = random.choice(taslar)
        taslar.remove(secilen)
        yield secilen
    print("tas kalamdı")

cek = tasCek(okey_tasları)
print(next(cek))