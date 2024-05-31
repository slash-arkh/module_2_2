n = int(input('Введите случайное число от 3 до 20: '))
key = []
for i in range(1, n):
    for j in range(i+1, n):
        if n % (i+j) == 0:
            key.append(i)
            key.append(j)
print(*key)

