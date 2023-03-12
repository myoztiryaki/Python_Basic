#pass kavrami
#def topla(): # bunu boş bırakırsak hata alırız ondan pass geçmek gerek
#    pass

#global kavrami

# def fonksiyon():
#     global ad # bu değişkeni fonksiyon dışında her yerde kullanılabilir hale geitrmek için kullanılır.
#     ad="merve"
#     print(ad)
#     ad="furkan"
#
# fonksiyon()
# print(ad)


# fonksiyonlara açıklama eklemek
# Ör: string ifadedeki küçük harf adetini döndürmek için bir fonksiyon yazdık.
# def satırından sonra tek tırnak 3 tane yazıp enter'a basınca param ve return ksımı çıkıyor.
# o alana fonksiyon açıklaması yazılır

def kucukadet(string):
    '''
    bu fonksiyon parametre olarak aldığı kelimede kaç adet küçük harf olduğunu bulur.
    :param string: herhangi bir kelime
    :return: int adet
    '''
    adet=0
    for i in string:
        if i.islower():
            adet +=1
    return adet
print(kucukadet("Merve"))


