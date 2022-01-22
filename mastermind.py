import random


class Gra:
    def kolory_słownik():
        kolory_słownik = {
                        "czarny": 1,
                        "biały": 2,
                        "żółty": 3,
                        "niebieski": 4,
                        "zielony": 5,
                        "czerwony": 6
        }
        return kolory_słownik

    def kolory_lista():
        kolory_słownik = Gra.kolory_słownik()
        kolory_lista = []
        for keys in kolory_słownik.keys():
            kolory_lista.append(keys)
        return kolory_lista

    def sprawdzanie_wpisanego_koloru(kolor):
        """
        Sprawdzenie, czy gracz wpisał kolory zgodnie z instrukcją
        """
        dobrze_wpisany_kolor = 0
        kolory_lista = Gra.kolory_lista()
        for y in kolory_lista:
            if y == kolor:
                dobrze_wpisany_kolor = 1
                pass
        if dobrze_wpisany_kolor == 0:
            print(f'Wpisz kolor spośród {Gra.kolory_lista()}')
            return False
        return True

    def gracz_ustawienie_kolorow():
        """
        Gracz za pomocą inputów wpisuje 4 kolory.
        """
        ustawienie_kolorow = []
        for i in range(1, 5):
            kolor = input(f'Kolor{i}: ')
            while not Gra.sprawdzanie_wpisanego_koloru(kolor):
                kolor = input(f'Kolor{i}: ')
            ustawienie_kolorow.append(kolor)
        return ustawienie_kolorow

    def sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod):
        """
        Porównanie ustawienia_kolorów (kolorów i ich usytuowania)
        z kodem kolorów
        """
        # dkndm = dobry_kolor_na_dobrym_miejscu
        dkndm = 0
        for y in range(0, 4):
            if ustawienie_kolorow[y] == kod[y]:
                dkndm += 1
        return dkndm

    def sprawdzanie_dobry_kolor(ustawienie_kolorow, kod):
        """
        Porównanie kolorów wpisanych przez gracza
        z kolorami w kodzie, bez uwzględnienia usytuowania.
        """
        # dk = dobry_kolor
        kod_kopia = []
        for i in kod:
            kod_kopia.append(i)
        for z in ustawienie_kolorow:
            for x in kod_kopia:
                if z == x:
                    kod_kopia.remove(x)
                    break
        dk = 4 - len(kod_kopia)
        return dk

    def losowanie_czterech_kolorow():
        """
        Komputer losuje cztery kolory, może służyć
        jako ustawienie kolorów dla gracza komputerowego
        grającego losowo lub ustawianie kodu
        dla gracza komputerowego
        testowane poprzez wyprintowanie
        """
        numery = random.choices(range(0, 6), k=4)
        kolory = []
        lista_kolorow = Gra.kolory_lista()
        for y in numery:
            x = lista_kolorow[y]
            kolory.append(x)
        return kolory


class Gracz_ustawiajacy_kod:
    def ustawienie_kod_gracz():
        """
        Metoda do ustawiania kodu przez gracza
        poprzez inputy.
        Testowana poprzez wyprintowanie.
        """
        ustawienie_kod_gracz = Gra.gracz_ustawienie_kolorow()
        return ustawienie_kod_gracz

    def sprawdzanie_proby_zgadniecia(ustawienie_kolorow, kod):
        """
        Gracz sprawdza próby drugiego gracza
        lub komputera i wpisuje wynik poprzez inputa
        Jest sprawdzany przy pomocy funkcji
        sprawdzanie_dobry_kolor_miejsce i sprawdzanie_dobry_kolor.
        """
        # dkndm = dobry_kolor_na_dobrym_miejscu
        # dk = dobry_kolor
        pytaniedkndm = "Ile jest dobrych kolorów na dobrych miejscach?"
        pytaniedk = "Ile jest dobrych kolorów?"
        f = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
        dkndm_komputer = f
        dk_komputer = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorow, kod)
        dkndm = int(input(f'{pytaniedkndm}: '))
        dk = int(input(f'{pytaniedk}: '))
        while not dkndm == dkndm_komputer:
            print("Upewnij się jeszcze raz i wpisz wartość od 0 do 4")
            dkndm = int(input(f'{pytaniedkndm}: '))
        while not dk == dk_komputer:
            print("Upewnij się jeszcze raz i wpisz wartość od 0 do 4")
            dk = int(input(f'{pytaniedk}: '))


