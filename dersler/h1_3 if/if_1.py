print("║  1-Toplama          ║")
print("║  2-Çıkarma          ║")
print("║  3-Çarpma           ║")

s = input("Seçiniz nedir?")

if s == "1":
    print("TOPLAMA")
    s1 = int(input("1.sayıyı giriniz:"))
    s2 = int(input("2.sayıyı giriniz:"))
    print("Toplam:", s1+s2)

if s == "2":
    print("ÇIKARMA")
    s1 = int(input("1.sayıyı giriniz:"))
    s2 = int(input("2.sayıyı giriniz:"))
    print("fARK:", s1-s2)

if s == "3":
    print("ÇARPMA")
    s1 = int(input("1.sayıyı giriniz:"))
    s2 = int(input("2.sayıyı giriniz:"))
    print("Çarpım:", s1*s2)
