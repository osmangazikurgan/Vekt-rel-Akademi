# def topla(): # basit fonksiyon
#     print("Toplam:", 5+6)

# topla()

# def topla(aa,bb): # parametre alan fonksiyon
#     print("Toplam:", aa+bb)

# topla(5,6)
# topla(3,5)
# # topla(topla(1,2),4) # bu şekilde kullanabilmek için değer döndüren fonksiyon olması gerek. (sonraki örnekte yapılacak)

def topla(aa,bb):
    return f"Toplam: {aa+bb}"

# print(topla(4,topla(2,3))) # olmaz.
print(topla(4,8))

def carp(xx,yy):
    return xx*yy

print(carp(2,4))
print(carp(2,carp(2,4)))


