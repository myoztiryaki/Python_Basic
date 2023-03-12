#kümeler sırasız yapıda, tek baslarına kullanılmazlar

#küme tanımlama
# kume={"mustafa","muhammet","kerem","oğuz","ali"}
# print(type(kume))
# print(kume) #sonucu karısık sıra ile getiriyor.

# bos küme tanımlama

#kume=set()
#print(type(kume))
#print(kume)

#kume={20,30,28,26,39,28,30}
#print(kume)
# kümeler tekrar eden öğeleri yazmaz bir kere gösterir.
# çıktı böyle olur {20, 39, 26, 28, 30}

# listeyi kumeye dönüştürme
# liste=[10,20,"elma","armut",10]
# kume=set(liste)
# print(kume)

# tekrar eden öğeleri teke düşürerek listeyi yazdırmak için ideal.

#karakter dizilerini kümeye dönüştürme

# karakter_dizisi="irem"
# kume=set(karakter_dizisi)
# print(kume),

# kume=set("merve")
# print(kume)
# print(sorted(kume))

#kümeyi sıralama

# kume={"mustafa","muhammet","kerem","oğuz","ali"}
# print(type(kume))
#
# liste=list(kume)
# print(type(liste))
# print(liste)
# liste.sort()
# print(liste)

#kümeye eleman ekleme
# kume={1,2,3}
# kume.add(4)
# print(kume)

# kumenin ilk elemanını silme
#kume=set("elma")
#print(kume)
#kume.pop()
#print(kume)

# silme herhangi bir değeri silme
kume=set("elma")
kume.remove("a")
print(kume)
