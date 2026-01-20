k = ["yaroslav"]
s = ["Yarik123."]
           
def auth(k, s)->str:
    login = input("Sisesta kasutajanimi: ")
    parool = input("Sisesta parool: ")
    if login in k:
        indeks = k.index(login)
        if s[indeks] == parool:
            return True
    else:
        print("Vale kasutajanimi või parool")
