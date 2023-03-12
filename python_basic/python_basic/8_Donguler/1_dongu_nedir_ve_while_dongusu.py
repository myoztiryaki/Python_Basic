# dongu nedir? neden kullanilir?
# döngüler yazdığımız kodların belli adetler kadar tekrar etmesini sağlar.
# iki tane döngü var; while ve for döngüleri

# while dongusu ve kullanimi
# while sart:
#    kodlar

# while sayi<=3:
#    print(sayi)
# sonsuz sayi
# sayi=1
# while sayi<=3:
#     print(sayi)
#     sayi=sayi+1
# print(sayi)

liste = ["ismet", "mustafa","ayse", "fatma", "duru","volkan"]
# print(liste[0])

# sira_no=0

# while sira_no<len(liste):   #listenin sonuna kadar len ile liste ulaşıyor.
#     print(liste[sira_no])
#     sira_no=sira_no+1
#
# değer genellikle i şeklinde kullanılır. ör:
i=0
while i<len(liste):
    print(liste[i])
    i=i+1
