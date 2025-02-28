# sınıf = veri modeli (veri şekli/veri kalıbı)
class OgrenciKalibi(): # Sınıf adları Pascal case olur, tekil olur.
    ad = "--"
    no = 00
    renk = "siyah"

ogrenci1 = OgrenciKalibi # () ile init yapılır 
ogrenci1.ad = "Yağız"
ogrenci1.no = 88

ogrenci2 = OgrenciKalibi() 
ogrenci2.ad = "Deniz"
ogrenci2.no = 77

ogrenci3 = OgrenciKalibi()

print(ogrenci1.ad, ogrenci1.no)
print(ogrenci3.ad, ogrenci3.no)