class Gracz_zgadujacy_kod:
    def zgadywanie_kolorow():
        """
    Funkcja służy do odgadnięcia kodu
    użytkownik wpisuje kolory przy pomocy inputa,
    sprawdzenie przy pomocy funkcji
    sprwadzanie_wpisanego_koloru,
    testowana poprzez wyprintowanie
        """
        ustawienie_kolorow = []
        for i in range(1, 5):
            kolor = input(f'Kolor{i}: ')
            while not Gra.sprawdzanie_wpisanego_koloru(kolor):
                kolor = input(f'Kolor{i}: ')
            ustawienie_kolorow.append(kolor)
        return ustawienie_kolorow


class Gracz_komputer_ustawiajacy_kod:
    def ustawienie_kod_komputer():
        """
        Komputer losuje "kod" kolorów,
        który drugi gracz ma odgadnąć,
        testowane poprzez wyprintowanie
        """
        ustawienie_kod_komputer = Gra.losowanie_czterech_kolorow()
        return ustawienie_kod_komputer


class Gracz_komputer_zgadujacy_kod_losowo:
    def __init__(self):
        self.ustawienie_kolorow = self.zgadywanie_kodu_komputer_losowo()

    def zgadywanie_kodu_komputer_losowo():
        """
        Gracz komputerowy losuje kolory w celu odgadnięcia
        kodu kolorów ustalonego przez gracza.
        Testowane poprzez wyprintowanie.
        """
        ustawienie_kolorow = Gra.losowanie_czterech_kolorow()
        return ustawienie_kolorow


class Gracz_komputer_zgadujacy_kod_taktyka:
    def kombinacje():
        """
        1 - czarny
        2 - biały
        3 - żółty
        4 - niebieski
        5 - zielony
        6 - czerwony
        """
        kombinacje = []
        for a in range(1, 7):
            for b in range(1, 7):
                for c in range(1, 7):
                    for d in range(1, 7):
                        kombinacje.append([a, b, c, d])
        return kombinacje

    def zgadywanie_kodu(kombinacje):
        ustawienie_kolorów = random.choice(kombinacje)
        return ustawienie_kolorów

    def zamienienie_kolorow_na_cyfry(ustawienie_kolorow):
        ustawienie_kolorow_cyfry = []
        kolory_cyfry = Gra.kolory_słownik()
        for y in ustawienie_kolorow:
            ustawienie_kolorow_cyfry.append(kolory_cyfry[f'{y}'])
        return ustawienie_kolorow_cyfry

    def usuwanie_kombinacji(ustawienie_kolorow_cyfry, kombinacje, dkndm, dk):
        if dk == 0:
            for x in kombinacje:
                if Gra.sprawdzanie_dobry_kolor(x, ustawienie_kolorow_cyfry) != 0:
                    kombinacje.remove(x)
        elif dk == 1:
            for x in kombinacje:
                if Gra.sprawdzanie_dobry_kolor(x, ustawienie_kolorow_cyfry) != 1:
                    kombinacje.remove(x)
        elif dk == 2:
            for x in kombinacje:
                if Gra.sprawdzanie_dobry_kolor(x, ustawienie_kolorow_cyfry) != 2:
                    kombinacje.remove(x)
        elif dk == 3:
            for x in kombinacje:
                if Gra.sprawdzanie_dobry_kolor(x, ustawienie_kolorow_cyfry) != 3:
                    kombinacje.remove(x)
        elif dk == 4:
            for x in kombinacje:
                if Gra.sprawdzanie_dobry_kolor(x, ustawienie_kolorow_cyfry) != 4:
                    kombinacje.remove(x)
        if dkndm == 0:
            for x in kombinacje:
                if Gra.sprawdzanie_dobry_kolor_miejsce(x, ustawienie_kolorow_cyfry) != 0:
                    kombinacje.remove(x)
        elif dkndm == 1:
            for x in kombinacje:
                if Gra.sprawdzanie_dobry_kolor_miejsce(x, ustawienie_kolorow_cyfry) != 1:
                    kombinacje.remove(x)
        elif dkndm == 2:
            for x in kombinacje:
                if Gra.sprawdzanie_dobry_kolor_miejsce(x, ustawienie_kolorow_cyfry) != 2:
                    kombinacje.remove(x)
        elif dkndm == 3:
            for x in kombinacje:
                if Gra.sprawdzanie_dobry_kolor_miejsce(x, ustawienie_kolorow_cyfry) != 3:
                    kombinacje.remove(x)
        return kombinacje
