number = int(input("Введите число: "))
first = 15
second = 17
third = 20
if first == second == third:
    print(3)
else:
    print('Неверно')
if first == second or first == third or second == third:
    print(2)
else:
    print('Неверно')
if first != second or first != third or second != third:
    print(0)
else:
    print('Неверно')