# VIT3_Python_Modul_Week_4
## Kutuphane Projesi
- Bu projede şu ana kadar öğrendiğiniz python bilgilerinizle beraber hata yakalama - dosya işlemleri  özellikle Json modulu ve dosya bilgisini kullanılarak bir kütüphane programı yazmanızı istiyoruz.
- Bir kutuphanede; Uyelik islemleri, Kitap islemleri  olmak uzere iki ana kısım vardır.
- Uyelik işlemleri içerisinde üye ekleme, üye silme, üye kontrolü, üyeye kitap verme, üyeden iade kitap alma bilgisi bulunmaktadır. Bir de üyelik verisinin kaydedildigi bir database veya dosya gerekmektedir. 
- Kitap işlemleri içinde benzer şeyleri söyleyebiliriz.

#### Projeyi detaylandıracak olursak:
 * main.py, kitap_işlemleri.py,üye_işlemleri.py, zaman.py  dosyalarindan oluşacak.
##### Main.py:
* Projemizi ana dosyası main.py dosyası olacak. işlemler bu dosyadan yürütülecek diğer Python dosyaları bir modül olarak bu bölümden çağrılacak . Örneğin kitap ekleme kitap silme ,üye ekleme , üyeye kitap verme ,üye kontrolü buradan yapılacak.
 ![resim](https://github.com/werhereitacademy/week_4/assets/141542413/fd0ea3eb-d5cc-4991-b67d-94ebf42ee8d9)

* Aşağıda bu projenin çalıştırılmış bir çıktısını göreceksiniz. Main sayfasında inputlar araciligiyla ile kitap_işlemleri ve üyelik_işlemleri modüllerindeki fonksiyonları çalıştırabilirsiniz.
  ![resim](https://github.com/werhereitacademy/week_4/assets/141542413/7708052f-5b9c-42ed-b4c0-1a6e92d5fbf6)
##### kitap_işlemleri.py :
* Bu modulde kitap bilgisi(kayitli kitaplar ve toplam adeti), ekleme,silme,arama,update fonksiyonlarini yazacaksiniz. Verilerimizi kitap.json dosyasina kaydedecegiz. Kitap.json dosyasi size hazir verilecek (dileyen kendide olusturabilir). Os Modulu ile dosya kontrolu mutlaka yapilmalidir. Aşağıda kitap işlemleri için fonksiyon örneklemeleri bulabilirsin fakat buna uymak zorunda değilsiniz, kendi planlamanızı da yapabilirsiniz.
 ![resim](https://github.com/werhereitacademy/week_4/assets/141542413/753abd94-38de-417e-afd8-0540ba8aa591)

* Kitap.json dosyasinda pekcok veri bulunmaktadir. Biz asagidaki veriler ile calisacagiz. Yeni veri eklerken veya arama yaparken bunlari baz alacagiz.
  
 ![resim](https://github.com/werhereitacademy/week_4/assets/141542413/ff5f0b47-5244-4b58-b8ae-7c5dff092a73)
 
##### Kitap.json : 
örnek çıktı aşağıdaki gibidir
![resim](https://github.com/werhereitacademy/week_4/assets/141542413/caaecfd5-db10-4bc7-985b-0f1a4fb208d4)
##### Uyelik_islemleri.py:
* Burada üye bilgisi(üye isimler ve toplam üye sayisi) ,üye güncelleme, üye ekleme, üye arama, üye silme, kitap ödünç verme ve kitap iade etme gibi işlemler yapılacaktır. Ayrıca üyeler uye.Json dosyasına kaydedilmelidir. Kitap ödünç verme işlemi yapılırken mutlak suretle 
* - kitabin ödünç verildigi tarih ve saat ve 2 hafta sonra iade edecek şekilde tarih bilgisi eklenmelidir ve bu bilgiler takip.json dosyasına kaydedilmelidir.
    
![resim](https://github.com/werhereitacademy/week_4/assets/141542413/6728d7fa-2aa2-49a8-b843-cccd9a397311)

* bu işlemi kendi oluşturduğumuz zaman py modulunden  yapacağız.
* - takip.json dosyasına kaydedildikten sonra ödünç verilen kitap Kitap.json dan silinmelidir ki bir başkasi almak istedigi zaman gozukmesin.
#####  Not:uye.json ve takip.json dosyasını kendiniz oluşturacaksınız.
![resim](https://github.com/werhereitacademy/week_4/assets/141542413/49f04d87-bece-4493-b62f-022cfa3d9201)
* Uye.json a kaydedeceğiniz veriler aşağıdaki gibi olmalıdır :
 ![resim](https://github.com/werhereitacademy/week_4/assets/141542413/8761111e-11f6-47ba-9605-cc8b33be84b3)
##### zaman.py :
* üyelerimize kitabımızı 2 haftalık süreyle ödünç vermekteyiz.Bu yüzden ödünç verdiğimiz andaki saat ve tarihi ile geri iade edilmesi gereken tarihi bu modül sayesinde kaydedeceğiz.
Bu modülümüzü çalıştırdığımızda bize şuan ki zamanı ve 2 hafta sonraki zamanı return etmesini istiyoruz.
![resim](https://github.com/werhereitacademy/week_4/assets/141542413/7a7c7274-32ef-42e9-b3c7-9d2094752893)
##### Takip.json a kaydedeceğiniz veriler aşağıdaki gibi olmalıdır :

![resim](https://github.com/werhereitacademy/week_4/assets/141542413/3948f87d-bf87-49a6-a9d6-75bcdf155afd)

## Hackerrank Questions 

1. Diagonal Difference: https://www.hackerrank.com/challenges/diagonal-difference/problem

2. Left Rotation: https://www.hackerrank.com/challenges/array-left-rotation/problem

3. Counter game: https://www.hackerrank.com/challenges/counter-game/problem

4. Time Delta: https://www.hackerrank.com/challenges/python-time-delta/problem
