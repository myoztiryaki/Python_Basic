# varsayılan değerli parametre
# örnek bir şirkette kart için ad soyad tel lazım ama bazı kullanıcılar tel girmiyor senaryosu
# ad
# soyad
# telefon

# def kartvizit(ad,soyad,telefon="021200000001"):
#     print("ad",ad)
#     print("soyad",soyad)
#     print("telefon",telefon)
# kartvizit("merve","öztiryaki","05302232323")
# kartvizit("furkan","çetükkaya")  # no yazmazsa yukarıda yazanı alır
# soldan sağa bilgiler gider, sıralama cevabı karışık olursa karışır. ad soyad sırasındaki gibi gitmesi lazım.
#çözümü var

# isim parametresi kullanımı

def kartvizit(ad,soyad,telefon):
     print("ad",ad)
     print("soyad",soyad)
     print("telefon",telefon)
kartvizit(telefon="05302232323",ad="volkan",soyad="kardeş")



