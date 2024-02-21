import json
import os

def oku():
    with open("kitap.json","r", encoding="utf-8") as dosya:
        kitaplar = json.load(dosya)
    #json.load() fonksiyonuyla JSON verisi Python sözlüklerine veya listelere dönüştürülür.
    #Bu dönüştürülmüş veriler kitaplar adlı bir değişkene atanır ve fonksiyon tarafından döndürülür.
    return kitaplar

def kayit(kitaplar):
    with open('kitap.json', 'w') as dosya:
        json.dump(kitaplar, dosya,indent=4)
        print("Verileriniz guncellendi.")
    #kitap ekleme islemeinden sonra bu fonksiyonu cagiriyoruz.

def kitap_ekle():

    yeni_kitap_adi = input("Lutfen yeni kitap ismini yaziniz:")
    yeni_kitap_yazar = input("Lutfen yeni kitabin yazarini yaziniz:")
    yeni_kitap_yayinevi= input("Lutfen yeni kitabin yayin evini yaziniz:")
    yeni_kitap_barkod = input("Lutfen yeni kitabin barkod numarasini yaziniz:")
    yeni_kitap_dil= input("Lutfen yeni kitabin dilini yaziniz:")
    yeni_kitap = {"Barkod":yeni_kitap_barkod, "Dil":yeni_kitap_dil,"Kitap_Adi":yeni_kitap_adi,"Yayinevi":yeni_kitap_yayinevi,"Yazar":yeni_kitap_yazar}
    kitaplar = oku()
    kitaplar.append(yeni_kitap)
    kayit(kitaplar)
#oku() fonksiyonunu kullanarak JSON dosyasındaki mevcut kitapları alıyoruz.
#Yeni kitap bilgileri, oluşturulan bir sözlük olarak eklenir ve mevcut kitaplar listesine eklenir
#Son olarak,kayit fonksiyonunu cagirarak kaydediyoruz..

def kitap_sil(silinecek_kitap):
    silinecek_kitap = input("Lutfen silmek istediniz kitabi yaziniz:")
    kitaplar = oku()
#Burada mevcut elimizde olan kitaplari aliyoruz.
    yeni_kitaplar = [kitap for kitap in kitaplar if kitap["Kitap_Adi"]!=silinecek_kitap]
#Burada input olarak aldigimiz silinecek kitabi filitreleyerek yeni kitap listesi olusturuyoruz.
    with open("kitap.json","w") as dosya:
        json.dump(yeni_kitaplar,dosya)
#Kalan kitaplari guncellenmes sekilde kitap.json dosyasina yaziyoruz.

def kitap_ara():
    kitaplar=oku()
    aranacak_kitap= input("Lutfen aramak istediginiz kitabi giriniz:")
    aranacak_kitap= aranacak_kitap.lower()
    bulunan_kitaplar=[]
    for kitap in kitaplar:
        if aranacak_kitap in kitap["Kitap_Adi"].lower():
            bulunan_kitaplar.append(kitap)
    if len(bulunan_kitaplar) >=1:
        print("Bulunan kitaplar;")
        for i in bulunan_kitaplar:
            print(i)
    else:
        print("Girmis oldugunuz kitap adinda kitap bulunamadi.")

def kitaplar():

    secim= input("Kutuphanemizde olan kitaplari gormek icin`1`\nGeri donmek icin`0`a basiniz:")
    kitaplar= oku()
    n=1
    if secim =="1":
        for kitap in kitaplar:
            print(f"{n}.",kitap["Kitap_Adi"])
            n+=1
    elif secim =="2":
        return
if __name__ == "__main__":
    print("islem")
    kitap_ekle()

