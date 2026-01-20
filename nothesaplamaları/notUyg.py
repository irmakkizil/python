def ort_hesapla(satir):
    satir = satir.strip()
    satir = satir[:-1]

    liste = satir.split(":")

    adlar = liste[0]
    notlar = liste[1]

    adlar = adlar.strip()
    notlar = notlar.strip().split(",")
   
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])

    ortalama = (not1+not2+not3)/3
    if ortalama>=90:
        harf="aa"
    elif ortalama>70 and ortalama<90:
        harf="bb" 
    else:
        harf="ff"

    return adlar+":"+harf+"\n"

def not_oku():
     with open("notlar.txt","r",encoding="utf-8") as file:
       for satir in file:
        print(ort_hesapla(satir))
def not_ekle():
    ad = input("ad: ")
    soyad = input("soyad: ")
    not1 = input("not1: ")
    not2 = input("not2: ")
    not3 = input("not3: ")

    with open("notlar.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+" :"+not1+","+not2+","+not3+"\n")

def kayıt_et():
    with open("notlar.txt","r",encoding="utf-8") as file:
        liste=[]

        for i in file:
            liste.append(ort_hesapla(i))

    with open("sonuclar.txt","w",encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)




while True:
    islem= input("1-Notları Oku:\n2-Not Ekle\n3-Notları Kayıt Et:\n4-Çıkış\nseçiminiz:")
    if islem=="1":
        not_oku()
    elif islem == "2":
        not_ekle()
    elif islem =="3":
        kayıt_et()
    else:
        break

