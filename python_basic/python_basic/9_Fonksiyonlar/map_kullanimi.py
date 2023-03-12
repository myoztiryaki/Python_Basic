# map kullanımı

# herhangi bir liste üzerinde işlem yapabilmek için döngü kullanmak gerek normalde.

# sayilar=[1,2,3,4,5,6]
# def kareAl(sayi):
#     return sayi**2

     # yeni_sayilar=[]
# for i in sayilar:
#     yeni_sayilar.append(kareAl(i))
# print("sayılar=",sayilar)
# print("yeni sayılar=", yeni_sayilar)

#aşağıdaki şekilde map kullanmak bizi döngüden kurtarıyor
# yeni_sayilar = list(map(kareAl,sayilar))
# print("sayılar=",sayilar)
# print("yeni sayılar=", yeni_sayilar)

#map ile lambda kullanımı
sayilar=[9,2,3,4,5,6]
yeni_sayilar = list(map(lambda x:x**2,sayilar))
print("sayılar=",sayilar)
print("yeni sayılar=", yeni_sayilar)
