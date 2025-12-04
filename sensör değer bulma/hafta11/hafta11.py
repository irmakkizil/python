import json
import matplotlib.pyplot as plt

with open("idx1.json") as f:
    idx1 = json.load(f)

with open("idx5.json") as f:
    idx5 = json.load(f)

with open("ayar.json") as f:
    ayar = json.load(f)

sicaklik = idx1["result"][0]["Temp"]
nem = idx1["result"][0]["Humidity"]

try:
    hava_kalitesi_str = idx5["result"][0]["Data"]
    hava_kalitesi = int(hava_kalitesi_str.split()[0]) 
except (KeyError, IndexError, ValueError) as e:
    print(f"Hata oluştu: {e}")
    hava_kalitesi = 0

sc_alt = ayar["icsAlt"]
sc_ust = ayar["icsUst"]
nem_alt = ayar["icnAlt"]
nem_ust = ayar["icnUst"]
co2_alt = ayar["co2Alt"]
co2_ust = ayar["co2Ust"]

def renk(deger, alt, ust):
    return "green" if alt <= deger <= ust else "red"

colors = [
    renk(sicaklik, sc_alt, sc_ust),
    renk(nem, nem_alt, nem_ust),
    renk(hava_kalitesi, co2_alt, co2_ust)
]

labels = ["Sıcaklık", "Nem", "Hava Kalitesi"]
values = [sicaklik, nem, hava_kalitesi]

plt.figure(figsize=(8,5))
plt.bar(labels, values, color=colors)
plt.title("Sensör Değerleri")
plt.ylabel("Değer")
plt.show()