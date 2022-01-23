from mastermind import Gra, Gracz_ustawiajacy_kod
from mastermind import Gracz_zgadujacy_kod, Gracz_komputer_ustawiajacy_kod
from mastermind import Gracz_komputer_kod_losowy
from mastermind import Gracz_komputer_kod_taktyczny
import argparse
from termcolor import colored
from tabulate import tabulate


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
        print("Gracz 2 próbuje odgadnąć kod")
        print("Gracz 1:")
        kod = Gracz_ustawiajacy_kod.ustawienie_kod_gracz()
        ustawienia_kolorow = []
        for proba in range(1, 11):
            runda = []
            print(f'Próba: {proba}')
            print("Gracz 2:")
            print(tabulate(ustawienia_kolorow))
            ustawienie_kolorow = Gracz_zgadujacy_kod.zgadywanie_kolorow()
            for element in ustawienie_kolorow:
                if element == "czarny":
                    tekst = colored("czarny", "grey")
                if element == "biały":
                    tekst = colored("biały", "white")
                if element == "żółty":
                    tekst = colored("żółty", "yellow")
                if element == "niebieski":
                    tekst = colored("niebieski", "blue")
                if element == "zielony":
                    tekst = colored("zielony", "green")
                if element == "czerwony":
                    tekst = colored("czerwony", "red")
                runda.append(tekst)
            print(ustawienie_kolorow)
            print("Gracz 1:")
            dk = Gracz_ustawiajacy_kod.sprawdzanie_dobry_kolor(ustawienie_kolorow, kod)
            dkndm = Gracz_ustawiajacy_kod.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
            tekst1 = colored(f'{dk}', 'white')
            print(f'Dobry kolor: {tekst1}')
            tekst2 = colored(f'{dkndm}', 'red')
            print(f'Dobry kolor na dobrym miejscu: {tekst2}')
            runda.append(tekst1)
            runda.append(tekst2)
            ustawienia_kolorow.append(runda)
            if dkndm == 4:
                print("Gratulacje Gracz 2, wygrałeś!!!")
                return
        print("Niestety Gracz 2, przegrałeś!:(")
        return
    if args.kg:
        ustawienia_kolorow = []
        print("kod = ****")
        print("Spróbuj odgadnąć kod ;)")
        kod = Gracz_komputer_ustawiajacy_kod.ustawienie_kod_komputer()
        for proba in range(1, 11):
            runda = []
            print(f'Próba: {proba}')
            print(tabulate(ustawienia_kolorow))
            ustawienie_kolorow = Gracz_zgadujacy_kod.zgadywanie_kolorow()
            for element in ustawienie_kolorow:
                if element == "czarny":
                    tekst = colored("czarny", "grey")
                if element == "biały":
                    tekst = colored("biały", "white")
                if element == "żółty":
                    tekst = colored("żółty", "yellow")
                if element == "niebieski":
                    tekst = colored("niebieski", "blue")
                if element == "zielony":
                    tekst = colored("zielony", "green")
                if element == "czerwony":
                    tekst = colored("czerwony", "red")
                runda.append(tekst)
            print(ustawienie_kolorow)
            dk = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorow, kod)
            dkndm = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
            tekst1 = colored(f'{dk}', 'white')
            print(f'Dobry kolor: {tekst1}')
            tekst2 = colored(f'{dkndm}', 'red')
            print(f'Dobry kolor na dobrym miejscu: {tekst2}')
            runda.append(tekst1)
            runda.append(tekst2)
            ustawienia_kolorow.append(runda)
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
            runda = []
            print(f'Próba: {proba}')
            print(tabulate(ustawienia_kolorow))
            ustawienie_kolorow = Gracz_komputer_kod_losowy.zgadywanie_kodu()
            for element in ustawienie_kolorow:
                if element == "czarny":
                    tekst = colored("czarny", "grey")
                if element == "biały":
                    tekst = colored("biały", "white")
                if element == "żółty":
                    tekst = colored("żółty", "yellow")
                if element == "niebieski":
                    tekst = colored("niebieski", "blue")
                if element == "zielony":
                    tekst = colored("zielony", "green")
                if element == "czerwony":
                    tekst = colored("czerwony", "red")
                runda.append(tekst)
            print(ustawienie_kolorow)
            dk = Gracz_ustawiajacy_kod.sprawdzanie_dobry_kolor(ustawienie_kolorow, kod)
            dkndm = Gracz_ustawiajacy_kod.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
            tekst1 = colored(f'{dk}', 'white')
            print(f'Dobry kolor: {tekst1}')
            tekst2 = colored(f'{dkndm}', 'red')
            print(f'Dobry kolor na dobrym miejscu: {tekst2}')
            runda.append(tekst1)
            runda.append(tekst2)
            ustawienia_kolorow.append(runda)
            if dkndm == 4:
                print("Komputer odgadł Twój kod")
                return
        print("Komputer nie odgadł Twojego kodu")
        return
    if args.gkt:
        ustawienia_kolorow = []
        print("Ustaw kod")
        kod = Gracz_ustawiajacy_kod.ustawienie_kod_gracz()
        kombinacje = Gracz_komputer_kod_taktyczny.kombinacje()
        for proba in range(1, 11):
            runda = []
            print(f'Próba: {proba}')
            print(tabulate(ustawienia_kolorow))
            ustawienie_kolorow = Gracz_komputer_kod_taktyczny.zgadywanie_kodu(kombinacje)
            for element in ustawienie_kolorow:
                if element == "czarny":
                    tekst = colored("czarny", "grey")
                if element == "biały":
                    tekst = colored("biały", "white")
                if element == "żółty":
                    tekst = colored("żółty", "yellow")
                if element == "niebieski":
                    tekst = colored("niebieski", "blue")
                if element == "zielony":
                    tekst = colored("zielony", "green")
                if element == "czerwony":
                    tekst = colored("czerwony", "red")
                runda.append(tekst)
            print(ustawienie_kolorow)
            dk = Gracz_ustawiajacy_kod.sprawdzanie_dobry_kolor(ustawienie_kolorow, kod)
            dkndm = Gracz_ustawiajacy_kod.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
            tekst1 = colored(f'{dk}', 'white')
            print(f'Dobry kolor: {tekst1}')
            tekst2 = colored(f'{dkndm}', 'red')
            print(f'Dobry kolor na dobrym miejscu: {tekst2}')
            runda.append(tekst1)
            runda.append(tekst2)
            ustawienia_kolorow.append(runda)
            if dkndm == 4:
                print("Komputer odgadł Twój kod")
                return
            ustawienie_kolorow_cyfry = Gracz_komputer_kod_taktyczny.zamienienie_kolorow_na_cyfry(ustawienie_kolorow)
            kombinacje = Gracz_komputer_kod_taktyczny.usuwanie_kombinacji(ustawienie_kolorow_cyfry, kombinacje, dkndm, dk)
        print("Komputer nie odgadł Twojego kodu")
        return
    if args.kkt:
        ustawienia_kolorow = []
        print("kod = ****")
        kod = Gracz_komputer_ustawiajacy_kod.ustawienie_kod_komputer()
        kombinacje = Gracz_komputer_kod_taktyczny.kombinacje()
        for proba in range(1, 11):
            runda = []
            print(f'Próba:{proba}')
            print(tabulate(ustawienia_kolorow))
            ustawienie_kolorow = Gracz_komputer_kod_taktyczny.zgadywanie_kodu(kombinacje)
            for element in ustawienie_kolorow:
                if element == "czarny":
                    tekst = colored("czarny", "grey")
                if element == "biały":
                    tekst = colored("biały", "white")
                if element == "żółty":
                    tekst = colored("żółty", "yellow")
                if element == "niebieski":
                    tekst = colored("niebieski", "blue")
                if element == "zielony":
                    tekst = colored("zielony", "green")
                if element == "czerwony":
                    tekst = colored("czerwony", "red")
                runda.append(tekst)
            print(ustawienie_kolorow)
            dk = Gra.sprawdzanie_dobry_kolor(ustawienie_kolorow, kod)
            dkndm = Gra.sprawdzanie_dobry_kolor_miejsce(ustawienie_kolorow, kod)
            tekst1 = colored(f'{dk}', 'white')
            print(f'Dobry kolor: {tekst1}')
            tekst2 = colored(f'{dkndm}', 'red')
            print(f'Dobry kolor na dobrym miejscu: {tekst2}')
            runda.append(tekst1)
            runda.append(tekst2)
            ustawienia_kolorow.append(runda)
            if dkndm == 4:
                print("Komputer odgadł kod")
                return
            ustawienie_kolorow_cyfry = Gracz_komputer_kod_taktyczny.zamienienie_kolorow_na_cyfry(ustawienie_kolorow)
            kombinacje = Gracz_komputer_kod_taktyczny.usuwanie_kombinacji(ustawienie_kolorow_cyfry, kombinacje, dkndm, dk)
        print("Komputer nie odgadł kodu")
        return


if __name__ == "__main__":
    main()
