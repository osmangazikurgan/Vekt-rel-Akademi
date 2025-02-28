# f, format ve %s
ad = "Erdinç DÖNMEZ"
not1 = 80
not2 = 90
print("Ad:",ad,", 1.Not:",not1)

print(f"Ad: {ad},  1.Not: {not1}")
print("Ad: {},  1.Not: {}".format(ad,not1)) # 
print("Ad: %s,  1.Not: %s" %(ad, not1)) #


print(f"1.not {not1}, 1.not {not2}")
print("ortalama: {}".format((not1+not2)/2))
print("100'den kalan %s" %(100-(not1+not2)/2))

# En az iki tanesini deneyin.
