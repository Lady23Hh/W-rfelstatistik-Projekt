import random

def würfeln_und_speichern(würfe, anzahl):
    for _ in range(anzahl):
        wurf = random.randint(1, 6)
        würfe.append(wurf)
    print(f"{anzahl} Würfe: {würfe}")

def statistik(würfe):
    zähler = [0] * 6
    for wurf in würfe:
        zähler[wurf-1] += 1
    print("\nStatistik:")
    for i in range(6):
        print(f"{i+1}: {zähler[i]} Mal ({zähler[i]/len(würfe)*100:.1f}%)")
    if len(würfe) > 0:
        print(f"Durchschnitt: {sum(würfe)/len(würfe):.1f}")

def würfel_statistik():
    würfe = []
    while True:
        print("\n1: Würfeln, 2: Statistik anzeigen, 3: Beenden")
        wahl = int(input("Wähle eine Option (1-3): "))
        if wahl == 1:
            anzahl = int(input("Wie oft würfeln? "))
            würfeln_und_speichern(würfe, anzahl)
        elif wahl == 2:
            statistik(würfe)
        elif wahl == 3:
            print("Tschüss!")
            break
        else:
            print("Ungültige Wahl, bitte 1-3 wälen!")

würfel_statistik()