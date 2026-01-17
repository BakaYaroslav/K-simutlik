import os
from Kysimutlik_Module import * 
while True:
    menu = input("Vali tegevus: \n1. Andmete lugemine failidest\n2. Küsimuste lisamine/kutvustamine\n3. Test\n4. Kustutada kõik andmed\n5. Välju\nSisesta valik (1/2/3/4/5): ")
    if menu == '1':
        read = andmete_lugemine_failidest()
        print("Küsimused ja vastused:", read)
    elif menu == '2':
        lisa = küsimuste_lisamine()
    elif menu == '3':
        test = testimine()
    elif menu == '4':
        statistika = andmete_kustutamine()
    elif menu == '5':
        print("Väljumine programmist.")
        break
