not1 = 35

#Bu gruptakiler gibi olursa eksik çalışır.
# if not1>90 : print("süper")
# if not1>80 : print("Güzeeel")
# if not1>50 : print("geçti")
# else: print("Kaldın")

if not1>90 : print("süper")
if not1>80 and not1<=90 : print("Güzeeel")
if not1>=50 and not1<=80 : print("geçti")
if not1<=49: print("Kaldın")

# and ve or lu kullanım yerin bir çok yerde elif işe yarayabilir.
# if not1>90 : print("süper")
# elif not1>80 : print("Güzeeel")
# elif not1>50 : print("geçti")
# else: print("Kaldın")