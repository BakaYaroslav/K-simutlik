import os
from Kysimutlik_Module import * 
while True:
    menu = input("Vali tegevus: \n1. Andmete lugemine failidest\n2. Küsimuste lisamine/kustutamine\n3. Test\n4. Lisada 10 küsimused \n5. Kustutada kõik andmed\n6. Välju\nSisesta valik (1-6): ")
    if menu == '1':
        read = andmete_lugemine_failidest()
        print("Küsimused ja vastused:", read)
    elif menu == '2':
        lisa = küsimuste_lisamine()
    elif menu == '3':
        test = testimine()
    elif menu == '4':
        algne = küsimuste_algne_salvestamine()
    elif menu == '5':
        statistika = andmete_kustutamine()
    elif menu == '6':
        print("Väljumine programmist.")
        break
