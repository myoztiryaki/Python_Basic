# Soru 1: klavyeden alınan 3 adet sayıdan en büyüğünü bulan kısa kodu yazınız.

# benim cevabım
# sayilar=(15,5,9)
# print(sorted(sayilar))
# sayilar=sorted(sayilar)
# print(sayilar[-1])

#hocanın cevabı
# s1=int(input("sayı1="))
# s2=int(input("sayı2="))
# s3=int(input("sayı3="))

# if s1>=s2 and s1>=s3:
#     print("en büyük sayı=", s1)
# elif s2>=s1 and s2>=s3:
#     print("en büyük sayı=", s2)
# elif s3>=s1 and s3>=s2:
#     print("en büyük sayı=", s3)

# if s1>=s2:
#     en_buyuk=s1
# else:
#     en_buyuk=s2
# if s3>en_buyuk:
#     en_buyuk=s3
# print("en büyük sayı=", en_buyuk)


# Soru 2: aşağıdaki notları yazı ile yazan kodu oluşturunuz.
# 0-44    =kaldı
# 45-54   =geçer
# 55-69   =orta
# 70-84   =iyi
# 85-100   =pekiyi

# aralık dışında bir not varsa geçersiz not yazdırınız.

# kisi_notu=100

#benim cevabım

# if kisi_notu < 0:
#     print("Geçersiz not")
#
# elif kisi_notu >= 0 and kisi_notu <= 44:
#     print("kaldı")
#
# elif kisi_notu >= 45 and kisi_notu <= 54:
#     print("geçer")
#
# elif kisi_notu >= 55 and kisi_notu <= 69:
#     print("orta")
#
# elif kisi_notu >= 70 and kisi_notu <= 84:
#     print("iyi")
#
# elif kisi_notu >= 85 and kisi_notu <= 100:
#     print("pekiyi")
# else :
#     print("geçersiz not")

# hocanın cevabı hoca kısa yazmış. 85<=kisi_notu<=100 gibi

# kisi_notu=100
#
# if kisi_notu<0 or kisi_notu>100:
#     print("Geçersiz not")
#
# elif kisi_notu >= 0 and kisi_notu <= 44:
#     print("kaldı")
#
# elif kisi_notu >= 45 and kisi_notu <= 54:
#     print("geçer")
#
# elif kisi_notu >= 55 and kisi_notu <= 69:
#     print("orta")
#
# elif kisi_notu >= 70 and kisi_notu <= 84:
#     print("iyi")
#
# elif kisi_notu >= 85 and kisi_notu <= 100:
#     print("pekiyi")
#




