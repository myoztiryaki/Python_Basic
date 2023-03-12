# remove listeden silerken değere göre siler
# sıra no K denir, değer de value denir
# olan değeri silmek (olmayanda silmez. if koymak gerekir)
# aynı kişiden iki tane varsa ilk bulduğunu siliyor sadece
# kisi=["mustafa", "ahmet", "muhammet", "osman"]
# print(kisi)
# kisi.remove("ahmet")
# print(kisi)

# pop methodu
# index no ya göre siler / olmayan no girilirse hata verir
# kisi=["mustafa", "ahmet", "muhammet", "osman", "ahmet"]
# print(kisi)
# kisi.pop(0)
# print(kisi)
# print(kisi.pop(0)) # silineni gösterir

# kisi.pop()  # en sondakini siler
# print(kisi)


# del aralık da belirtilebiliyor silmek için
# kisi=["mustafa", "ahmet", "muhammet", "osman", "ahmet"]
# del kisi[0:2]
# print(kisi)
# del kisi   listeyi komple siler
# print(kisi)

# clear method  liste içini boşaltmaya yarar. Liste boş gelir
# kisi=["mustafa", "ahmet", "muhammet", "osman", "ahmet"]
# print(kisi)
# kisi.clear()
# print(kisi)
