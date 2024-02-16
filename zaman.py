import datetime
"""
üyelerimize kitabımızı 2 haftalık süreyle ödünç vermekteyiz.
Bu yüzden ödünç verdiğimiz andaki saat ve tarihi ile geri iade edilmesi gereken tarihi bu modül sayesinde kaydedeceğiz.
Bu modülümüzü çalıştırdığımızda bize şuan ki zamanı ve 2 hafta sonraki zamanı return etmesini istiyoruz.
"""
from datetime import datetime,timedelta
#Burada kendi zaman programimizi olusturuyoruz.
#Iki tarih return edilecek 1,Simdiki zaman(Kayit tarihi ve saati) 2,Kitap iki hafta sonra iade olacak tarih(yalnizca tarih yeterli)
#Ornek alinan tarih 20-09-2023, 10:38 iade tarihi 04-10-2023




def simdiki_zaman():
    return datetime.now().strftime("%Y-%m-%d")

def on_dort_gun_sonrasi():
    return (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")