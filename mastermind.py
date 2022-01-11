import random


class Kolory:
    """
    Ma metode zwracającą słownik kolorów przyporządkowanych
    do cyft i metodę zwracającą liste kolorów.
    """
    def kolory_słownik():
        kolory_słownik = {
                        1: "czarny",
                        2: "biały",
                        3: "szary",
                        4: "różowy",
                        5: "żółty",
                        6: "niebieski",
                        7: "zielony",
                        8: "czerwony"
        }
        return kolory_słownik

    def kolory_lista():
        kolory_słownik = Kolory.kolory_słownik()
        kolory_lista = []
        for values in kolory_słownik.values():
            kolory_lista.append(values)
        return kolory_lista


class Zle_wpisany_kolor():
    def sprawdzanie_wpisanego_koloru(kolor):
        """
        Sprawdzenie, czy gracz wpisał kolory zgodnie z instrukcją
        """
        dobrze_wpisany_kolor = 0
        kolory_lista = Kolory.kolory_lista()
        for y in kolory_lista:
            if y == kolor:
                dobrze_wpisany_kolor = 1
                pass
        if dobrze_wpisany_kolor == 0:
            print(f'Wpisz kolor spośród {Kolory.kolory_lista()}')
            return False
        return True


class Gracz():
    def zgadywanie_kolorów():
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
            while not Zle_wpisany_kolor.sprawdzanie_wpisanego_koloru(kolor):
                kolor = input(f'Kolor{i}: ')
            ustawienie_kolorów.append(kolor)
        return ustawienie_kolorów

    def ustawienie_kod_gracz():
        """
        Metoda do ustawienia kodu kolorów przez gracza.
        Opiera się na funkcji z inputami zgadywanie_kolorów.
        Koloryu wpisane przy pomocy inputa i sprawdzane przy pomocy
        funkcji sprawdzanie_wpisanego_koloru.
        Testowana poprzez wyprintowanie.
        """
        ustawienie_kod_gracz = Gracz.zgadywanie_kolorów()
        return ustawienie_kod_gracz

    def sprawdzanie_poprawności_próby_zgadnięcia(ustawienie_kolorów, kod):
        # dkndm = dobry_kolor_na_dobrym_miejscu
        # dk = dobry_kolor
        pytaniedkndm = "Ile jest dobrych kolorów na dobrych miejscach?"
        pytaniedk = "Ile jest dobrych kolorów?"
        dkndm_komputer = Gracz_komputer.sprawdzanie_dobry_kolor_miejsce_komp(ustawienie_kolorów, kod)
        dk_komputer = Gracz_komputer.sprawdzanie_dobry_kolor_komp(ustawienie_kolorów, kod)
        dkndm = int(input(f'{pytaniedkndm}: '))
        dk = input((f'{pytaniedk}: '))
        while not dkndm == dkndm_komputer:
            print("Upewnij się jeszcze raz i wpisz wartość od 0 do 4")
            dkndm = int(input(f'{pytaniedkndm}: '))
        while not dk == dk_komputer:
            print("Upewnij się jeszcze raz i wpisz wartość od 0 do 4")
            dk = int(input(f'{pytaniedk}: '))


class Gracz_komputer():
    def ustawienie_kod_komputer():
        """
        Komputer losuje "kod" kolorów,
        który gracz ma odgadnąć,
        testowane poprzez wyprintowanie
        """
        numery = random.choices(range(1, 8), k=4)
        ustawienie_kod_komputer = []
        lista_kolorów = Kolory.kolory_lista()
        for y in numery:
            x = lista_kolorów[y]
            ustawienie_kod_komputer.append(x)
        return ustawienie_kod_komputer

    def zgadywanie_sekwencji_komputer_losowo():
        """
        Gracz komputerowy losuje kolory w celu odgadnięcia
        kodu kolorów ustalonego przez gracza.
        Testowane poprzez wyprintowanie.
        """
        ustawienie_kolorów_komputer = Gracz_komputer.ustawienie_kod_komputer()
        return ustawienie_kolorów_komputer

    def zgadywanie_sekwencji_komputer_taktyka():
        pass

    def sprawdzanie_dobry_kolor_miejsce_komp(ustawienie_kolorów, kod):
        for y in range(1, 5):
            # dkndm = dobry_kolor_na_dobrym_miejscu
            dkndm = 0
            if ustawienie_kolorów[y] == kod[y]:
                dkndm += 1
            return dkndm

    def sprawdzanie_dobry_kolor_komp(ustawienie_kolorów, kod):
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


kod = ["zielony", "niebieski", "biały", "żółty"]
ustawienie_kolorów = ["czarny", "różowy", "czerwony", "żółty"]
Gracz.sprawdzanie_poprawności_próby_zgadnięcia(ustawienie_kolorów, kod)
