#kumelerde kullanılan fonksiyonlar

#union birlesim tekrarlayanları çıkarıp birleştirir
kume1=set("elma")
kume2=set("armut")
# print(kume1.union(kume2))

#isdisjoint kesişim sorgular kesişim var o yüzden false gelir
# print(kume1.isdisjoint(kume2)) # kesişim olmasa true dönerdi

# symmetric_difference eşleşmeyenler
print(kume1.symmetric_difference(kume2))

#esleşmeyen, aynı olmayan benzersiz verileri getiriyor.