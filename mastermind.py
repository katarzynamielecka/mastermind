import random
from itertools import product


class Gra:
    def kolory_słownik():
        kolory_słownik = {
                        1: "czarny",
                        2: "biały",
                        3: "żółty",
                        4: "niebieski",
                        5: "zielony",
                        6: "czerwony"
        }
        return kolory_słownik

    def kolory_lista():
        kolory_słownik = Gra.kolory_słownik()
        kolory_lista = []
        for values in kolory_słownik.values():
            kolory_lista.append(values)
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

    def gracz_ustawienie_kolorów():
        """
        Gracz za pomocą inputów wpisuje 4 kolory.
        """
        ustawienie_kolorów = []
        for i in range(1, 5):
            kolor = input(f'Kolor{i}: ')
            while not Gra.sprawdzanie_wpisanego_koloru(kolor):
                kolor = input(f'Kolor{i}: ')
            ustawienie_kolorów.append(kolor)
        return ustawienie_kolorów

    def sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorów, kod):
        """
        Porównanie ustawienia_kolorów (kolorów i ich usytuowania)
        z kodem kolorów
        """
        # dkndm = dobry_kolor_na_dobrym_miejscu
        dkndm = 0
        for y in range(0, 4):
            if ustawienie_kolorów[y] == kod[y]:
                dkndm += 1
        return dkndm

    def sprawdzanie_dobry_kolor(ustawienie_kolorów, kod):
        """
        Porównanie kolorów wpisanych przez gracza
        z kolorami w kodzie, bez uwzględnienia usytuowania.
        """
        # dk = dobry_kolor
        kod_kopia = []
        for i in kod:
            kod_kopia.append(i)
        for z in ustawienie_kolorów:
            for x in kod_kopia:
                if z == x:
                    kod_kopia.remove(x)
                    break
        dk = 4 - len(kod_kopia)
        return dk

    def losowanie_czterech_kolorów():
        """
        Komputer losuje cztery kolory, może służyć
        jako ustawienie kolorów dla gracza komputerowego
        grającego losowo lub ustawianie kodu
        dla gracza komputerowego
        testowane poprzez wyprintowanie
        """
        numery = random.choices(range(0, 6), k=4)
        kolory = []
        lista_kolorów = Gra.kolory_lista()
        for y in numery:
            x = lista_kolorów[y]
            kolory.append(x)
        return kolory


class Gracz_ustawiający_kod:
    def ustawienie_kod_gracz():
        """
        Metoda do ustawiania kodu przez gracza
        poprzez inputy.
        Testowana poprzez wyprintowanie.
        """
        ustawienie_kod_gracz = Gra.gracz_ustawienie_kolorów()
        return ustawienie_kod_gracz

    def sprawdzanie_poprawności_próby_zgadnięcia(ustawienie_kolorów, kod):
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
        f = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorów, kod)
        dkndm_komputer = f
        dk_komputer = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorów, kod)
        dkndm = int(input(f'{pytaniedkndm}: '))
        dk = int(input(f'{pytaniedk}: '))
        while not dkndm == dkndm_komputer:
            print("Upewnij się jeszcze raz i wpisz wartość od 0 do 4")
            dkndm = int(input(f'{pytaniedkndm}: '))
        while not dk == dk_komputer:
            print("Upewnij się jeszcze raz i wpisz wartość od 0 do 4")
            dk = int(input(f'{pytaniedk}: '))


class Gracz_zgadujący_kod:
    def __init__(self):
        self.ustawienie_kolorów = self.zgadywanie_kolorów()

    def zgadywanie_kolorów(self):
        """
    Funkcja służy do odgadnięcia kodu
    użytkownik wpisuje kolory przy pomocy inputa,
    sprawdzenie przy pomocy funkcji
    sprwadzanie_wpisanego_koloru,
    testowana poprzez wyprintowanie
        """
        ustawienie_kolorów = []
        for i in range(1, 5):
            kolor = input(f'Kolor{i}: ')
            while not Gra.sprawdzanie_wpisanego_koloru(kolor):
                kolor = input(f'Kolor{i}: ')
            ustawienie_kolorów.append(kolor)
        return ustawienie_kolorów


class Gracz_komputer_ustawiający_kod:
    def ustawienie_kod_komputer():
        """
        Komputer losuje "kod" kolorów,
        który drugi gracz ma odgadnąć,
        testowane poprzez wyprintowanie
        """
        ustawienie_kod_komputer = Gra.losowanie_czterech_kolorów()
        return ustawienie_kod_komputer


class Gracz_komputer_zgadujący_kod_losowo:
    def __init__(self):
        self.ustawienie_kolorów = self.zgadywanie_kodu_komputer_losowo()

    def zgadywanie_kodu_komputer_losowo():
        """
        Gracz komputerowy losuje kolory w celu odgadnięcia
        kodu kolorów ustalonego przez gracza.
        Testowane poprzez wyprintowanie.
        """
        ustawienie_kolorów = Gra.losowanie_czterech_kolorów()
        return ustawienie_kolorów


class Gracz_komputer_zgadujący_kod_taktyka:
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

    def pierwsza_runda():
        ustawienie_kolorów = ["czarny", "czarny", "biały", "biały"]
        return ustawienie_kolorów

    def początek_runda_druga(dkndm, dk):
        kombinacje = Gracz_komputer_zgadujący_kod_taktyka.kombinacje()
        if dk == 0:
            for x in kombinacje:
                for y in x:
                    if y == 1:
                        kombinacje.remove(x)
                    if y == 2:
                        kombinacje.remove(x)
        if dk ==3:
            for x in kombinacje:
                czarne = 0
                biale = 0
                for y in x:
                    if y == 1:
                        czarne += 1
                    if y == 2:
                        biale += 1
                if biale + czarne != 3 or biale == 0 or czarne == 0:
                    kombinacje.remove(x)

        if dk == 4:
            for x in kombinacje:
                for y in x:
                    if y != 1 or y != 2:
                        kombinacje.remove(x)
        if dk == 1 or dk == 2:
            for x in kombinacje:
                sprawdzenie = 0
                for y in x:
                    if y != 1 or y != 2:
                        sprawdzenie += 1
                if sprawdzenie == 4:
                    kombinacje.remove(x)
        if dkndm == 0:
            for x in kombinacje:
                if x[0] == 1 or x[1] == 1 or x[2] == 2 or x[3] == 2:
                    kombinacje.remove(x)

