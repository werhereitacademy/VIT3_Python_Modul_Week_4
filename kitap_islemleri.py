import json
import os

#cwd= current working directory:programin calistigi klasor
cwd= os.getcwd()

#dosya yolundaki ayirici karakter.
path_separator = os.sep
#kitap_dosya_yolu = os.path.join(cwd, "kitap.json")
kitap_dosya_yolu = cwd + path_separator + "kitap.json"
kitap_dosyasi_mevcut = os.path.isfile(kitap_dosya_yolu)


def oku():
    
    if kitap_dosyasi_mevcut:
        with open(kitap_dosya_yolu, "r") as dosya:
            kitaplar = json.load(dosya) 
            return kitaplar
    else:
        with open(kitap_dosya_yolu, "w") as dosya:
            kitaplar = []
            json.dump(kitaplar, dosya)
            return kitaplar
    
#print(oku())

def toplam_kitap_sayisi():
    kitaplar = oku()
    return len(kitaplar)
#print(toplam_kitap_sayisi())

def kayit(veri):

    with open(kitap_dosya_yolu, "w") as dosya:
        json.dump(veri, dosya)
        
def kitap_ekle(barkod, kitap_adi, yayinevi, dil, fiyat, yazar):
    eklenecek_kitap = {
        "Barkod": barkod,
        "Kitap_Adi": kitap_adi,
        "Yayinevi": yayinevi,
        "Dil": dil,
        "Fiyat": fiyat,
        "Yazar": yazar
    }

    kitaplar = oku()
    kitaplar.append(eklenecek_kitap)
    kayit(kitaplar)
    
def kitap_sil(barkod):
    kitaplar = oku()
    silinecek_kitap = None
    for kitap in kitaplar:
        if kitap["Barkod"] == barkod:
            silinecek_kitap = kitap
            break
    if silinecek_kitap:
        kitaplar.remove(silinecek_kitap)
        kayit(kitaplar)
        

def kitap_ara(barkod):
    kitaplar = oku()
    for kitap in kitaplar:
        if kitap["Barkod"] == barkod:
            return kitap
    return None
#print(kitap_ara())


def kitap_guncelle(barkod, yeni_kitap_adi, yeni_yayinevi, yeni_dil, yeni_fiyat, yeni_yazar):
    kitaplar = oku()
    guncellenecek_kitap = None
    for kitap in kitaplar:
        if kitap["Barkod"] == barkod:
            guncellenecek_kitap = kitap
            break
    if guncellenecek_kitap:
        guncellenecek_kitap["Kitap_Adi"] = yeni_kitap_adi
        guncellenecek_kitap["Yayinevi"] = yeni_yayinevi
        guncellenecek_kitap["Dil"] = yeni_dil
        guncellenecek_kitap["Fiyat"] = yeni_fiyat
        guncellenecek_kitap["Yazar"] = yeni_yazar
        kayit(kitaplar)
        
#print(kitap_ara(9786057003768))
#kitap_guncelle(9786057003768, "Kurtulus Kopegi", "Kurtulus Kopegi yayinevi", "Türkce", 50, "Kurtulus Kopegi")
#print(kitap_ara(9786057003768))