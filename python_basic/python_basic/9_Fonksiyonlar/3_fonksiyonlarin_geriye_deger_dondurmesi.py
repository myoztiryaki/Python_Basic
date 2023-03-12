# fonksiyonların geriye değer döndürmesi return
# neden gerekli

# def topla(s1,s2):
  #  print(s1+s2)
# topla(1,2) #3
# topla(3,4) #7
# topla(3,7) #10
# # sonuc1 = topla(1,2)
# # sonuc2 = topla(3,4)
# # topla(sonuc1,sonuc2)
# bunları otomatik yaptırmak istediğimizde sorun verir.
# o yüzden kullanılır değer döndürme

def topla(s1,s2):
    sonuc = (s1+s2)
    return sonuc
# print(topla(1,2))
sonuc1=topla(1,2)
sonuc2=topla(3,4)
print(topla(sonuc1,sonuc2))
