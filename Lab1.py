import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return np.sin(x)
def f2(x):
    return 1 / (1 + 25 * x ** 2)
def f3(x):
    return np.abs(x)


def chebyshev_nodes(n):
    return np.array([np.cos((2 * i - 1) * np.pi / (2 * n)) for i in range(1, n + 1)])

def equidistant_nodes(n):
    return np.array([-1 + 2 * (i - 1) / (n - 1) for i in range(1, n + 1)])


def cubic_spline(x, y, x_interp):
    n = len(x)
    h = np.diff(x)

    A = np.zeros((n, n))
    A[0, 0] = 1  # S''(x_0) = 0
    A[-1, -1] = 1  # S''(x_n) = 0
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]

    b = np.zeros(n)
    for i in range(1, n - 1):
        b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    c = np.linalg.solve(A, b)

    a = y[:-1]
    b = (y[1:] - y[:-1]) / h - h * (2 * c[:-1] + c[1:]) / 3
    d = (c[1:] - c[:-1]) / (3 * h)

    spline_values = np.zeros_like(x_interp)

    for i in range(n - 1):
        idx = np.where((x_interp >= x[i]) & (x_interp <= x[i + 1]))[0]
        dx = x_interp[idx] - x[i]
        spline_values[idx] = a[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3

    return spline_values


def lagrange_polynomial(x, y, x_interp):
    n = len(x)
    interp_values = np.zeros_like(x_interp)

    for i in range(n):
        li = np.ones_like(x_interp)
        for j in range(n):
            if i != j:
                li *= (x_interp - x[j]) / (x[i] - x[j])
        interp_values += y[i] * li

    return interp_values


def plot_cubic_spline(f, n_values, x):
    plt.figure(figsize=(12, 8))

    for n in n_values:
        nodes = np.linspace(-1, 1, n)
        values = f(nodes)
        spline_values = cubic_spline(nodes, values, x)

        plt.plot(x, spline_values, label=f'n = {n}')

    plt.plot(x, f(x), label='Исходная функция', color='black', linewidth=2, linestyle='--')
    plt.title('Интерполяция кубическим сплайном')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_lagrange_interpolation(f, n_values, x, nodes_type='равноотстоящие'):
    plt.figure(figsize=(12, 8))

    for n in n_values:
        if nodes_type == 'равноотстоящие':
            nodes = equidistant_nodes(n)
        elif nodes_type == 'чебушевские':
            nodes = chebyshev_nodes(n)

        values = f(nodes)
        interp_values = lagrange_polynomial(nodes, values, x)

        plt.plot(x, interp_values, label=f'n = {n} ({nodes_type})')


    plt.plot(x, f(x), label='Исходная функция', color='black', linewidth=2, linestyle='--')
    plt.title(f'Интерполяция полиномом Лагранжа ({nodes_type} узлы)')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    print("Выберите функцию для интерполяции:")
    print("1. f(x) = sin(x)")
    print("2. f(x) = 1 / (1 + 25x^2)")
    print("3. f(x) = |x|")

    choice = int(input("Введите номер функции: "))

    if choice == 1:
        f = f1
    elif choice == 2:
        f = f2
    elif choice == 3:
        f = f3
    else:
        raise ValueError("Неверный выбор функции")

    n_values = list(map(int, input("\nВведите значения n : ").split()))
    x = np.linspace(-1, 1, 500)

    print("\n1. Построение интерполяционного полинома Лагранжа")
    print("2. Построение кубического сплайна")

    task_choice = int(input("Введите номер задачи: "))

    print("\n1. Равноотстоящие узлы")
    print("2. Узлы Чебышева")
    nodes_choice = int(input("Выберите тип узлов: "))

    if nodes_choice == 1:
        node_type = 'равноотстоящие'
    elif nodes_choice == 2:
        node_type = 'чебушевские'
    else:
        raise ValueError("Неверный выбор типа узлов")

    if task_choice == 1:
        plot_lagrange_interpolation(f, n_values, x, nodes_type=node_type)
    elif task_choice == 2:
        plot_cubic_spline(f, n_values, x)
    else:
        raise ValueError("Неверный выбор задачи")
