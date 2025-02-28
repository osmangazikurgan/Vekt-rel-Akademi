tatil_gunleri=("Cumartesi","Pazar")
siniflar = ["9A","10A","11A","11B","12A"]
ogrenci_bilgileri={ # dict key:value ikilisiyle çalışan JSON benzeri yapılardır.
    "ogrenci1" : {"ogrenci_adi" :"Remzi DURAN",
    "ogrenci_no" : "351"},
    "ogrenci2" : {"ogrenci_adi" :"Kemal KUTLU",
    "ogrenci_no" : "458"}
}

print(ogrenci_bilgileri)
# print(ogrenci_bilgileri[1]) # dictionary lerde index olmaz. onun yerine keyler olur.
print("XX1:",ogrenci_bilgileri["ogrenci2"])
print("XX2:",ogrenci_bilgileri["ogrenci2"]["ogrenci_adi"])
