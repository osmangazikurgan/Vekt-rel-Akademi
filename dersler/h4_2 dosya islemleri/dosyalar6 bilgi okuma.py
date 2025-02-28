def ekle():
    d = open("rehber.txt","a") # append/ekleme modunda açar
    print("╔═ REHBERE EKLEME ══════════")
    print("║ Ad giriniz \t: ",end=""); ad = input()
    print("║ Numara giriniz \t: ",end=""); no = input()

    d.write(f"{ad}|{no}\n")
    d.close() # close kullanılmaz ise dosya sorun çıkartabilir.

def oku():
    # d = open("rehber.txt","r") # açma modu parametresi default olarak r dir. (read)
    d = open("rehber.txt") # yukarıdaki ile aynı işi yapar.
    okunan = d.read()
    print(okunan)

oku()

