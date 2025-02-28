import random as rnd

print(rnd.random()) # random fonksiyonu 0 ile 1 arası sayı verir
print(rnd.randint(50,100)) # bir aralıktan tam sayı verir

oyunSecenekleri = ["taş","kağıt","makas"]
print(rnd.choice(oyunSecenekleri))

print(dir(rnd))
help(rnd.shuffle)