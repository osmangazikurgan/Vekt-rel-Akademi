# sınıf = veri modeli (veri şekli/veri kalıbı)
class Ogrenci(): # Sınıf adları Pascal case olur, tekil olur.
    ad = "--"
    no = 00
    renk = "siyah"

ogrenci1 = Ogrenci # Sınıf referansını ogrenci1 e atadı
ogrenci2 = Ogrenci() # Ogrenci sınıfından yeni bir nesne oluşturdu
ogrenci3 = Ogrenci() # init parantezi 
print(type(ogrenci1))
print(type(ogrenci2))

ogrenci1.ad = "Kemal"
print(ogrenci1.ad)
print(ogrenci2.ad)
print(ogrenci3.renk)
# ogrenci2.ad = "Hasan"
# # print(ogrenci1.ad)
# # print(ogrenci2.ad)
# # print(ogrenci3.ad)
# ogrenci3.ad = "Deniz"
# print(ogrenci1.ad)
# print(ogrenci2.ad)
# print(ogrenci3.ad)
