class Ilan():
    ilan_no = "---"
    ilan_adi = "---"
    ilan_aciklamasi = "Açıklama girilmedi"
    def __init__(self,a,b,c):
        self.ilan_no = a
        self.ilan_adi = b
        self.ilan_aciklamasi = c
    
    def ilan_bilgileri(self, uyelik_tipi):
        if uyelik_tipi == "premium" : 
            print ("Merhaba çok değerli üyemiz.")
            print (f"İlan adı:{self.ilan_adi}, \nİlan no:{self.ilan_no}\
                   , \nİlan açıklaması:{self.ilan_aciklamasi}")
        
        if uyelik_tipi == "basic" : 
            print ("Merhaba değerli üyemiz.")
            print (f"İlan adı:{self.ilan_adi}, \nİlan no:{self.ilan_no}\
                   , \nİlan açıklaması:{self.ilan_aciklamasi}")

ilan_2341 = Ilan("257","On numara şahin","Temiz, 210binde,...")         
ilan_5784 = Ilan("874","Kİralık ev","3+1 metroya yakın, kombili,...")         

ilan_2341.ilan_bilgileri("premium")
ilan_2341.ilan_bilgileri("basic")
ilan_5784.ilan_bilgileri("premium")
    
