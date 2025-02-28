print("   NOT HESAPALAMA PROGRAMI")
print("=============================\n")

ad = input("Adınızı girin\t :")
n1 = int(input(f"Sayın {ad}, 1.Yazılı notun nedir\t :"))
n2 = int(input(f"Sayın {ad}, 2.Yazılı notun nedir\t :"))

ortalama = (n1+n2)//2

if n1>100 or n2>100 or n1<0 or n2<0: 
    print("Geçersiz not girişi.")
    print("Lütfen tekrar deneyiniz..")

else:
    if ortalama>90 : print(f"süper. ortalaman:{ortalama}")
    elif ortalama>80 : print(f"Güzeeel not ortalaman {ortalama}")
    elif ortalama>50 : print(f"{ortalama} ortalama ile geçtin")
    else: print(f"Malesef {ortalama} ortalama ile kaldın.")

