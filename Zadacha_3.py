#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#Пример:

#- Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

n = int(input("Введите количество чисел N: "))

def numbers(n):
    summ = 0
    for i in range(n):
        a = int(input(f"Введите число {i + 1}: "))
        a = (1 + 1/a)**a
        summ = a + summ
        i += 1
    return summ

print("Сумма числе равна: ", round((numbers(n)),2))