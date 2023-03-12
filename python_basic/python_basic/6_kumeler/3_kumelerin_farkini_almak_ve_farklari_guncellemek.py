# kümelerde kullanılan fonksiyonlar

#difference kümelerin farkını alır
kume1 = set("elma")
kume2 = set("armut")
# farklari = kume1.difference(kume2)
# farklari = kume2.difference(kume1)
# print(farklari)

# difference_update kümelerin farkını kümeye günceller
print("kume1",kume1)
print("kume2",kume2)
kume1.difference_update(kume2)
print("kume1",kume1)
