import random


def zgadywanie_kolorów():
    """
    użytkownik wpisuje kolory przy pomocy inputa
     """
    ustawienie_kolorów = []
    for i in range(1, 5):
        ustawienie_kolorów.append(input(f"kolor{i}: "))
    return ustawienie_kolorów


def wybór_kolorów():
    '''komputer wybiera swój kod kolorów'''
    kolory_słownik = {
                1: "black",
                2: "white",
                3: "grey",
                4: "pink",
                5: "yellow",
                6: "blue",
                7: "green",
                8: "red"
                }
    numery = random.choices(range(1, 8), k=4)
    ustawienie_komputer = []
    for y in numery:
        x = kolory_słownik[y]
        ustawienie_komputer.append(x)
    return ustawienie_komputer


def gra():
    '''
    Komputer sprawdza kod kolorów wpisany przez gracza
    '''
    ustawienie_komputer = wybór_kolorów()
    for próba in range(1, 10):
        dobrykolor_na_dobrymmiejscu = 0
        ustawienie_kolorów = zgadywanie_kolorów()
        for y in range(len(ustawienie_komputer)):
            if ustawienie_komputer[y] == ustawienie_kolorów[y]:
                dobrykolor_na_dobrymmiejscu += 1
        if dobrykolor_na_dobrymmiejscu == 4:
            return f'Gratulacje! Zgadłeś sekwencję w {próba} rundzie'
        tab_kolory = []
        for i in ustawienie_komputer:
            tab_kolory.append(i)
        for z in ustawienie_kolorów:
            for w in tab_kolory:
                if z == w:
                    tab_kolory.remove(w)
                    pass
        dobre_kolory = 4 - len(tab_kolory)

        print(f'Dobry kolor na dobrym miejscu: {dobrykolor_na_dobrymmiejscu}')
        print(f'Dobry kolor: {dobre_kolory}')
    return f'Niestety przegrałeś, prawidlowa sekwencja to {ustawienie_komputer}'


print(gra())
