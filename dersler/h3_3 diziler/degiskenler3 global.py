a = 5 # global
def yaz():
    global a
    a=6 # local değil
    print(a)

yaz()
print(a)
