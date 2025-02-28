import modulx.adam_asmaca
import modulx.oyun_tetris
def oyunmenu():
    print("Oyunlar menusu")
    print("1-Tetris")
    print("2-Yılan")
    print("3-Adam asmaca")
    print("4-...")
    s = input("Hangi oyun? (numarasını gir) :")
    if s == "1": modulx.oyun_tetris.tetri_basla()
    if s == "3": modulx.adam_asmaca.adam_asmaca_oyna()
    # if s == "1": 
    # if s == "1":


    
