import random


def beker():
    paros_lista = []
    szam1 = int(input("Kérem az 1. páros számot! "))
    while szam1 % 2 != 0:
        szam1 = int(input("Ez nem PÁROS! Kérem az 1. páros számot! "))
    print(szam1)
    paros_lista.append(szam1)

    szam2 = int(input("Kérem az 2. páros számot! "))
    while szam2 % 2 != 0:
        szam2 = int(input("Ez nem PÁROS! Kérem az 2. páros számot! "))
    print(szam2)
    paros_lista.append(szam2)

    szam3 = int(input("Kérem az 3. páros számot! "))
    while szam3 % 2 != 0:
        szam3 = int(input("Ez nem PÁROS! Kérem az 3. páros számot! "))
    print(szam3)
    paros_lista.append(szam3)
    print(f"A páros számok listája: {paros_lista}")

    legkisebb_paros = 0
    legkisebb_index= 0
    if szam1 < szam2 and szam1 < szam3:
        legkisebb_paros = szam1
        legkisebb_index = 1
    if szam2 < szam1 and szam2 < szam3:
        legkisebb_paros = szam2
        legkisebb_index = 2
    if szam3 < szam1 and szam3 < szam2:
        legkisebb_paros = szam3
        legkisebb_index = 3
    print(f"A {legkisebb_index}. lépésben adta meg a legkisebb páros számot, melynek értéke: {legkisebb_paros}")
    print("")



#13 db veletlen szam kiirasa, [-40,150] zart intervallumban.
#A generált értékeket tárold lista adatszerkezetben

def veletlen_szamok_lista():
    lista = []
    i = 0
    while i < 13:
        vel = int(random.random() * 111) - 40
        i += 1
        lista.append(vel)
    print(f"A lista: {lista}")
    ketjegyuek_szama(lista)
    paros_osszege(lista)
    paros_osszege(lista)



def ketjegyuek_szama(lista):
    i =0
    ketjegyu_db = 0
    while i < len(lista):
        if 100 > lista[i] > 9 or -100 < lista[i] < -9:
            ketjegyu_db += 1
        i += 1
    print(f"A kétjegyű számok száma: {ketjegyu_db}")
    return ketjegyu_db


def paros_osszege(lista):
    i = 0
    parosok_osszege = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            parosok_osszege += lista[i]
        i += 1
    print(f"A párosok összege:  {parosok_osszege}")
    return parosok_osszege

def paratlan_osszege(lista):
    i = 0
    paratlanok_osszege = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            paratlanok_osszege += lista[i]
        i += 1
    print(f"A páratlan számok összege: {paratlanok_osszege}")
    return paratlanok_osszege

def nagyobb():
    if parosok_osszege > paratlanok_osszege:
        elvalasztojel = ">"
    else:
        elvalasztojel = "<"
    print(f"A párosok összege {parosok_osszege} {elvalasztojel} a páratalanok összege {paratlanok_osszege}")
    print("")




def beolvasas(fajlnev):
    print("")
    fajlom = open(fajlnev, "r", encoding='utf-8')
    fejlec = fajlom.readline().strip().split(";")
    print(fejlec)
    sorok = fajlom.readlines()
    fajlom.close()
    fajlfeldolgozas(sorok)

stadion = []
varos = []
csapatok_szama= []
elso_merkozes = []
utolso_merkozes = []

def fajlfeldolgozas(sorok):
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split(";")
        stadion.append(sor[0])
        varos.append(sor[1])
        csapatok_szama.append(sor[2])
        elso_merkozes.append(sor[3])
        utolso_merkozes.append(sor[4])
        i += 1
    print(stadion)
    print(varos)
    print(csapatok_szama)
    print(elso_merkozes)
    print(utolso_merkozes)
    print(f"A csapatok darabszáma: {len(csapatok_szama)} darab")














