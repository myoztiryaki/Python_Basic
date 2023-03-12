# personel defteri uygulamasi
# kullanıcıdan alınan bilgileri bir sözlüğe ekleyen
# listeleme ve arama imkanı sunan
# aynı zamanda güncelleme ve silme imkanı veren
# uygulama
# kullanıcıdan alınan bilgiler
# ad,soyad,telefon,adre

personel=[]
while True:

    print("::menü::")
    print("1-ekleme")
    print("2-listeleme")
    print("3-arama")
    print("4-güncelleme")
    print("5-silme")
    print("6-çıkış")
    print("7-listeyi gör")

    secim = input("Seçiminiz")

    if secim=="6":
        print("çıkılıyor...")
        break

    elif secim=="7":
        print(personel)

    elif secim=="1":
        ad=input("ad=")
        soyad=input("soyad=")
        telefon=input("telefon=")
        adres=input("adres=")
        eklenecek_veri= {
            "ad":ad,
            "soyad":soyad,
            "telefon":telefon,
            "adres":adres
        }
        personel.append(eklenecek_veri)
        print("bilgiler eklendi...")

    elif secim=="2":
        print("{:<5}{:<15}{:<15}{:<13}{:<25}".format("NO","AD","SOYAD","TELEFON","ADRES"))
        for key,value in enumerate(personel):
            print("{:<5}{:<15}{:<15}{:<13}{:<25}".format(key+1,value["ad"],value["soyad"],value["telefon"], value["adres"]))
        print("listeleme bitti...")

    elif secim=="3":
        aranan_ad=input("aramak istediğiniz personel adı=")
        adet=0
        print("{:<5}{:<15}{:<15}{:<13}{:<25}".format("NO", "AD", "SOYAD", "TELEFON", "ADRES"))
        for key, value in enumerate(personel):
            if aranan_ad==value["ad"]:
                print("{:<5}{:<15}{:<15}{:<13}{:<25}".format(key + 1, value["ad"], value["soyad"], value["telefon"], value["adres"]))
                adet+=1
        if adet==0:
            print("aradığınız kişi bulunamadı...")

    elif secim=="4":
        aranan_ad = input("güncellemek istediğiniz personel adı=")
        adet=0
        bulunanlar_sozluk={}
        print("{:<5}{:<15}{:<15}{:<13}{:<25}".format("NO", "AD", "SOYAD", "TELEFON", "ADRES"))
        for key, value in enumerate(personel):
            if aranan_ad==value["ad"]:
                print("{:<5}{:<15}{:<15}{:<13}{:<25}".format(key + 1, value["ad"], value["soyad"], value["telefon"],
 value["adres"]))
                adet+=1
                bulunanlar_sozluk[key]=key
        if adet==0:
            print("güncellemek istediğiniz kişi bulunamadı...")
        else:
            sor=int(input("güncellemek istediğiniz kişi no="))
            sor= (sor-1)
            if sor in bulunanlar_sozluk:
                ad=input("yeni ad=")
                soyad=input("yeni soyad=")
                telefon=input("yeni telefon=")
                adres=input("yeni adres=")
                guncellenecek_veri={
                    "ad": ad,
                    "soyad": soyad,
                    "telefon": telefon,
                    "adres": adres
                }
                personel[sor]=guncellenecek_veri
                print("değişiklikler eklendi...")
            else:
                print("hatalı no değeri girildi...")



    elif secim=="5":
        aranan_ad = input("güncellemek istediğiniz personel adı=")
        adet = 0
        bulunanlar_sozluk = {}
        print("{:<5}{:<15}{:<15}{:<13}{:<25}".format("NO", "AD", "SOYAD", "TELEFON", "ADRES"))
        for key, value in enumerate(personel):
            if aranan_ad == value["ad"]:
                print("{:<5}{:<15}{:<15}{:<13}{:<25}".format(key + 1, value["ad"], value["soyad"], value["telefon"],
                                                             value["adres"]))
                adet += 1
                bulunanlar_sozluk[key] = key
        if adet==0:
            print("silmek istediğiniz kişi bulunamacı")
        else:
            sor = int(input("silmek istediğiniz kişi no="))
            sor = (sor - 1)
            if sor in bulunanlar_sozluk:
                del personel[sor]
                print("personel bilgieleri silindi")

            else:
                print("hatalı no değeri girildi...")

