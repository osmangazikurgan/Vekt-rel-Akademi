# open("rehber.txt").write("Merhaba") # dosya açma parametresi olmadığında, okuma modunda açar
# open("rehber.txt","w").write("Merhaba") # w modu önceki verilerin silinmesine neden olur.
# open("rehber.txt","w").write("Nasılsın")

dosya = open("rehber.txt","w")
dosya.write("Merhaba")
dosya.write("Nasılsın")