c, f = map(int, input().split()) #кол-во городов и прямых рейсов

# матрица short путей
matrix = [[float('inf') for j in range(c)] for i in range(c)]

for i in range(c): #обнуляемся, расстояние между одним и тем же городом = 0
    matrix[i][i] = 0

# данные о прямых рейсах между городами и добавляем элементы в матрицу short путей
for i in range(f):
    x, y, p = map(int, input().split())
    matrix[x-1][y-1] = p
    matrix[y-1][x-1] = p

# алгоритм Флойда-Уоршелла для нахождения the shortest пути между всеми парами городов
for k in range(c):
    for i in range(c):
        for j in range(c):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

# перебираем все пары городов и фиксируем максимальную стоимость
max_cost = 0
for i in range(c):
    for j in range(i+1, c):
        max_cost = max(max_cost, matrix[i][j])

print(max_cost)

