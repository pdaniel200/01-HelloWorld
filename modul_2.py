'''numbers = [10, 3, 9, 7, 99]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
#print(max)'''

print('------- # MODULE V2 -------------------')


# number = ''


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
