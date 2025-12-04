import random

kolonsayısı = int(input("Kaç kolon oluşturmak istiyorsunuz? "))
ugurlusayı=int(input("istediğin uğurlu sayı var mı?(yoksa 0 girin)"))

kolonlar_listesi = []  

if ugurlusayı==0:
    for i in range(0, kolonsayısı):
        kolon = random.sample(range(1, 91), 6)  
        kolonlar_listesi.append(kolon)  
        print(f"{i}. Kolon: {kolon}")
else:
    
         for i in range(0, kolonsayısı):

             kolon = [ugurlusayı]+random.sample(range(1, 91), 5)  
             kolonlar_listesi.append(kolon)  


print("\nTüm kolonlar:", kolonlar_listesi)


