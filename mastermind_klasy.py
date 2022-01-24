# Katarzyna Mielęcka - projekt
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

    def dobry_kolor_miejsce(ustawienie_kolorow, kod):
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

    def dobry_kolor(ustawienie_kolorow, kod):
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
        dla gracza komputerowego.
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
        """
        kod = Gra.gracz_ustawienie_kolorow()
        return kod

    def dobry_kolor(ustawienie_kolorow, kod):
        """
        Metoda do sprawdzenia kolorow wpisanych przez gracza
        podczas próby zgadnięcia kodu z kolorami w kodzie.
        Sprawdzenia dokonuje gracz, który ustawiał kod, jednak
        jest sprawdzany przez komputer, aby nie oszukiwał.
        """
        # dk = dobry_kolor
        mozliwosci = [0, 1, 2, 3, 4]
        pytaniedk = "Ile jest dobrych kolorów?"
        dk_komputer = Gra.dobry_kolor(ustawienie_kolorow, kod)
        n = 0
        k = 0
        while n != 2:
            n = 0
            if k != 0:
                print("Upewnij się jeszcze raz i wpisz wartość od 0 do 4")
            k = 1
            dk_input = input(f'{pytaniedk}: ')
            for y in mozliwosci:
                if dk_input == str(y):
                    n += 1
            if dk_input == str(dk_komputer):
                n += 1
        dk = int(dk_input)
        return dk

    def dobry_kolor_miejsce(ustawienie_kolorow, kod):
        """
        Metoda do sprawdzenia usytuowania kolorow wpisanych przez gracza
        podczas próby zgadnięcia kodu z usytuowaniem kolorow w kodzie.
        Sprawdzenia dokonuje gracz, który ustawiał kod, jednak
        jest sprawdzany przez komputer, aby nie oszukiwał.
        """
        # dkndm = dobry_kolor_na_dobrym_miejscu
        mozliwosci = [0, 1, 2, 3, 4]
        pytaniedkndm = "Ile jest dobrych kolorów na dobrych miejscach?"
        f = Gra.dobry_kolor_miejsce(ustawienie_kolorow, kod)
        dkndm_komputer = f
        n = 0
        k = 0
        while n != 2:
            n = 0
            if k != 0:
                print("Upewnij się jeszcze raz i wpisz wartość od 0 do 4")
            k = 1
            dkndm_input = input(f'{pytaniedkndm}: ')
            for y in mozliwosci:
                if dkndm_input == str(y):
                    n += 1
            if dkndm_input == str(dkndm_komputer):
                n += 1
        dkndm = int(dkndm_input)
        return dkndm


class Gracz_zgadujacy_kod:
    def zgadywanie_kolorow():
        """
    Funkcja służy do odgadnięcia kodu
    użytkownik wpisuje kolory przy pomocy inputa,
    sprawdzenie przy pomocy funkcji
    sprwadzanie_wpisanego_koloru.
        """
        ustawienie_kolorow = []
        for i in range(1, 5):
            kolor = input(f'Kolor{i}: ')
            while not Gra.sprawdzanie_wpisanego_koloru(kolor):
                kolor = input(f'Kolor{i}: ')
            ustawienie_kolorow.append(kolor)
        return ustawienie_kolorow


class Komputer_ustawiajacy_kod:
    def ustawienie_kod_komputer():
        """
        Komputer losuje "kod" kolorów,
        który drugi gracz ma odgadnąć.
        """
        kod = Gra.losowanie_czterech_kolorow()
        return kod

    def sprawdzanie_zgadniecia(ustawienie_kolorow, kod):
        dk = Gra.dobry_kolor(ustawienie_kolorow, kod)
        print(f'Dobry kolor: {dk}')
        dkndm = Gra.dobry_kolor_miejsce(ustawienie_kolorow, kod)
        print(f'Dobry kolor na dobrym miejscu: {dkndm}')


class Komputer_losowy:
    def zgadywanie_kodu():
        """
        Gracz komputerowy losuje kolory w celu odgadnięcia
        kodu kolorów ustalonego przez gracza.
        """
        ustawienie_kolorow = Gra.losowanie_czterech_kolorow()
        return ustawienie_kolorow


class Komputer_taktyczny:
    """
    Gracz komputer zgadujący opiera się na liście kombinacji
    wszystkich kolorów. Po próbie zgadnięcia komputera i odpowiedzi
    drugiego gracza z listy kombinacji usuwane są ustawienia kolorów,
    które na pewno nie są kodem. Każda następną próbę zgadnięcia komputer
    wykonuje losując z listy kombinacji ustawienie.
    """
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
        ustawienie_cyfr = random.choice(kombinacje)
        ustawienie_kolorow = []
        kolory = Gra.kolory_lista()
        for y in ustawienie_cyfr:
            ustawienie_kolorow.append(kolory[y-1])
        return ustawienie_kolorow

    def ustawienie_cyfry(ustawienie_kolorow):
        ustawienie_cyfr = []
        kolory_cyfry = Gra.kolory_słownik()
        for y in ustawienie_kolorow:
            ustawienie_cyfr.append(kolory_cyfry[f'{y}'])
        return ustawienie_cyfr

    def usuwanie_kombinacji(ustawienie_cyfr, kombinacje, dkndm, dk):
        """
        Usuwanie kolorów z listy kombinacji jest uskuteczniane przy pomocy
        funkcji sprawdzenie_dobry_kolor i sprawdzenie_dobry_kolor_miejsce.
        Metody te porównują kolory z listy kombinacji i z poprzedniego
        ustawienia kolorów zaproponowanego przez komputer.
        """
        if dk == 0:
            for x in kombinacje:
                if Gra.dobry_kolor(x, ustawienie_cyfr) != 0:
                    kombinacje.remove(x)
        elif dk == 1:
            for x in kombinacje:
                if Gra.dobry_kolor(x, ustawienie_cyfr) != 1:
                    kombinacje.remove(x)
        elif dk == 2:
            for x in kombinacje:
                if Gra.dobry_kolor(x, ustawienie_cyfr) != 2:
                    kombinacje.remove(x)
        elif dk == 3:
            for x in kombinacje:
                if Gra.dobry_kolor(x, ustawienie_cyfr) != 3:
                    kombinacje.remove(x)
        elif dk == 4:
            for x in kombinacje:
                if Gra.dobry_kolor(x, ustawienie_cyfr) != 4:
                    kombinacje.remove(x)
        if dkndm == 0:
            for x in kombinacje:
                if Gra.dobry_kolor_miejsce(x, ustawienie_cyfr) != 0:
                    kombinacje.remove(x)
        elif dkndm == 1:
            for x in kombinacje:
                if Gra.dobry_kolor_miejsce(x, ustawienie_cyfr) != 1:
                    kombinacje.remove(x)
        elif dkndm == 2:
            for x in kombinacje:
                if Gra.dobry_kolor_miejsce(x, ustawienie_cyfr) != 2:
                    kombinacje.remove(x)
        elif dkndm == 3:
            for x in kombinacje:
                if Gra.dobry_kolor_miejsce(x, ustawienie_cyfr) != 3:
                    kombinacje.remove(x)
        return kombinacje
