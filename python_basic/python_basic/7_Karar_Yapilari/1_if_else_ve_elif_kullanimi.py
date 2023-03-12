#karar yapıları

#if
# if sart:
#    şart doğru ise
# sayi1=300
# sayi2=20
# print("if öncesi")
# if sayi1==sayi2:
#     print("sayılar eşit")
# print("if sonrası")

#else
# if sayi1==sayi2:
#     print("sayilar eşit")
# else:
#     print("sayılar eşit değil")


#elif
# if sayi1==sayi2:
#     print("sayilar eşit")
# elif sayi1>sayi2:
#     print("sayı bütük sayı 2 den")
# elif sayi1<sayi2:
#     print("sayı2 büyük sayı1 den")

# kisi_yasi = 35  burada eksi de sorun olur
# if kisi_yasi<18:
#     print("çocuk")
# elif kisi_yasi>=18 and kisi_yasi<=45:
#     print("yetişkim")
# else:
#     print("yaşlı")
#
kisi_yasi = 100
if kisi_yasi < 0:
    print("geçersiz yaş")
elif kisi_yasi<18:
    print("çocuk")

elif kisi_yasi <= 45:
    print("yetişkim")
else:
    print("yaşlı")

