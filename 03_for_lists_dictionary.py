# afisare din ce este compus un string
for item in "Python":
    print(item)

names = ['John', 'Maria', 'Mirela', 'Adina']

# de afisat totalul dintr-un range
prices = range(10, 20, 3)
total = 0

for price in prices:
    total = total + price
print(total)
print(sum(prices))

# nestet loop sau loop in loop
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'{y}, {z}, {x}')

numbers = range(0, 100, 10)
'''
for letter in numbers:
    print(letter * '*')
'''
print('--------------------------')

# de afisat nr de plusuri dintr-un range de la 0 la 100, contorizat din 10 in 10 unitati
numbers = range(0, 100, 10)
for xcount in numbers:
    output = ''
    for count in range(xcount):
        output += '+'
    print(output)

print('----de scris unele cuvinte dintr-o de atatea ori de cate litere este compus cuvantul----------------------')

# de scris unele cuvinte dintr-o de atatea ori de cate litere este compus cuvantul
names = ['John', 'Maria', 'Mirela', 'Adina']
print(names)
for namecount in names[1:3]:
    # output = 0
    # print(namecount)
    for namemulti in namecount:
        output = len(namecount)
        for final in namemulti:
            output2 = output * namecount
    print(output2)

print('---cum gasim cel mai mare numar dintr-o lista V1-----------------------')

# cum gasim cel mai mare numar dintr-o lista
listlargest = [5, 9, 8, 2, 0, 22]
print(f'V1 Cel mai mare nr din lista este: {max(listlargest)}')

print('---cum gasim cel mai mare numar dintr-o lista V2-----------------------')

# cum gasim cel mai mare numar dintr-o lista V2
maxnr = listlargest[0]
for test_number in listlargest:
    if test_number > maxnr:
        maxnr = test_number
print(f'V2 Cel mai mare nr din lista este: {maxnr}')

print('---2D LISTS - liste 2D - cum accesam un element dintr-o lista 2D-----------------------')

# 2D LISTS - liste 2D - cum accesam un element dintr-o lista 2D

matrix = [
    [1, 2, 7, 4],
    [2, 8, 1],
    [9, 6, 3, 8, 7]
]

print(matrix[0][2])
matrix[0][2] = 20  # asa se modifica valoarea din matrice 2D
print(matrix[0][2])

print('------afisare toate nr din matrice--------------------')

# afisare toate nr din matrice
for row in matrix:
    for item in row:
        print(item)

print('--adaugare nr in lista ------------------------')

# adaugare numere in lista
matrix.append([23, 5] + [21, 8])  # adaugare la capatul listei
matrix.insert(2, [222, 99])  # adaugare lista in 2D lista
matrix[0].remove(4)
print(matrix)

print('------- liste -------------------')

# liste
lista = [5, 9, 8, 2, 0, 2, 22]
# lista.clear() # sterge lista
print(lista)
lista.pop()  # sterge ultimul item din lista
print(lista)
print(lista.index(8))  # afiseaza ce index in lista are valoarea introdusa
print(50 in lista)  # boolean value atunci cand verificam daca valoarea introdusa este in lista
print(lista.count(2))  # verifica de cate ori apare valoarea dorita intr-o lista
lista.sort()  # sorteaza ascendent lista
lista.reverse()  # sorteaza descendent
print(lista)
lista2 = lista.copy()
print(lista2)

print('------- sterge duplicate in liste -------------------')

lista = [5, 8, 9, 8, 2, 0, 2, 22]
print(lista)
unice = []  # adaugam empty list
for numar in lista:
    if numar not in unice:
        unice.append(numar)
print(unice)

print('------- # DICTIONARY -------------------')

customer = {
    'name': 'John Smith',
    'age': 30,
    'email': 'john@gmail.com',
    'isverified': True
}
print(customer['name'])
print(customer['age'])
print(customer.get('birthdate'))  # afiseaza daca apare valoarea din dictionar
print(customer.get('birthdate', 'Jan 1'))  # daca key value nu exista, adauga
customer['name'] = 'Jack Smith'  # modifica valoarea cheii din dictionar
print(customer['name'])

print('------- # DICTIONARY EXAMPLE 1 -------------------')
# phone = input('Input Phone: ')
phone = '9878979'
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ''
for num in phone:
    output = output + digits_mapping.get(num, "!") + " "
print(output)
print(f'Numarul contine {len(phone)} cifre')

print('------- # DICTIONARY EXAMPLE 2 -------------------')

msg = 'Buna ziua! :) Astazi am dormit 8 ore :D As mai dormi inca o ora :P'
words = msg.split(' ')  # impartim cuvintele in functie de spatiu sau liniuta
print(words)  # printam de proba lista words
smiley_mapping = {
    ':)': '😊',
    ':(': '😔',
    ':D': '😁',
    ':P': '😜'
}
output = ''  # stabilim variabila goala
for word in words:  # ne uitam in lista splituita words si mapam cu dictionarul
    output += smiley_mapping.get(word, word) + ' '
print(output)

print('------- #  -------------------')
