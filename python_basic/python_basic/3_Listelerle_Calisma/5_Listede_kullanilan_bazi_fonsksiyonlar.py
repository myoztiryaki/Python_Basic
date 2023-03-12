# count bir listede kaç tane o değerden olduğunu verir
# liste=["elma", "armut", "kiraz", "armut"]
# print(liste.count("armut"))

# copy
# liste=["elma", "armut", "kiraz", "armut"]
# yeni_liste=liste
# print(yeni_liste)
# yeni_liste.append("fındık")
# print(yeni_liste)
# print(liste) burada aynalama yapıldı.

# liste=["elma", "armut", "kiraz", "armut"]
# yeni_liste=liste.copy()   tamamen listeden bağımsız yeni kopya üzerinde çalışıyor
# yeni_liste.append("fındık")
# print(yeni_liste)
# print(liste)


# extend  iki liste birleştirmekte kullanılır.
# liste1=["elma", "armut", "kiraz", "armut"]
# liste2=["fındık","ceviz"]
# liste1.extend(liste2)
# print(liste1) birleşmiş hali
# print(liste2) tek liste 2


# sort sıralama için kullanılıyor. harfe göre sıraladı
# liste=["elma", "armut", "kiraz"]
# liste.sort()
# print(liste)
# #sıralamayı tersten yapmak istersek
# liste.sort(reverse=True)
# print(liste)


# reverse  sıralama yapmaz sadece tersinden yazar

# liste=["elma", "armut", "kiraz"]
# liste.reverse()
# print(liste)