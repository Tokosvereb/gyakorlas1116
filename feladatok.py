def elsofeladat():
    mondat=("Indul a kutya és a tyúk aludni")
    i = 0
    szamlalo = 0
    hossz = len(mondat)
    while i < hossz:
        if mondat[i] ==' ':
            szamlalo += 1
        i += 1
    print(f"A mondatban a szóközök száma:{szamlalo}")

def masodikfeladat():
    mondat = "Indul a kutya és a tyúk aludni"
    i = 0
    szkozok_nelkuli = ''
    while i < len(mondat):
        if mondat[i] != ' ':   #a felkialtojel az tagadas az egyenlosegre
            szkozok_nelkuli += mondat[i]
        i += 1

    print(f"Szóközök nélküli kiírás:{szkozok_nelkuli}")

def hrmadikofeladat():
    mondat = "InDuL a kUtYa ÉS a TyÚk AlUdNI"
    i = 0


