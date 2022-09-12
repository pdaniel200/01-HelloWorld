import math

print('*' * 100)
price = 200
print(price)

name = 'Johnnn Smitnh'
age = 20
is_new = True

numar_litera_n = name.count('n') # metoda care numara de cate ori apare 'n' in variabila name

print(len(name)) # functia len citeste cate litere apar in variabila
print(str(numar_litera_n) * int(len(name)))


propozitie = 'Cineva merge la pescuit si vrea sa prinda peste cu undita, o sa mearga cu masina pana la un rau de munte'
print(propozitie)
numar_litera = 8
detectare_litere = propozitie[int(numar_litera)]  # extrage litera cu numarul setat din variabila numar_litera
print(detectare_litere)
citire_litere = propozitie.count(detectare_litere)  # metoda care citeste cate litere de acel fel sunt in propozitie
print(citire_litere)
afisare_n_litera = detectare_litere * citire_litere  # multiplica litera de atatea ori de cat apare in propozitie
print(afisare_n_litera.upper())  # afiseaza multiplicarea si o transforma in litere mari

print(2 ** 5)  # la puterea
print(abs(-2.9))  # transforma tot timpul in numar pozitiv
print(math.ceil(2.9))  # rotunjeste in sus
print(math.floor(2.9))  # rotunjeste in jos

house_price = 1000000
good_credit = True
if good_credit:
    house_price *= 0.1
else:
    house_price *= 0.2
print(f'You need to put {house_price}$ down payment')


name = 'John Smith'
lenght = int(len(name))
if lenght < 3:
    print('Name must be at least 3 characters long')
elif lenght > 20:
    print('Name can be maximum 20 characters')
else:
    print('Name looks good')


numar_incercari = 1
limita_incercari = 5
unitate_masura = ''
weight = input('Weight: ')

while numar_incercari < limita_incercari and weight.isnumeric() == False:
    print('Mai incerca o data!')
    weight = input('Weight in numbers: ')
    numar_incercari += 1
    if weight.isnumeric():
        while unitate_masura != 'k' or unitate_masura != 'l':
            unitate_masura = input('(L)bs or (K)g: ').lower()
            if unitate_masura == 'k':
                print(f'You are {int(weight) / 0.45} pounds')
                break
            elif unitate_masura == "l":
                print(f'You are {int(weight) * 0.45} kilograms')
                break
        break
    elif numar_incercari < limita_incercari:
        print(f'Ai incercat de {numar_incercari} ori!')
else:
    if weight.isnumeric():
        while unitate_masura != 'k' or unitate_masura != 'l':
            unitate_masura = input('(L)bs or (K)g: ').lower()
            if unitate_masura == 'k':
                print(f'You are {int(weight) / 0.45} pounds')
                break
            elif unitate_masura == "l":
                print(f'You are {int(weight) * 0.45} kilograms')
                break

    else:
        print(f'Cam atat pentru astazi!')







'''
unitate_masura = input('(L)bs or (K)g: ')
masura = unitate_masura.lower()



if masura == "k":
    print(f'You are {int(weight) / 0.45} pounds')
elif masura == "l":
    print(f'You are {int(weight) * 0.45} kilograms')
else:


print(f'Write a measure unit, L for pounds or K for kilograms: ')
unitate_masura = input()
'''