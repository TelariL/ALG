import numpy as np
import matplotlib.pyplot as plt

def f1(x):
  return np.exp(x)
def f2(x):
  return x**2
def f3(x):
  return x**3
def f4(x):
  return x**2 + 2*x + 1
def f5(x):
    return np.sin(x)
def f6(x):
    return np.cos(x)


def IntegralLeftRectangle(f, lowerLimit, upperLimit, countArtitions):
    delta_i = (upperLimit - lowerLimit) / countArtitions
    sum = 0
    for i in range(0, countArtitions):
        x_i = lowerLimit + delta_i * i
        y_i = f(x_i)
        square = delta_i * y_i
        sum += square
    return sum
def IntegralRightRectangle(f, lowerLimit, upperLimit, countArtitions):
    delta_i = (upperLimit - lowerLimit) / countArtitions
    sum = 0
    for i in range(1, countArtitions+1):
        x_i = lowerLimit + delta_i * i
        y_i = f(x_i)
        square = delta_i * y_i
        sum += square
    return sum
def IntegralCentralRectangle(f, lowerLimit, upperLimit, countArtitions):
    delta_i = (upperLimit - lowerLimit) / countArtitions
    sum = 0
    for i in range(countArtitions):
        x_i = lowerLimit + delta_i * (i + 0.5)
        y_i = f(x_i)
        square = delta_i * y_i
        sum += square
    return sum


def RungeRule(Integral_n, Integral_2n):
    return abs(Integral_2n - Integral_n) / (3)

def CalculateIntegral(f, lowerLimit, upperLimit, accuracy, method, countArtitions):
    Integral_n = method(f, lowerLimit, upperLimit, countArtitions)
    Integral_2n = method(f, lowerLimit, upperLimit, 2 * countArtitions)
    temp = RungeRule(Integral_n, Integral_2n)

    while temp > accuracy:
        countArtitions *= 2
        Integral_n = Integral_2n
        Integral_2n = method(f, lowerLimit, upperLimit, 2 * countArtitions)
        temp = RungeRule(Integral_n, Integral_2n)
    return Integral_2n, countArtitions, (upperLimit - lowerLimit) / countArtitions


print("Выберите функцию для интегрирования:")
print("1) f(x) = e^x")
print("2) f(x) = x^2")
print("3) f(x) = x^3")
print("4) f(x) = x^2 + 2x + 1")
print("5) f(x) = sin(x)")
print("6) f(x) = cos(x)")

func = int(input("Введите номер функции: "))
lowerLimit = float(input("Введите нижний предел интегрирования: "))
upperLimit = float(input("Введите верхний предел интегрирования: "))
accuracy = float(input("Введите допустимую погрешность: "))

if func == 1:
    f = f1
elif func == 2:
    f = f2
elif func == 3:
    f = f3
elif func == 4:
    f = f4
elif func == 5:
    f = f5
elif func == 6:
    f = f6
else:
    print("Ошибка ввода функции")
    exit()


result_rectangles_Left, n_rectangles_Left, step_rectangles_Left = CalculateIntegral(f, lowerLimit, upperLimit, accuracy, IntegralLeftRectangle, 2)

result_rectangles_Center, n_rectangles_Center, step_rectangles_Center = CalculateIntegral(f, lowerLimit, upperLimit, accuracy, IntegralCentralRectangle, 2)

result_rectangles_Right, n_rectangles_Right, step_rectangles_Right = CalculateIntegral(f, lowerLimit, upperLimit, accuracy, IntegralRightRectangle, 2)


plt.figure(figsize=(8, 4))
plt.title("Интеграл (левые прямоугольники)")
plt.xlabel("Количество разбиений")
plt.ylabel("Значение интеграла")
plt.scatter(n_rectangles_Left, result_rectangles_Left, marker="o", color="red", label="Интеграл")
plt.axhline(y=result_rectangles_Left, color="black", linestyle="--", label="Значение интеграла")
plt.annotate(f"Шаг: {step_rectangles_Left:.4f}", xy=(n_rectangles_Left, result_rectangles_Left), xytext=(n_rectangles_Left + 10, result_rectangles_Left + 0.1), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2"))
plt.legend()

plt.figure(figsize=(8, 4))
plt.title("Интеграл (центральные прямоугольники)")
plt.xlabel("Количество разбиений")
plt.ylabel("Значение интеграла")
plt.scatter(n_rectangles_Center, result_rectangles_Center, marker="o", color="green", label="Интеграл")
plt.axhline(y=result_rectangles_Center, color="black", linestyle="--", label="Значение интеграла")
plt.annotate(f"Шаг: {step_rectangles_Center:.4f}", xy=(n_rectangles_Center, result_rectangles_Center), xytext=(n_rectangles_Center + 10, result_rectangles_Center + 0.1), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2"))
plt.legend()

plt.figure(figsize=(8, 4))
plt.title("Интеграл (правые прямоугольники)")
plt.xlabel("Количество разбиений")
plt.ylabel("Значение интеграла")
plt.scatter(n_rectangles_Right, result_rectangles_Right, marker="o", color="blue", label="Интеграл")
plt.axhline(y=result_rectangles_Right, color="black", linestyle="--", label="Значение интеграла")
plt.annotate(f"Шаг: {step_rectangles_Right:.4f}", xy=(n_rectangles_Right, result_rectangles_Right), xytext=(n_rectangles_Right + 10, result_rectangles_Right + 0.1), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2"))
plt.legend()

x = np.linspace(lowerLimit, upperLimit, 200)
y = f(x)

plt.figure(figsize=(8, 4))
plt.title("Функция f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y, color="black")

plt.tight_layout()
plt.show()
