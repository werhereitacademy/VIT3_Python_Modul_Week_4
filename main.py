from kitap_islemleri import *
from uye_islemleri import *
import json
from zaman import *
from datetime import datetime,timedelta
import os


while True:
    secim = input(
        "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~≀" +
        "\n≀                                                                                ≀"+
        "\n≀   Uyelik islmeleri icin 1'e basin                                              ≀" +
        "\n≀   Kitap islemleri 2'ye basin                                                   ≀" +
        "\n≀   Cikis icin 0'e basin                                                         ≀" +
        "\n≀                                                                                ≀" +
        "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~≀")

    if secim == "1":
        secim1 = input(
            "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~  ≀" +
            "\n≀                                                                          ≀" +
            "\n≀   Uyeler icin 1'e basin           Kitap Odunc almak icin 5`e basin       ≀" +
            "\n≀   Uye eklemek icin 2'ye basin     Kitap Iade vermek icin 6`ya basin      ≀" +
            "\n≀   Uye aramak icin 3`e basin       Kitap Takibi icin 7`ye basin           ≀" +
            "\n≀   Uye silmek icin 4`e basin       Cikis yapmak icin 0`a basin            ≀" +
            "\n≀                                                                          ≀" +
            "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ≀")
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
            "\n≀   Cikis yapmak icin 0`a basin                                            ≀" +
            "\n≀                                                                          ≀" +
            "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ≀")

        if secim2 == "1":
            kitaplar()
        elif secim2 == "2":
            kitap_ekle()
        elif secim2 == "3":
            kitap_ara()
        elif secim == "0":
            continue
    elif secim == "0":
        break
