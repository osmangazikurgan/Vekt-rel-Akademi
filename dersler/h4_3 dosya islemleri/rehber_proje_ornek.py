def ekle():
    d = open("rehber.txt","a",encoding="utf8") # append/ekleme modunda açar
    print("╔═ REHBERE EKLEME ══════════")
    print("║ Ad giriniz \t: ",end=""); ad = input()
    print("║ Numara giriniz \t: ",end=""); no = input()

    d.write(f"{ad}|{no}\n")
    d.close() # close kullanılmaz ise dosya sorun çıkartabilir.

def oku():
    # d = open("rehber.txt","r") # açma modu parametresi default olarak r dir. (read)
    d = open("rehber.txt") # yukarıdaki ile aynı işi yapar.
    okunan = d.read() # dosya içindeki tüm verileri okur
    print(okunan)
def oku1():
    d = open("rehber.txt") # yukarıdaki ile aynı işi yapar.
    okunan = d.readline() # dosya içindeki bir satırı okur
    print(okunan)

def anamenu():
    print("╔═ REHBERE UYGULAMASI ══════════")
    print("║ 1-Rehbere ekle")
    print("║ 2-Bilgileri listele ")
    print("║ 3-... ")
    print("║ 4-... ")
    print("║ Seçiminiz nedir? ")
    secim = input()
    if secim == "1" : ekle()
    if secim == "2" : oku1()
    if secim == "1" : ekle()

anamenu()

