first = input("Введите число: ")
second = input("Введите число: ")
third = input("Введите число: ")

if first == second and first == third:
    print('Все', 3, 'числа равны между собой')
elif first == second or first == third or second == third:
    print(2, 'числа равны между собой')
else:
    print('Обнаружено', 0, 'равных между собой чисел')