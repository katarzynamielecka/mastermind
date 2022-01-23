from ast import arguments
from mastermind import Gra, Gracz_ustawiajacy_kod
from mastermind import Gracz_zgadujacy_kod, Gracz_komputer_ustawiajacy_kod
from mastermind import Gracz_komputer_kod_losowy
from mastermind import Gracz_komputer_kod_taktyczny
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-gg', action='store_true',
                        help="Dwóch graczy.")
    parser.add_argument('-kg',  action='store_true',
                        help="Gracz komputerowy ustalający kod i gracz zgadujący.")
    parser.add_argument('-gkl', action='store_true',
                        help="Gracz ustalający kod i gracz komputerowy zgadujący losowo.")
    parser.add_argument('-gkt', action='store_true',
                        help="Gracz ustalający kod i gracz komputerowy zgadujący.")
    parser.add_argument('-kkt', action='store_true',
                        help="Dwóch graczy komputerowych.")
    args = parser.parse_args()
    if args.gg:
        print("Gracz 1 ustala kod")
        print("Gracz drugi ptóbuje odgadnąć kod")
        print("Gracz 1:")
        kod = Gracz_ustawiajacy_kod.ustawienie_kod_gracz()
        ustawienia_kolorow = []
        for proba in range(1, 11):
            print(f'{proba}')
            print("Gracz 2:")
            ustawienie_kolorow = Gracz_zgadujacy_kod.zgadywanie_kolorow()
            ustawienia_kolorow.append(ustawienie_kolorow)
            print("Gracz 1:")
            dkndm = Gracz_ustawiajacy_kod.sprawdzanie_zgadniecia(ustawienie_kolorow, kod)
            if dkndm == 4:
                print("Gratulacje Gracz 2, wygrałeś!!!")
                return
        print("Niestety Gracz 2, przegrałeś!:(")
        return
    if args.kg:
        ustawienia_kolorow = []
        print("Spróbuj odgadnąć kod ;)")
        kod = Gracz_komputer_ustawiajacy_kod.ustawienie_kod_komputer()
        for proba in range(1, 11):
            print(f'{proba}')
            ustawienie_kolorow = Gracz_zgadujacy_kod.zgadywanie_kolorow()
            ustawienia_kolorow.append(ustawienie_kolorow)
            dk = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorow, kod)
            print(f'Dobry kolor: {dk}')
            dkndm = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
            print(f'Dobry kolor na dobrym miejscu: {dkndm}')
            if dkndm == 4:
                print("Gratulacje, wygrałeś!!!")
                return
        print("Niestety, przegrałeś!:(")
        return
    if args.gkl:
        ustawienia_kolorow = []
        print("Ustaw kod")
        kod = Gracz_ustawiajacy_kod.ustawienie_kod_gracz()
        for proba in range(1, 11):
            print(f'{proba}')
            ustawienie_kolorow = Gracz_komputer_kod_losowy.zgadywanie_kodu()
            ustawienia_kolorow.append(ustawienie_kolorow)
            dkndm = Gracz_ustawiajacy_kod.sprawdzanie_zgadniecia(ustawienie_kolorow, kod)
            if dkndm == 4:
                print("Komputer odgadł Twój kod")
                return
        print("Komputer nie odgadł Twojego kodu")
        return



if __name__ == "__main__":
    main()
