import json
import os
from kitap_islemleri import kitap_sil,kayit,oku
from zaman import simdiki_zaman, on_dort_gun_sonrasi
from datetime import datetime,timedelta
"""Kitap iade verme ile devam edecegim, En son elimde olan kitaplari goruntuledim./13-02-2024-11:23"""

def uye_dosya_ac():
    if os.path.exists("uye.json"):
        with open("uye.json", "r") as uyeler_dosyasi:
            try:
                uyeler = json.load(uyeler_dosyasi)
            except json.decoder.JSONDecodeError:
                uyeler = []
#Buradan dosyanin olup olmadigini kontrol ediyoruz. Eger dosya varsa dosyayi bize veriyor dosya yoksa liste olarak donduruyor.
#Liste olmasi durumunda kaydettigimiz zaman dosyaya olusturuyoruz.

    else:
        uyeler = []
    return uyeler

def uyeler():
    uyeler= uye_dosya_ac()

    for uye in uyeler:
        print("id:",uye["id"],"Uye isim:",uye["Üye adı"])

def uye_guncelle():
    id = int(input("Lutfen bilgilerini guncellemek istediginiz uyenin id numarsini giriniz:"))
    uyeler= uye_dosya_ac()
    for uye in uyeler:
        if uye["id"] == id:
            yeni_uye_adi = input("Lütfen guncel üye adını giriniz: ")
            yeni_uye_adres = input("Lütfen guncel üye adresini giriniz: ")
            yeni_tel_numarasi = input("Lütfen guncel üyeye ait telefon numarasını giriniz: ")
            uye["Üye adı"]=yeni_uye_adi
            uye["Tel"]=yeni_tel_numarasi
            uye["Adres"]=yeni_uye_adres
            uye_kaydet(uyeler)


def uye_kontrol(uyeler,id):
    for uye in uyeler:
        if uye["id"]== id:
            return True
    else:
        return False
#Burada uyeleri kontrol eden bir fonksiyon yazdim. Uye ekleme sirasinda bunun yardimi ile kontrol edip ayni id numarasindan olup olmadigini sorgulayacagim.
def uye_kaydet(uyeler):
    with open("uye.json", "w") as uyeler_dosyasi:
        json.dump(uyeler, uyeler_dosyasi, indent=4)
        print("Basariyla guncellendi.")
#Burada bir kadet fonksiyonu olusturdum. Uye ekleme veya silme isleminden sonra guncel hali kaydediyorum.
def uye_ekle():
    uyeler = uye_dosya_ac()
    id = int(input("Bir ID numarası giriniz: "))
    if uye_kontrol(uyeler, id):
        print(f"{id} id numarası zaten sistemde mevcut.")
        return
#Bu kisima kadar once uye dosyasini okuyorum sonra daha once olusturdugum uye kontrol fonksiyonu ile id kontrolu yapiyorum.
    uye_adi = input("Lütfen üye adını giriniz: ")
    uye_adres = input("Lütfen üye adresini giriniz: ")
    tel_numarasi = input("Lütfen üyeye ait telefon numarasını giriniz: ")

    yeni_uye = {"id": id, "Üye adı": uye_adi, "Tel": tel_numarasi, "Adres": uye_adres}
    uyeler.append(yeni_uye)
    print(uyeler)
 #Yeni uyemi bir sozluk haline getiriyorum ve daha once fonksiyon ile uyeler listeme ya da onceden olusturlmus dosyama ekliyorum.
    uye_kaydet(uyeler)
 #kaydetme fonksiyonum ile guncel hali kaydediyorum.

def uye_ara():
    uyeler = uye_dosya_ac()
    #Burada onceden olusturdugumuz fonksiyonu kullanarak uyelere ya da bos listeye ulastik.
    aranan_uye = int(input("Aramak istediginiz uyenin id numarisini girini:"))
    for uye in uyeler:
        if uye["id"]== aranan_uye:
            print("Aramis oldugunuz uyenin bilgileri:",uye)
            break
        #Burada else yapmadim, cunku aksi takdirde her uyede ulasilamadi diye ayrica yazi basacakti

    else:
        print("Aramis oldugunuz id`ye ulasilamadi.")



def uye_silme():
    uyeler =uye_dosya_ac()
    silinecek_uye = int(input("Lutfen silmek istediginiz id yi yaziniz:"))
    for uye in uyeler:
        if uye["id"]== silinecek_uye:
            uyeler.remove(uye)
    uye_kaydet(uyeler)
    print(f"{silinecek_uye} numaralı üye başarıyla silindi.")

def kitap_odunc_verme():
    while True:
        odunc_kitap_tercih = input("Hangi kitabi odunc almak istiyorsunuz (Giris sayfasina donmek icin: 0`a basin)")
        if odunc_kitap_tercih == "0":
            return  # Giriş sayfasına dön

        with open("kitap.json", "r", encoding="utf-8") as dosya:
            kitaplar = json.load(dosya)

        kitap_bulundu = False
        for kitap in kitaplar:
            if kitap["Kitap_Adi"] == odunc_kitap_tercih:
                kitap_bulundu = True
                break

        if not kitap_bulundu:
            print("Kitap bulunamadı. Lütfen tekrar deneyin.")
            continue

        while True:
            try:
                id = int(input("Lutfen id numarinizi giriniz:"))
                uyeler = uye_dosya_ac()
                for uye in uyeler:
                    if uye["id"] == id:
                        takip = takip_oku()
                        takip.append({"Üye": uye, "Kitap": kitap, "ödünç_tarihi": simdiki_zaman(),
                                      "iade_tarihi": on_dort_gun_sonrasi()})
                        takip_yaz(takip)

                        yeni_kitaplar = [k for k in kitaplar if k["Kitap_Adi"] != odunc_kitap_tercih]
                        kayit(yeni_kitaplar)
                        print("Kitap ödünç verildi.")
                        return
                else:
                    print("Bu üye bulunamadı. Lütfen tekrar deneyin.")
            except ValueError:
                print("Lütfen geçerli bir ID numarası girin.")

