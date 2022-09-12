# importam o "functie?" dintr-un modul
import modul_2
numbers = [10, 3, 9, 7, 99]

#print(modul_2.max)  # rulam metoda din modul

#find_max(max)
maximum = modul_2.find_max(numbers)
print(maximum)

numbers = [10, 30, 9, 7]
numbers.append(100)
maximum = modul_2.find_max(numbers)
print(maximum)
print('------- # MODULES -------------------')
