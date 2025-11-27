import random

sayi=random.randint(1,100)
can=int(input("Kaç hakda bilmek istersiniz"))
hak=can
sayac=0

while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input("Tahmininizi giriniz:"))
    if tahmin == sayi:
        print(f"Tebrikler{sayac}.denemede bildiniz puanınız: {100-(100/can)*(sayac-1)} ")
        break
    elif tahmin<sayi:
        print("Daha yüksek bir tahmin yapınız")
    else:
        print("Daha düşük bir tahmin yapınız.")
    if hak ==0:
        print(f"Hakkınız bitmiştir sayımız:{sayi}")


