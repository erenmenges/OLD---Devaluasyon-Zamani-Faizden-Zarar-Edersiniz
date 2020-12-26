para = int(input("Parayı gir: "))
faizilk = int(input("Faiz oranını girin (nokta veya virgül koyma ve 4 basamaklı gir[örn:%11,25 --> 1125]):"))
dolar_kuru = float(input("Dolar kurunu girin:"))
paradolar = (para / dolar_kuru)
places = 4
faiz = faizilk * (10 ** (-1 * places))
faizlipara = para + (para * faiz)
faizliparadolar = faizlipara / dolar_kuru
dolargelecek = dolar_kuru
while (faizlipara/dolargelecek) >= (para/dolar_kuru):
    dolargelecek += 0.01
print("Eğer 1 sene sonra dolar kuru ", dolargelecek, " olursa zarar edersiniz.")
