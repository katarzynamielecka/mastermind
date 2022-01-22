from mastermind import Gra
from mastermind import Gracz_komputer_zgadujacy_kod_taktyka


def test_kolory_słownik():
    x = Gra.kolory_lista()
    y = ['czarny', 'biały', 'żółty', 'niebieski', 'zielony', 'czerwony']
    assert x == y


def test_sprawdzanie_wpisanego_koloru_returns_True():
    w = Gra.sprawdzanie_wpisanego_koloru("czarny")
    assert w


def test_sprawdzanie_wpisanego_koloru_returns_False():
    w = Gra.sprawdzanie_wpisanego_koloru("cnjdsb")
    assert not w


def test_sprawdzanie_wpisanego_koloru_puste():
    w = Gra.sprawdzanie_wpisanego_koloru("")
    assert not w


def test_sprawdzanie_dobry_kolor_miejsce1():
    ustawienie_kolorow = ["biały", "biały", "niebieski", "zielony"]
    kod = ["biały", "czarny", "biały", "zielony"]
    x = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
    assert x == 2


def test_sprawdzanie_dobry_kolor_miejsce2():
    ustawienie_kolorow = ["biały", "biały", "biały", "biały"]
    kod = ["biały", "biały", "biały", "biały"]
    x = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
    assert x == 4


def test_sprawdzanie_dobry_kolor_miejsce3():
    ustawienie_kolorow = ["biały", "biały", "biały", "biały"]
    kod = ["biały", "biały", "biały", "biały"]
    x = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
    assert x == 4


def test_sprawdzanie_dobry_kolor_miejsce4():
    ustawienie_kolorow = ["biały", "zielony", "czerwony", "żółty"]
    kod = ["szary", "niebieski", "żółty", "czarny"]
    x = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
    assert x == 0


def test_sprawdzanie_dobry_kolor1():
    ustawienie_kolorow = ["czarny", "niebieski", "zielony", "żółty"]
    kod = ["niebieski", "biały", "biały", "żółty"]
    x = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorow, kod)
    assert x == 2


def test_sprawdzanie_dobry_kolor2():
    ustawienie_kolorow = ["czarny", "czarny", "czarny", "żółty"]
    kod = ["czarny", "biały", "niebieski", "żółty"]
    x = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorow, kod)
    assert x == 2


def test_sprawdzanie_dobry_kolor3():
    ustawienie_kolorow = ["czarny", "czarny", "czarny", "żółty"]
    kod = ["czarny", "czarny", "zielony", "żółty"]
    x = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorow, kod)
    assert x == 3


def test_zamienianie_kolorow_na_cyfry():
    ustawienie_kolorow = ['czarny', 'biały', 'żółty', 'niebieski']
    x = Gracz_komputer_zgadujacy_kod_taktyka.zamienienie_kolorow_na_cyfry(ustawienie_kolorow)
    assert x == [1, 2, 3, 4]


def test_zamienianie_kolorow_na_cyfry2():
    ustawienie_kolorow = ['czerwony', 'zielony', 'czarny', 'czarny']
    x = Gracz_komputer_zgadujacy_kod_taktyka.zamienienie_kolorow_na_cyfry(ustawienie_kolorow)
    assert x == [6, 5, 1, 1]


def test_usuwanie_kombinacji():
    ustawienie_kolorow_cyfry = [1, 2, 3, 4]
    kombinacje = [[1, 2, 3, 4], [1, 3, 6, 5], [1, 2, 3, 6], [2, 2, 3, 4]]
    dkndm = 1
    dk = 2
    x = Gracz_komputer_zgadujacy_kod_taktyka.usuwanie_kombinacji(ustawienie_kolorow_cyfry, kombinacje, dkndm, dk)
    assert x == [[1, 3, 6, 5]]


def test_usuwanie_kombinacji2():
    ustawienie_kolorow_cyfry = [1, 1, 1, 1]
    kombinacje = [[1, 1, 3, 1], [2, 3, 6, 5], [1, 3, 3, 6], [2, 2, 1, 4]]
    dkndm = 3
    dk = 3
    x = Gracz_komputer_zgadujacy_kod_taktyka.usuwanie_kombinacji(ustawienie_kolorow_cyfry, kombinacje, dkndm, dk)
    assert x == [[1, 1, 3, 1]]


def test_usuwanie_kombinacji3():
    ustawienie_kolorow_cyfry = [1, 2, 3, 4]
    kombinacje = [[1, 2, 3, 4], [1, 2, 4, 3], [4, 2, 1, 3], [1, 2, 4, 4]]
    dkndm = 2
    dk = 4
    x = Gracz_komputer_zgadujacy_kod_taktyka.usuwanie_kombinacji(ustawienie_kolorow_cyfry, kombinacje, dkndm, dk)
    assert x == [[1, 2, 4, 3]]


def test_usuwanie_kombinacji4():
    ustawienie_kolorow_cyfry = [1, 2, 3, 4]
    kombinacje = [[1, 2, 3, 4], [1, 2, 6, 4], [1, 3, 3, 4], [2, 2, 3, 4]]
    dkndm = 3
    dk = 3
    x = Gracz_komputer_zgadujacy_kod_taktyka.usuwanie_kombinacji(ustawienie_kolorow_cyfry, kombinacje, dkndm, dk)
    assert x == [[1, 2, 6, 4], [1, 3, 3, 4], [2, 2, 3, 4]]
