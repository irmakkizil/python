iller = {'Tekirdağ':120, 'Ankara':664, 'Çanakkale':233, 'Bursa':436, 'Mersin':1143}

mil_limit = float(input("Mil değeri girin: "))


mil_iller = {sehir: km * 0.621371 for sehir, km in iller.items()}

uzak_iller = [sehir for sehir, mil in mil_iller.items() if mil > mil_limit]

print("Girilen milden uzak şehirler:", uzak_iller)