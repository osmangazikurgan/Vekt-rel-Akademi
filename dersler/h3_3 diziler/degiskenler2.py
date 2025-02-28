a = 5 # global
def yaz():
    a=6 # local
    print(a)

yaz()
print(a)