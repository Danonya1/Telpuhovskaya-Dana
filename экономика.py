S = []
D = []
print("Введите N моментов времени:")
n=int(input())
print("Введите элементы для спроса:")
for i in range(n):
    element = int(input())
    S.append(element)

print("Введите элементы для предложений:")
for i in range(n):
    element = int(input())
    D.append(element)

# просто для проверки работы проги выведем массивы
print("Первый массив:", S)
print("Второй массив:", D)

def equilibrium_points(S, D):
    count = 0
    for i in range(len(S)):
        if S[i] == D[i]:         #сравним
            count += 1
    return count
print(equilibrium_points(S, D))
