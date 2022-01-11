from mastermind import Gracz, Zle_wpisany_kolor, Gracz_komputer, Kolory


def test_kolory_słownik():
    x = Kolory.kolory_lista()
    y = ['czarny', 'biały', 'szary', 'różowy', 'żółty', 'niebieski', 'zielony', 'czerwony']
    assert x == y


def test_sprawdzanie_wpisanego_koloru_returns_True():
    w = Zle_wpisany_kolor.sprawdzanie_wpisanego_koloru("czarny")
    assert w


def test_sprawdzanie_wpisanego_koloru_returns_False():
    w = Zle_wpisany_kolor.sprawdzanie_wpisanego_koloru("cnjdsb")
    assert not w


def test_sprawdzanie_wpisanego_koloru_puste():
    w = Zle_wpisany_kolor.sprawdzanie_wpisanego_koloru("")
    assert not w


def test_sprawdzanie_dobry_kolor_miejsce_komp1():
    ustawienie_kolorów = ["biały", "biały", "niebieski", "zielony"]
    kod = ["biały", "czarny", "biały", "zielony"]
    x = Gracz_komputer.sprawdzanie_dobry_kolor_miejsce_komp(ustawienie_kolorów, kod)
    assert x == 2


def test_sprawdzanie_dobry_kolor_miejsce_komp2():
    ustawienie_kolorów = ["biały", "biały", "biały", "biały"]
    kod = ["biały", "biały", "biały", "biały"]
    x = Gracz_komputer.sprawdzanie_dobry_kolor_miejsce_komp(ustawienie_kolorów, kod)
    assert x == 4


def test_sprawdzanie_dobry_kolor_miejsce_komp3():
    ustawienie_kolorów = ["biały", "biały", "biały", "biały"]
    kod = ["biały", "biały", "biały", "biały"]
    x = Gracz_komputer.sprawdzanie_dobry_kolor_miejsce_komp(ustawienie_kolorów, kod)
    assert x == 4


def test_sprawdzanie_dobry_kolor_miejsce_komp4():
    ustawienie_kolorów = ["biały", "zielony", "czerwony", "różowy"]
    kod = ["szary", "różowy", "żółty", "czarny"]
    x = Gracz_komputer.sprawdzanie_dobry_kolor_miejsce_komp(ustawienie_kolorów, kod)
    assert x == 0


def test_sprawdzanie_dobry_kolor_komp():
    ustawienie_kolorów = ["czarny", "niebieski", "zielony", "żółty"]
    kod = ["niebieski", "biały", "różowy", "żółty"]
    x = Gracz_komputer.sprawdzanie_dobry_kolor_komp(ustawienie_kolorów, kod)
    assert x == 2


def test_sprawdzanie_dobry_kolor_komp():
    ustawienie_kolorów = ["czarny", "czarny", "czarny", "żółty"]
    kod = ["czarny", "biały", "różowy", "żółty"]
    x = Gracz_komputer.sprawdzanie_dobry_kolor_komp(ustawienie_kolorów, kod)
    assert x == 2


def test_sprawdzanie_dobry_kolor_komp():
    ustawienie_kolorów = ["czarny", "czarny", "czarny", "żółty"]
    kod = ["czarny", "czarny", "różowy", "żółty"]
    x = Gracz_komputer.sprawdzanie_dobry_kolor_komp(ustawienie_kolorów, kod)
    assert x == 3



