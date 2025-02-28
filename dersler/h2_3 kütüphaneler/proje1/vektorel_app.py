import moduller.oyunlar
import moduller.hesammakinesi
# import moduller.hesammakinesi as hm
from moduller.hesammakinesi import hmmenu
# from moduller.hesammakinesi import * # tüm fonksiyonlar.
import oyunlarklasoru.yilan_oyunu

def anamenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   VEKTOREL APP    \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Oyunlar          ║")
    print("║  2-Hesp mak.        ║")
    print("║  3-                 ║")
    print("║  4-                 ║")
    print("║  9-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    if secim == "1" : moduller.oyunlar.oyunmenu()
    # if secim == "2" : moduller.hesammakinesi.hmmenu() # import moduller.hesammakinesi şeklinde kullanım için idi.
    # if secim == "2" : moduller.hesammakinesi.hmmenu() # import moduller.hesammakinesi şeklinde kullanım için idi.
    if secim == "2" : hmmenu()
    if secim == "9" : exit()
    else : anamenu()

# print(dir(moduller.oyunlar)) 
print(dir(moduller.hesammakinesi)) # modüllerin içindeki fonksiyonlar.
help(moduller.hesammakinesi.hmmenu)
anamenu()