#silme
# del komutu sözlüğü bütün olarak silmemize ve içerisindeki herhangi bir değeri silmemize yarıyor
sozluk={
    "home":"ev",
    "about us":"hakkımızda",
    "product": "ürünler",
    "love": "Furkan"
}
# print(sozluk)
# #del sozluk
# del sozluk["product"]
# print(sozluk)

# pop  siliyor ama çift parantez yapınca geri getiriyor
# print(sozluk)
# print(sozluk.pop("home"))
# print(sozluk)

# pop item  son öğeyi siler

print(sozluk)
print(sozluk.popitem())
print(sozluk)