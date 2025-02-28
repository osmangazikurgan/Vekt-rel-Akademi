import oyunlar
import hesapmakinesi
import modulx.xxx
def anamenu():
    print("Proje ana menusu")
    print("1-Oyunlar")
    print("2-Hesap makinesi")
    print("3-xxx")
    print("...")
    secim = input("Seçiminiz")
    if secim == "1" : oyunlar.oyunmenu()
    if secim == "2" : hesapmakinesi.hmmenu()
    if secim == "3" : modulx.xxx.xxxinmenusu()
    anamenu()

anamenu()