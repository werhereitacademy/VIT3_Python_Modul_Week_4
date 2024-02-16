from kitap_islemleri import *
from uye_islemleri import *
from zaman import *

while True:
    secim = input(
        "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~≀" +
        "\n≀                                                                                ≀"+
        "\n≀   Uyelik islmeleri icin 1'e basin                                              ≀" +
        "\n≀   Kitap islemleri 2'ye basin                                                   ≀" +
        "\n≀   Cikis icin 0'e basin                                                         ≀" +
        "\n≀                                                                                ≀" +
        "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~≀\n")

    if secim == "1":
        secim1 = input(
            "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~  ≀" +
            "\n≀                                                                          ≀" +
            "\n≀   Uyeler icin 1'e basin           Kitap Odunc almak icin 5`e basin       ≀" +
            "\n≀   Uye eklemek icin 2'ye basin     Kitap Iade vermek icin 6`ya basin      ≀" +
            "\n≀   Uye aramak icin 3`e basin       Kitap Takibi icin 7`ye basin           ≀" +
            "\n≀   Uye silmek icin 4`e basin       Cikis yapmak icin 0`a basin            ≀" +
            "\n≀                                                                          ≀" +
            "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ≀\n")
        if secim1 == "1":
            uyeler()
        elif secim1 == "2":
            uye_ekle()
        elif secim1 == "3":
            uye_ara()
        elif secim1 == "4":
            uye_silme()
        elif secim1 == "5":
            kitap_odunc_verme()
        elif secim1 == "6":
            kitap_iade()
        elif secim1 == "7":
            kitap_takip()
        elif secim1 == "0":
            continue

    elif secim == "2":
        secim2 = input(
            "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~  ≀" +
            "\n≀                                                                          ≀" +
            "\n≀   Kitaplar icin 1'e basin                                                ≀" +
            "\n≀   Kitap eklemek icin 2'ye basin                                          ≀" +
            "\n≀   Kitap aramak icin 3`e basin                                            ≀" +
            "\n≀   Kitap guncellemek icin 4`e basin                                       ≀" +
            "\n≀   Kitap silmek icin 5`e basin                                            ≀" +
            "\n≀   Cikis yapmak icin 0`a basin                                            ≀" +
            "\n≀                                                                          ≀" +
            "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ≀\n")

        if secim2 == "1":
            kitaplar = oku()
            print(kitaplar)
            
        elif secim2 == "2":
            print("Kitap eklemek istediginiz kitabin bilgilerini giriniz:")
            barkod = input("Barkod numarasini giriniz:")
            kitap_adi = input("Kitap adini giriniz:")
            yayinevi = input("Yayinevinigiriniz:")
            dil = input("Dili giriniz:")
            fiyat = input("Fiyati giriniz:")
            yazar = input("Yazari giriniz:")
            kitap_ekle(barkod, kitap_adi, yayinevi, dil, fiyat, yazar)
            print("Kitap ekleme islemi tamamlandi")
            
        elif secim2 == "3":
            barkod = input("Barkod numarasini giriniz:")
            kitap = kitap_ara(barkod)
            if kitap:
                print(kitap)
            else:
                print("Boyle bir kitap bulunamadi")
                
        elif secim2 == "4":
            print("Guncellemek istediginiz kitabin bilgilerini giriniz:")
            barkod = input("Barkod numarasini giriniz:")
            yeni_kitap_adi = input("Yeni kitap adini giriniz:")
            yeni_yayinevi = input("Yeni yayinevinigiriniz:")
            yeni_dil = input("Yeni dili giriniz:")
            yeni_fiyat = input("Yeni fiyati giriniz:")
            yeni_yazar = input("Yeni yazari giriniz:")
            kitap_guncelle(barkod, yeni_kitap_adi, yeni_yayinevi, yeni_dil, yeni_fiyat, yeni_yazar)
            print("Kitap guncelleme islemi tamamlandi")
            
        elif secim2 == "5":
            print("Silmek istediginiz kitabin bilgilerini giriniz:")
            barkod = input("Barkod numarasini giriniz:")
            kitap_sil(barkod)
            print("Kitap silme islemi tamamlandi")
            
                
            
        elif secim == "0":
            continue
    elif secim == "0":
        break
