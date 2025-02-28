def topla(a,b):
    return a+b

topla(3,5)
print(topla(7,4))
ee = topla(2,4)
print(ee)

ff = topla(7,topla(3,6))
# ff = topla(7,9)
# ff = 16
print(ff)

# def topla(a,b=0): # topla fonksiyonu bir parametre ile de çalışabilir.
# def topla(a=0,b=0): # print(topla()) şeklinde kullanım için..
# def topla(a=0,b): # şeklinde kullanılamaz. \
#   default değerli parametreler diğerlerinden önce olamaz.
print(topla())


