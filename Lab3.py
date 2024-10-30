import numpy as np

def Metod_Gaussa(A, f):
    n = len(f)

    Af = np.concatenate((A, f.reshape(n, 1)), axis=1)

    for i in range(n-1):
        if Af[i,i] == 0:
            for h in range(i+1, n):
                if Af[h,i] != 0:
                    for l in range(i, n+1):
                        temp = Af[i,l]
                        Af[i,l] = Af[h,l]
                        Af[h,l] = temp
        pivot = Af[i,i]

        for j in range(i+1, n):
            factor = Af[j, i]/pivot
            for k in range(i, n+1):
                temp = Af[i,k]
                Af[j,k] -= temp * factor

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        s = sum(Af[i, j] * x[j] for j in range(i + 1, n))
        x[i] = (Af[i, -1] - s) / Af[i, i]

    return x

def Metod_Holeckogo(A, f):
    L = np.linalg.cholesky(A)
    y = np.linalg.solve(L, f)
    x = np.linalg.solve(L.T, y)
    r = np.dot(A, x) - f
    return x, r

n = int(input("Введите размерность матрицы и вектора: "))
A = np.zeros((n, n))
print("Введите элементы матрицы A:")
for i in range(n):
  row = input().split()
  A[i] = [float(x) for x in row]

print("Введите элементы вектора f:")
f = [float(x) for x in input().split()]
f = np.array(f)

x = Metod_Gaussa(np.copy(A), np.copy(f))
r = np.dot(np.copy(A), x) - f
print("Решение системы уравнений методом Гаусса: ", x)
print("Остаток r = Ax - f: ", r)

x, r = Metod_Holeckogo(np.copy(A), np.copy(f))
print("\nРешение системы уравнений методом Холецкого: ", x)
print("Остаток r = Ax - f: ", r)