def takip_yaz(takip):
    for odunc in takip:
        odunc["ödünç_tarihi"] = datetime.strptime(odunc["ödünç_tarihi"], "%Y-%m-%d").strftime("%Y-%m-%d")
        odunc["iade_tarihi"] = datetime.strptime(odunc["iade_tarihi"], "%Y-%m-%d").strftime("%Y-%m-%d")

    with open("takip.json", "w") as takip_dosyasi:
        json.dump(takip, takip_dosyasi, indent=4)
        print("Başarıyla güncellendi.")

def takip_oku():
    if os.path.exists("takip.json"):
        with open("takip.json", "r") as takip_dosyasi:
            try:
                takip = json.load(takip_dosyasi)
            except json.decoder.JSONDecodeError:
                takip = []
    else:
        takip = []
    return takip


def kitap_iade():
    # Kullanıcıdan üye ID'sini alıyoruz.


    # Üyelerin bulunduğu JSON dosyasını okuyoruz.
    uyeler = uye_dosya_ac()

    # Girilen ID'nin uyeler listesinde bulunup bulunmadığını kontrol ediyoruz.
    while True:
        id = int(input("Lütfen id numaranızı giriniz:"))
        if uye_kontrol(uyeler, id):
            print("Tesekkur ederiz giris yapiliyor..")
            break
        if not uye_kontrol(uyeler, id):
            print("Bu id numarasına sahip bir üye bulunamadı")
    # Ödünç alınan kitapların kaydedildiği takip JSON dosyasını okuyoruz.
    takip_dosya = takip_oku()
    n = 0

    # Ödünç alınan kitaplar içindeki kitapları listeliyoruz.
    for odunc in takip_dosya:
        if odunc["Üye"]["id"] == id:
            n += 1
            print("Elinizde bulunan kitaplar:")
            print("-" * 30)
            kitap_bilgisi = odunc["Kitap"]
            print(f"Elinizde olan {n}. kitap: Kitabın Adı: {kitap_bilgisi['Kitap_Adi']} - Yazarı: {kitap_bilgisi['Yazar']} - Yayınevi: {kitap_bilgisi['Yayinevi']}")
            print("-" * 30)

            # Kullanıcıdan iade etmek istediği kitap adını alıyoruz.

    while True:
        iade_kitap_adi = input("Hangi kitabı iade etmek istiyorsunuz:\nGeri donmek icin 0`a basin. ")
        if iade_kitap_adi == "0":
            return
        for odunc in takip_dosya:
            if odunc["Üye"]["id"] == id and odunc["Kitap"]["Kitap_Adi"].lower() ==iade_kitap_adi.lower():
                kitaplar = oku()
                kitaplar.append(odunc["Kitap"])
                takip_dosya.remove(odunc)
                kayit(kitaplar)
                takip_yaz(takip_dosya)
                print(f"{iade_kitap_adi} adlı kitap başarıyla iade edildi.")

                return

        else:
            print("Girmis oldugunuz kitap sizde gozukmemektedir.")
            continue

def kitap_takip():
    uyeler = uye_dosya_ac()

    # Girilen ID'nin uyeler listesinde bulunup bulunmadığını kontrol ediyoruz.
    while True:
        id = int(input("Lütfen id numaranızı giriniz:"))
        if uye_kontrol(uyeler, id):
            print("Tesekkur ederiz giris yapiliyor..")
            break
        if not uye_kontrol(uyeler, id):
            print("Bu id numarasına sahip bir üye bulunamadı")
    takip_dosya = takip_oku()
    #Eger girilen id varsa takip dosayasindan kitap bilgilerini getiriyoruz.
    n=0
    for odunc in takip_dosya:
        if odunc["Üye"]["id"] == id:
            n += 1
            print("-" * 30)
            kitap_bilgisi = odunc["Kitap"]
            print(f"Elinizde olan {n}. kitap: Kitabın Adı: {kitap_bilgisi['Kitap_Adi']} - Yazarı: {kitap_bilgisi['Yazar']} - Yayınevi: {kitap_bilgisi['Yayinevi']}")
            print("-" * 30)

        else:
            print("Elinizde kitap gozukmuyor.")
            return
"""
def odunc_kitap_dosya_ac():
    if os.path.exists("odunc_kitaplar.json"):
        with open("odunc_kitaplar.json", "r") as odunc_kitaplar_dosyasi:
            try:
                odunc_kitaplar = json.load(odunc_kitaplar_dosyasi)
            except json.decoder.JSONDecodeError:
                odunc_kitaplar = []
    else:
        odunc_kitaplar = []
    return odunc_kitaplar

def odunc_kitaplar_kaydet(odunc_kitaplar):
    with open("odunc_kitaplar.json", "w") as odunc_kitaplar_dosyasi:
        json.dump(odunc_kitaplar, odunc_kitaplar_dosyasi, indent=4)
        print("Basariyla guncellendi.")
"""

if __name__ == "__main__":

    uyeler()