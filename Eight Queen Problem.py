import numpy as np
import random as rd

satranç_tahtası = np.arange(1, 65).reshape(8, 8)

def veziri_yerleştir(vezirin_konumu):
    yasaklı_karelere_ekle(vezirin_konumu)

def yasaklı_karelere_ekle(vezirin_konumu):
    konumy = np.where(satranç_tahtası == vezirin_konumu)[1][0]
    for çapraz_sol in range(vezirin_konumu - (konumy * 9), vezirin_konumu + 1 + ((7-konumy)*9), 9):
        if 65 > çapraz_sol > 0:
            yasaklı_kareler.add(çapraz_sol)
    for çapraz_sağ in range(vezirin_konumu - ((7-konumy) * 7), vezirin_konumu + 1 + (konumy*7), 7):
        if 65 > çapraz_sağ > 0:
            yasaklı_kareler.add(çapraz_sağ)

    for yatay in satranç_tahtası:
        if vezirin_konumu in yatay:
            for yataydaki_kare in yatay:
                yasaklı_kareler.add(yataydaki_kare)
            
            for dikeydeki_kareler in range(len(satranç_tahtası)):
                yasaklı_kareler.add(satranç_tahtası[dikeydeki_kareler, konumy])

def satranç_kordinatına_dönüştür(array1, array2):
    son_hal = []
    dikeyler = "habcdefg"
    for yatay, dikey in zip(array1, array2):
        son_hal.append(f"{dikeyler[(dikey % 8)]}{8 - yatay}")
    
    print("{} kere deneme yapıldı".format(deneme_sayısı + 1))
    print(satranç_tahtası)
    print(vezirlerin_konumu)
    
    return son_hal

çaprazlar = set()
vezirlerin_konumu = []
yataylar = []
yasaklı_kareler = set()

deneme_sayısı = 0
koyulacak_vezir_sayısı = 8

seçim_aralığı = list(range(1, 65))

while koyulacak_vezir_sayısı > 0:
    random_pos = rd.choice(seçim_aralığı)
    if len(yasaklı_kareler) != 64:
        if random_pos not in yasaklı_kareler:
            yataylar.append(np.where(satranç_tahtası == random_pos)[0][0])
            veziri_yerleştir(random_pos)
            vezirlerin_konumu.append(random_pos)
            
            koyulacak_vezir_sayısı -= 1
            seçim_aralığı.remove(random_pos)
            print("Vezir Yerleştirildi!")
    else:    
        print("Başa Dönülüyor...")
        print("Yerleştirilebilen vezir sayısı : {}".format(8 - koyulacak_vezir_sayısı))
        vezirlerin_konumu.clear()
        yasaklı_kareler.clear()
        yataylar.clear()
        koyulacak_vezir_sayısı = 8
        deneme_sayısı += 1
        seçim_aralığı = list(range(1, 65))


print(satranç_kordinatına_dönüştür(yataylar, vezirlerin_konumu))