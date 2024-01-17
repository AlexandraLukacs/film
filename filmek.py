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
    min: int= 9999999999
    min_index=0

    for i in range(0, len(lista), 1):
        if lista[i].perc < min:
            min= lista[i].perc
            min_index=i
        return min_index
    

def percfilm110(lista):
    """for i in range(0, len(lista), 1):
        if lista[i]"""