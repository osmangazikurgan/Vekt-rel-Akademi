# sınıf = veri modeli (veri şekli/veri kalıbı)
class OgrenciKalibi(): # Sınıf adları Pascal case olur, tekil olur.
    ad = "--"
    no = 00
    renk = "siyah"
    
    def __init__(aa,x="",y=0):
        aa.ad = x
        aa.no = y

    def bilgi_yaz(qq,tekrar):
        for a in range(tekrar):
            print(qq.ad, qq.no)

ogrenci1 = OgrenciKalibi("Osman",44) # () ile init yapılır 
# ogrenci2 = OgrenciKalibi() 
# ogrenci2.ad = "Deniz"
# ogrenci2.no = 77

ogrenci3 = OgrenciKalibi("Zeynep",55)

print(ogrenci1.ad, ogrenci1.no)
print(ogrenci3.ad, ogrenci3.no)

print(ogrenci3.bilgi_yaz(10))

ogrenci5 = OgrenciKalibi()
print(ogrenci5.bilgi_yaz(10))


