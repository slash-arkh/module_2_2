def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        a = []
        for j in range(m):
            a.append(value)
        matrix.append(a)
    return matrix

result1 = get_matrix(5,3,15)
result2 = get_matrix(2,3,4)
result3 = get_matrix(5,5,5)
print(result1)
print(result2)
print(result3)
