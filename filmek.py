from Film import Film

def fajlbeolv():
    film_lista=[]
    f=open("film.txt", "r", encoding="utf-8")
    f.readline()
    fajl_lista=f.readlines()
    f.close
    for i in range(0, len(fajl_lista), 1):
        aktsor=fajl_lista[i].strip().split(";")
        film=Film(aktsor[0], aktsor[1], aktsor[2], int(aktsor[3]), int(aktsor[4]))
        print(film.cim, film.rendezo, film.foszereplo, film.ev, film.perc)
        film_lista.append(film)
    return film_lista

def legrovidebb_film_cim(lista):
    min_index=0
    min: int= lista[min_index].perc
    for i in range(0, len(lista), 1):
        if lista[i].perc < min:
            min= lista[i].perc
            min_index=i
    return min_index
    

def percfilm110(lista):
    db: int= 0
    for i in range(0, len(lista), 1):
        if lista[i].perc >= 110:
            db += 1
    return db


def szinesz_film(lista):
    szinesz: str= str(input("Adjon meg egy színész nevet: "))
    van: int= 0
    for i in range(0, len(lista), 1):
        if lista[i].foszereplo == szinesz:
            print(f"Pár film ajánlás: {lista[i].cim}")
            van = 1
    if van == 0:
        print("Nincs ilyen nevű színséz")
    return szinesz


def kiir(lista, szinesz):
    fajl=open("film2.txt", "w", encoding="utf-8")
    van: int= 0
    for i in range(0, len(lista), 1):
        if lista[i].foszereplo == szinesz:
            fajl.write(f"Pár film ajánlás: {lista[i].cim}\n")
            van = 1
    if van == 0:
        fajl.write("Nincs ilyen nevű színséz")
    fajl.close()
