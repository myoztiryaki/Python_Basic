# örnekler

# 1-100 e kadar olan sayıları yazdırma
# i=1
# while i<=100:
#     print(i)
#     i+=1

# 1-100 e kadar olan sayıların toplamı
# i=1
# toplam=0
# while i<=10000000:
#     toplam=toplam+i
#     i+=1
# print("1-100 toplam = ",toplam)

# formül ile 1-100 toplamı
# n*(n+1)/2
# n=100000
# toplam=n*(n+1)/2
# print("1-100 toplam = ",toplam)
#

# 1-10 arası çift sayıları ekrana yazdıran kodu önce while sonra for ile oluşturun
# while dongusu ile cozum

# i=1
# while i<=10:
#     mod= i%2;
#     if mod==0:
#         print(i)
#     i+=1

# for dongusu ile cozum

# for i in range(0,11,2):
#     print(i)
    #veya
# for i in range(0,11):
#     if i%2==0:
#         print(i)


# başlangıç ve bitiş değeri kullanıcıdan alınan sayılardan 3 ve 5'e tam bölünenlerin toplamını hesaplayan kodu oluşturun
# while döngüsü ile
# baslangic = int(input("başlangıç değeri = "))
# bitis = int(input("bitis değeri = "))
# toplam=0
# while baslangic<=bitis:
#     if baslangic%3==0 and baslangic%5==0:
#        # print(baslangic)
#         toplam=(toplam+baslangic)
#     baslangic+=1
# print("2-300 arasındaki 3 ve 5'e tam bölünenlerin toplamı =", toplam)

#for döngüsü ile

baslangic = int(input("başlangıç değeri = "))
bitis = int(input("bitis değeri = "))
toplam=0
for i in range(baslangic,bitis+1):
    if i%15==0:
        toplam = (toplam+i)
print("toplam=", toplam)