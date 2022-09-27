# De afisat numerele pare dintr-o lista si de numarat cate numere sunt pare
lista_nr = range(100)
nr_pare = 0

for lista_par in lista_nr:
    if lista_par % 2 == 0:
        # print(f'Numar par: {lista_par}')
        nr_pare += 1
print(f'Avem {nr_pare} numere pare')

print(type([*range(20)]))

var = 'Python'
count = 0
count_litera = -1
for x in var:
    while count < 6:
        count += 1
        count_litera += 1
        print(var[count_litera])
    break
