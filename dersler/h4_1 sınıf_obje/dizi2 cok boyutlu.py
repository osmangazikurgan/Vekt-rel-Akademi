yemek_menusu1 = [ # iki boyutlu dizi
    ["tarhana","şeriye","mercimek"],
    ["musakka","mantı","karnı yarık"],
    ["Tulumba","Tiramisu","Lokma tatlısı"]
]

# print(yemek_menusu)
# print(yemek_menusu[2])
print(yemek_menusu1[2][1])
print(["ee","rr","tt"][1])

yemek_menusu = { # üç boyutlu dizi
    "corbalar":{"tarhana","şeriye","mercimek"},
    "yemekler":{"musakka","mantı","karnı yarık"},
    "tatlılar":{
        "Tulumba":{"fiyat":100,"içindekiler":["un","su"]},
        "Tiramisu":{},
        "Lokma tatlısı":{}}
}

print(yemek_menusu["tatlılar"])
print(yemek_menusu["tatlılar"]["Tulumba"])
print(yemek_menusu["tatlılar"]["Tulumba"]["fiyat"])
print(yemek_menusu["tatlılar"]["Tulumba"]["içindekiler"])
print(yemek_menusu["tatlılar"]["Tulumba"]["içindekiler"][0])

dizi=["elma","armut","kiraz","kavun"]
print (dizi)
dizi.sort() 
print (dizi)