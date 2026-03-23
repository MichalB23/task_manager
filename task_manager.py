ukoly = []

def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Vyberte možnost (1-4): ")
        
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Ukončuji program. Na shledanou!")
            break
        else:
            print("Neplatná volba! Zadejte číslo 1-4.")

def pridat_ukol():
    ukol = input("Zadejte název nového úkolu: ")
    ukoly.append(ukol)
    print(f"Úkol '{ukol}' byl přidán.")

def zobrazit_ukoly():
    if len(ukoly) == 0:
        print("Seznam úkolů je prázdný.")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol}")

def odstranit_ukol():
    zobrazit_ukoly()
    if len(ukoly) > 0:
        try:
            cislo = int(input("Zadejte číslo úkolu k odstranění: "))
            if 1 <= cislo <= len(ukoly):
                odstranen = ukoly.pop(cislo - 1)
                print(f"Úkol '{odstranen}' byl odstraněn.")
            else:
                print("Neplatné číslo úkolu!")
        except ValueError:
            print("Zadejte platné číslo!")

hlavni_menu()