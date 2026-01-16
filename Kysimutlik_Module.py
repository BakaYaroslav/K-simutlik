read = []
kus_vas = {} # Tühja sõnastiku loomine
def andmete_lugemine_failidest(read,kus_vas):
    with open("kysimused_vastused.txt", "r") as f:
        
        for rida in f:
            read.append(rida)
        
    
    for rida in read:
        kysimus, vastus = rida.split(':') # Jagame rea kaheks
        kus_vas[kysimus.strip()] = vastus.strip() # Lisame sõnastikku
    return kus_vas, read

sõnastik = {"A":"a"}
loend = ["A"]

sõnastik, loend = andmete_lugemine_failidest(loend,sõnastik)
print(sõnastik)
print(loend)


def andmete_salvestamine_failidesse():
    pass

def testimine():
    pass

def emaili_saatmine():
    pass

def küsimuste_lisamine():
    pass
