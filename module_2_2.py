namber1 = int(input('Введите три числа: Первое число  '))
namber2 = int(input("Ведите второе число "))
namber3 = int(input("Введте третье число "))
if namber1== namber2== namber3:
    print("Савподение трех чисел ")
elif namber1==namber2 or namber2==namber3 or namber1==namber3:
    print('Совподение двух чисел ')
else : print("Не одного совпадения")