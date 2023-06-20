def sum_range(start, end):
    if start > end:
        start, end = end, start # если первое число больше второго, меняем их местами
    return sum(range(start, end+1)) # суммируем числа от start до end включительно

start = int(input("Введите начальное значение диапазона: "))
end = int(input("Введите конечное значение диапазона: "))
result = sum_range(start, end)
print("Сумма чисел от", start, "до", end, "включительно равна", result)

