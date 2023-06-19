import random

def magic(X):
    seq = [random.randint(0, 9999) for i in range(random.randint(5, 100))] ##Функция magic() генерирует случайную последовательность целых чисел от 0 до 9999 случайной длины от 5 до 100 элементов
    sum_seq = sum(seq) # сумма чисел последовательности
    if sum_seq % X == 0: # проверка деления суммы на X без остатка
        return True
    else:
        return False #Если это возможно, функция возвращает True, иначе - False
