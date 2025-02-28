d = open("rehber.txt","a") # append/ekleme modunda açar
print("╔═ REHBERE EKLEME ══════════")
print("║ Ad giriniz \t: ",end=""); ad = input()
print("║ Numara giriniz \t: ",end=""); no = input()

d.write(f"{ad}|{no}\n")
d.close() # close kullanılmaz ise dosya sorun çıkartabilir.

