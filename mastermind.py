# Katarzyna Mielęcka - projekt
from mastermind_klasy import Gra, Gracz_ustawiajacy_kod
from mastermind_klasy import Gracz_zgadujacy_kod, Komputer_ustawiajacy_kod
from mastermind_klasy import Komputer_taktyczny
from mastermind_klasy import Komputer_losowy
import argparse
from termcolor import colored
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-gg', action='store_true',
                        help="Dwóch graczy.")
    parser.add_argument('-kg',  action='store_true',
                        help="Komputer ustalający kod i gracz zgadujący.")
    parser.add_argument('-gkl', action='store_true',
                        help="Gracz ustalający kod i komputer zgadujący losowo.")
    parser.add_argument('-gkt', action='store_true',
                        help="Gracz ustalający kod i komputer zgadujący.")
    parser.add_argument('-kkt', action='store_true',
                        help="Dwóch graczy komputerowych.")
    args = parser.parse_args()
    if args.gg:
        print("Gracz 1 ustala kod")
        print("Gracz 2 próbuje odgadnąć kod")
        print('')
        print("Gracz 1:")
        kod = Gracz_ustawiajacy_kod.ustawienie_kod_gracz()
        ustawienia_kolorow = []
        for proba in range(1, 11):
            runda = []
            print(f'Próba: {proba}')
            print("Gracz 2:")
            if proba != 1:
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
            dk = Gracz_ustawiajacy_kod.dobry_kolor(ustawienie_kolorow, kod)
            dkndm = Gracz_ustawiajacy_kod.dobry_kolor_miejsce(ustawienie_kolorow, kod)
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
        kod = Komputer_ustawiajacy_kod.ustawienie_kod_komputer()
        for proba in range(1, 11):
            runda = []
            print(f'Próba: {proba}')
            if proba != 1:
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
            dk = Gra.dobry_kolor(ustawienie_kolorow, kod)
            dkndm = Gra.dobry_kolor_miejsce(ustawienie_kolorow, kod)
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
            if proba != 1:
                print(tabulate(ustawienia_kolorow))
            ustawienie_kolorow = Komputer_losowy.zgadywanie_kodu()
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
            dk = Gracz_ustawiajacy_kod.dobry_kolor(ustawienie_kolorow, kod)
            dkndm = Gracz_ustawiajacy_kod.dobry_kolor_miejsce(ustawienie_kolorow, kod)
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
        kombinacje = Komputer_taktyczny.kombinacje()
        for proba in range(1, 11):
            runda = []
            print(f'Próba: {proba}')
            if proba != 1:
                print(tabulate(ustawienia_kolorow))
            ustawienie_kolorow = Komputer_taktyczny.zgadywanie_kodu(kombinacje)
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
            dk = Gracz_ustawiajacy_kod.dobry_kolor(ustawienie_kolorow, kod)
            dkndm = Gracz_ustawiajacy_kod.dobry_kolor_miejsce(ustawienie_kolorow, kod)
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
            ustawienie_cyfr = Komputer_taktyczny.ustawienie_cyfry(ustawienie_kolorow)
            kombinacje = Komputer_taktyczny.usuwanie_kombinacji(ustawienie_cyfr, kombinacje, dkndm, dk)
        print("Komputer nie odgadł Twojego kodu")
        return
    if args.kkt:
        ustawienia_kolorow = []
        print("kod = ****")
        kod = Komputer_ustawiajacy_kod.ustawienie_kod_komputer()
        kombinacje = Komputer_taktyczny.kombinacje()
        for proba in range(1, 11):
            runda = []
            print(f'Próba:{proba}')
            if proba != 1:
                print(tabulate(ustawienia_kolorow))
            ustawienie_kolorow = Komputer_taktyczny.zgadywanie_kodu(kombinacje)
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
            dk = Gra.dobry_kolor(ustawienie_kolorow, kod)
            dkndm = Gra.dobry_kolor_miejsce(ustawienie_kolorow, kod)
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
            ustawienie_cyfr = Komputer_taktyczny.ustawienie_cyfry(ustawienie_kolorow)
            kombinacje = Komputer_taktyczny.usuwanie_kombinacji(ustawienie_cyfr, kombinacje, dkndm, dk)
        print("Komputer nie odgadł kodu")
        return


if __name__ == "__main__":
    main()
