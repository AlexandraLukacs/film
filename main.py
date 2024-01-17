import filmek

lista=filmek.fajlbeolv()
legrovfilmcim=filmek.legrovidebb_film_cim(lista)
print(f"A legrövidebb film címe: {lista[legrovfilmcim].cim}")