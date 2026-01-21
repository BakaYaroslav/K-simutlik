import os
from Kysimutlik_Module import * 
User = True
Admin = True
while User:
    menu_user = input("Vali tegevus: \n1. Test \n2. Sisse kui admin \n3. Välja\nSisesta valik 1-3: ")
    if menu_user in ['1', '2', '3']:
        if menu_user == '1':
            test = testimine()
            Admin = False
        elif menu_user == '2':
            login = auth(k, s)
            if login:
                print("Sisselogimine edukas. Tere tulemast, admin!")
                User = False
                Admin = True
        elif menu_user == '3':
            print("Väljumine programmist.")
            User = False
            Admin = False
    else:   
        print("Palun sisesta kehtiv valik (1-3).")



while Admin:
    menu = input("Vali tegevus: \n1. Andmete lugemine failidest\n2. Küsimuste lisamine/kustutamine\n3. Test\n4. Lisada 10 küsimused \n5. Kustutada kõik andmed\n6. Välju\nSisesta valik (1-6): ")
    if menu in ['1', '2', '3', '4', '5', '6']:
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
    else:
        print("Palun sisesta kehtiv valik (1-6).")
