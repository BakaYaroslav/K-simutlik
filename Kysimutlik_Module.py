import os
import random
import smtplib
from email.message import EmailMessage


kus_vas = {
    'Mis on Eesti pealinn?': 'Tallinn', 
    'Mis värvi on lumi?': 'valge', 
    'Mitu silma on inimesel?': '2', 
    'Mis on 2 + 2?': '4', 
    'Mis on Eesti riigikeel?': 'eesti', 
    'Mis värvi on muru?': 'roheline', 
    'Kas koer ütleb miau või au?': 'au', 
    'Mis on päikese värv?': 'kollane', 
    'Mitu jalga on kassil?': '4', 
    'Kas vesi on märg või kuiv?': 'märg'
}

stat = {}


if not os.path.isfile('kysimused_vastused.txt') or os.path.getsize('kysimused_vastused.txt') == 0:
    with open('kysimused_vastused.txt', 'w', encoding='utf-8') as f:
        for j, (kysimus, vastus) in enumerate(kus_vas.items(), start=1):
            f.write(f'{j}. {kysimus}: {vastus}\n')

def int_kontroll(sisend: str) -> int:
    while True:
        try:
            arv = int(sisend)
            return arv
        except ValueError:
            sisend = input('Palun sisesta täisarv: ')

def andmete_lugemine_failidest(filename='kysimused_vastused.txt'):
    read_lines = []
    with open('kysimused_vastused.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                read_lines.append(line.strip())
                
    for i, line in enumerate(read_lines):
        print(f" {line}")

def küsimuste_lisamine():
    ''' Funktsioon küsimuste lisamiseks või kustutamiseks
        Kui me kustutamine me ostime number ja kustutame numbrini
        '''
    while True:
        valik = input('Kas soovid lisada (l) або kustutada (k) küsimusi? ').lower()
        if valik not in ['l', 'k']:
            print("Palun sisesta 'l' lisamiseks või 'k' kustutamiseks.")
            continue
        
        if valik == 'l':
            mitu_küsimust = int_kontroll(input('Mitu küsimust sa tahad lisada? '))
            if mitu_küsimust <= 0:
                print('Palun sisesta positiivne täisarv.')
                continue
            
            for i in range(mitu_küsimust):
                küs = input('Sisesta küsimus: ')
                vas = input('Sisesta vastus: ')
                stat[küs] = vas
            
            read = 0
            if os.path.isfile('kysimused_vastused.txt'):
                with open('kysimused_vastused.txt', 'r', encoding='utf-8') as f:
                    read = len(f.readlines())
            
            with open('kysimused_vastused.txt', 'a', encoding='utf-8') as f:
                for j, (kysimus, vastus) in enumerate(stat.items(), start=read + 1):
                    f.write(f'{j}. {kysimus}: {vastus}\n')
            
            print('Andmed on salvestatud.')
            break

        elif valik == 'k':
            ask = input('Oled sa kindel, et soovid KÕIK küsimused kustutada (j) või ühe kaupa (e)? ').lower()
            if ask == 'j':
                with open('kysimused_vastused.txt', 'w', encoding='utf-8') as f:
                    f.write('')
                    kus_vas.popitem # eemaldab viimase lisatud küsimuse-vastuse paari
                print('Kõik küsimused on kustutatud.')
            elif ask == 'e':
                   # lugeme olemasolevad küsimused
                with open('kysimused_vastused.txt', 'r', encoding='utf-8') as f:
                    read_lines = [line.strip() for line in f if line.strip()] # line.strip() eemaldab tühjad read, if line.strip() tagab, et ainult mitte-tühjad read lisatakse

                # Näitame olemasolevaid küsimusi
                for line in read_lines:
                    print(line)

                # Küsime kasutajalt, millised küsimused kustutada
                to_delete = input('Sisesta kustutatava küsimuse numbrid (nt 2,4): ')
                to_delete = [int(x.strip()) for x in to_delete.split(',')]
                if any(num < 1 or num > len(read_lines) for num in to_delete):  # kontrollime kehtivust
                    print('Vigased numbrid sisestatud. Proovi uuesti.')
                    continue

                # Eemaldame valitud küsimused ja loome uue nimekirja ridadega
                new_lines = []
                for i, line in enumerate(read_lines, start=1):
                    if i not in to_delete:
                        new_lines.append(line)

                # Salvestame uuendatud nimekirja faili
                with open('kysimused_vastused.txt', 'w', encoding='utf-8') as f:
                    for i, line in enumerate(new_lines, start=1):
                        question = line.split('. ', 1)[-1]  # eemaldab numbri ja punkti 
                        f.write(f"{i}. {question}\n")

                print('Küsimused kustutatud!')


            break

def emaili_saatmine():
    email_subject = 'TESTI TULEMUS'
    sender_email_address = 'jaroslavbaka25@gmail.com'
    email_password = 'qztk ogxx duva gvez'
    email_smtp = 'smtp.gmail.com'
    
    try:
        message = EmailMessage()
        if tulemus == 'SOBIS':
            body = f'Tere, {nimi}!\n\n✅ Test on edukalt läbitud!\n📊 Sinu tulemus: {score} õiget vastust.\nHästi tehtud!'
        else:
            body = f'Tere, {nimi}!\n\n❌ Sel korral test ebaõnnestus.\n📊 Sinu tulemus: {score} õiget vastust.\nÄra anna alla, proovi uuesti!'
        
        message['Subject'] = email_subject
        message['From'] = sender_email_address
        message['To'] = email
        message.set_content(body)
        
        with smtplib.SMTP_SSL(email_smtp, 465) as server:
            server.login(sender_email_address, email_password)
            server.send_message(message)
        print('Email saadetud!')
    except Exception as e:
        print('Tekkis viga emaili saatmisel:', e)

def testimine():
    global tulemus, score, nimi, email
    
    nimi = input('Sisesta oma nimi: ')
    

    nimid = []
    if os.path.isfile('kõik.txt'):
        with open('kõik.txt', 'r', encoding='utf-8') as f:
            for rida in f:
                nimid.append(rida.split(' - ')[0])
    
    if nimi in nimid:
        print(f'{nimi}, sa oled juba testi sooritanud.')
        return


    while True:
        email = input('Sisesta oma email: ')
        if '@' not in email or '.' not in email:
            print('Palun sisesta kehtiv emaili aadress.')
        else:
            break

    if not kus_vas:
        print('Küsimuste faili pole або see on tühi.')
        return

    score = 0
    with open('kysimused_vastused.txt', 'r', encoding='utf-8') as f:
        kus = f.readlines()
  
    random.shuffle(kus)
    
    rand_kus = min(5, len(kus))
    
    for i in range(rand_kus):
        kysimus, vastus = kus[i].split('. ', 1)[-1].rsplit(': ', 1) # eraldab küsimuse ja vastuse ja eemaldab numbrid 
        v = vastus.strip()
        user_answer = input(f'{kysimus.strip()} ')

        if user_answer.strip().lower() == v.lower():
            print('Õige vastus!')
            score += 1
        else:
            print(f'Vale vastus! Õige vastus on: {v}')
    
    if score >= 0.6 * rand_kus:
        print(f'Palju õnne {nimi}! Skoor: {score}')
        tulemus = 'SOBIS'
    else:
        print(f'Kahjuks ebaõnnestus {nimi}. Skoor: {score}')
        tulemus = 'EI SOBINUD'


    with open('kõik.txt', 'a', encoding='utf-8') as f:
        f.write(f'{nimi} - {score} - {email} - {tulemus}\n')
    
    if tulemus == 'SOBIS':
        with open('oiged.txt', 'a', encoding='utf-8') as f:
            f.write(f'{nimi} - {score} - {email}\n')
    else:
        with open('valed.txt', 'a', encoding='utf-8') as f:
            f.write(f'{nimi} - {score} - {email}\n')
            
    emaili_saatmine()

def andmete_kustutamine():
    files = ['kõik.txt', 'oiged.txt', 'valed.txt']
    for file in files:
        with open(file, 'w', encoding='utf-8') as f:
            f.write('')
    print('Andmed on kustutatud.')
