from mastermind import Gra, Gracz_ustawiający_kod, Gracz_zgadujący_kod
from mastermind import Gracz_komputer_ustawiający_kod
from mastermind import Gracz_komputer_zgadujący_kod_losowo, Gracz_komputer_zgadujący_kod_taktyka


def test_kolory_słownik():
    x = Gra.kolory_lista()
    y = ['czarny', 'biały', 'szary', 'różowy', 'żółty', 'niebieski', 'zielony', 'czerwony']
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


def test_sprawdzanie_dobry_kolor_miejsce_komp1():
    ustawienie_kolorów = ["biały", "biały", "niebieski", "zielony"]
    kod = ["biały", "czarny", "biały", "zielony"]
    x = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorów, kod)
    assert x == 2


def test_sprawdzanie_dobry_kolor_miejsce_komp2():
    ustawienie_kolorów = ["biały", "biały", "biały", "biały"]
    kod = ["biały", "biały", "biały", "biały"]
    x = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorów, kod)
    assert x == 4


def test_sprawdzanie_dobry_kolor_miejsce_komp3():
    ustawienie_kolorów = ["biały", "biały", "biały", "biały"]
    kod = ["biały", "biały", "biały", "biały"]
    x = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorów, kod)
    assert x == 4


def test_sprawdzanie_dobry_kolor_miejsce_komp4():
    ustawienie_kolorów = ["biały", "zielony", "czerwony", "żółty"]
    kod = ["szary", "niebieski", "żółty", "czarny"]
    x = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorów, kod)
    assert x == 0


def test_sprawdzanie_dobry_kolor_komp1():
    ustawienie_kolorów = ["czarny", "niebieski", "zielony", "żółty"]
    kod = ["niebieski", "biały", "biały", "żółty"]
    x = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorów, kod)
    assert x == 2


def test_sprawdzanie_dobry_kolor_komp2():
    ustawienie_kolorów = ["czarny", "czarny", "czarny", "żółty"]
    kod = ["czarny", "biały", "niebieski", "żółty"]
    x = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorów, kod)
    assert x == 2


def test_sprawdzanie_dobry_kolor_komp3():
    ustawienie_kolorów = ["czarny", "czarny", "czarny", "żółty"]
    kod = ["czarny", "czarny", "zielony", "żółty"]
    x = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorów, kod)
    assert x == 3
