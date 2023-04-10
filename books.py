import random
from colorama import init, Fore, Back, Style

# Initializare, incat sa fie accesibile culorile
init()
n_carti = 66

v_Testament = ["Geneza", "Exodul", "Leviticul", "Numeri", "Deuteronomul",
               "Iosua", "Judecatori", "Rut", "1 Samuel", "2 Samuel",
               "1 Imparati", "2 Imparati", "1 Cronici", "2 Cronici",
               "Ezra", "Neemia", "Estera", "Iov", "Psalmi", "Proverbe",
               "Eclesiastul", "Cantarea Cantarilor", "Isaia", "Ieremia",
               "Plangerile lui Ieremia", "Ezechiel", "Daniel", "Osea",
               "Ioel", "Amos", "Obadia", "Iona", "Mica", "Naum", "Habacuc",
               "Tefania", "Hagai", "Zaharia", "Maleahi"]

n_Testament = ["Matei", "Marcu", "Luca", "Ioan", "Faptele Apostolilor", "Romani", "1 Corinteni",
               "2 Corinteni", "Galateni", "Efeseni", "Filipeni", "Coloseni", "1 Tesaloniceni",
               "2 Tesaloniceni", "1 Timotei", "2 Timotei", "Tit", "Filimon", "Evrei", "Iacov",
               "1 Petru", "2 Petru", "1 Ioan", "2 Ioan", "3 Ioan", "Iuda", "Apocalipsa"]

alegere = input("Noul sau Vechiul?: ")


if alegere == 'Noul':
    print("Cartea pe care o vei citi este: " +
          Fore.RED + random.choice(n_Testament))
elif alegere == 'Vechiul':
    print("Cartea pe care o vei citi este: " +
          Fore.CYAN + random.choice(v_Testament))
else:
    print("Iesire...")
