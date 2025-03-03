import re 
metin1 = "Bügün hava çok soğuk"
metin2 = "Bursa çok sıcak"
metin3 = "bugün hava soğuk"
metin4 = "çok güzel bir hava var"


aranan = "çok"



print(re.search(aranan, metin4))

