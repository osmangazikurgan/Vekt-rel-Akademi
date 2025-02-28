def hmmenu():
    """
       Hesap makinesi menüsü ...222
    """

    # Hesap makinesi menüsü ...

    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   Hesap Makinesi Menu  \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Topla            ║")
    print("║  2-Çarp             ║")
    print("║  3-...              ║")
    print("║  4-...              ║")
    print("║  5-üst alma         ║")
    print("║  6-Ana menu         ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    secim = input()
    s1 = int(input("1.Sayı nedir?"))
    s2 = int(input("2.Sayı nedir?"))
    if secim =="1": print(topla(s1,s2))
    if secim =="2": print(carp(s1,s2))

def topla(a,b):
    return a+b

def carp(a,b):
    return a*b

def ustal(x,y):
    return x**y



