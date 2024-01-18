import filmek

lista=filmek.fajlbeolv()
legrovfilmcim=filmek.legrovidebb_film_cim(lista)
print(f"A legrövidebb film címe: {lista[legrovfilmcim].cim}")
perc110=filmek.percfilm110(lista)
print(f"{perc110} db legalább 110 perces film van")
szineszesfilm=filmek.szinesz_film(lista)
filmek.kiir(lista, szineszesfilm)