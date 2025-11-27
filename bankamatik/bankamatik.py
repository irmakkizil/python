HesapA ={
    "Ad":"ahmet",
    "hesapNo":23243434,
    "bakiye":3000,
    "ekHesap":2000
}
HesapB ={
    "Ad":"ali",
    "hesapNo":13243434,
    "bakiye":2000,
    "ekHesap":3000
}

def paraCek(hesap,miktar):
    print(f"merhaba {hesap['Ad']}")

    if hesap["bakiye"]>=miktar:
        hesap["bakiye"]-=miktar
        print("paranızı alabilirsiniz")

    else:
        print("bakiye yetersiz")
        ekHesaptanKulanılacakTutar= miktar-hesap["bakiye"]
        if hesap["ekHesap"]>=ekHesaptanKulanılacakTutar:
            onay=input("ek hesap kullanmak ister misiniz(e/h):")
            if onay == "e":
                hesap["bakiye"]=0
                hesap["ekHesap"]-=ekHesaptanKulanılacakTutar
                print("ek hesap kullanıldı paranızı alabilirsiniz")
            else:
                print("Ana hesapta paranız yetersiz oldugu için işlem tamamlanamadı")
        else:
            print("bakiye yetersiz")

def bakiyeHesapla(hesap):
    print(f"işlem sonrası bakiyeniz {hesap["bakiye"]} dir. ek hesap bakiyeniz {hesap["ekHesap"]} dır.  ")


paraCek(HesapB,1000)
bakiyeHesapla(HesapB)
paraCek(HesapA,5000)
bakiyeHesapla(HesapA)
