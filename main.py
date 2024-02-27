import math


def f(x):
    return math.sqrt(x) * math.cos(x ** 2)


I = -0.5963227286825986
# Шаги разбиения
step1 = 0.1
step2 = 0.05
step3 = 0.025
step4 = 0.0125
a = 1  # Нижний предел интегрирования
b = 2  # Верхний предел интегрирования


def integral_left_rectangles(f, a, b, step):
    n = int((b - a) / step)
    integral = 0
    for i in range(n):
        integral += f(a + i * step)
    integral *= step
    return integral


def integral_trapezoid(f, a, b, step):
    n = int((b - a) / step)
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * step)
    integral *= step
    return integral


def integral_simpson(f, a, b, step):
    n = int((b - a) / step)
    integral = f(a) + f(b)
    for i in range(1, n):
        k = a + i * step
        if i % 2 == 0:
            integral += 2 * f(k)
        else:
            integral += 4 * f(k)

    integral *= step / 3
    return integral


print(f'Метод левых прямоугольников; Шаг = 0,1|   {"%.16f" % float(integral_left_rectangles(f, a, b, step1))}')
print(f'Погрешность по Рунге (метод левых)|        {"%.16f" % float(2 * abs(integral_left_rectangles(f, a, b, step1) - integral_left_rectangles(f, a, b, step2)))}')
print(f'Метод левых прямоугольников; Шаг = 0,05|  {"%.16f" % float(integral_left_rectangles(f, a, b, step2))}')
print(f'Погрешность по Рунге (метод левых)|        {"%.16f" % float(2 * abs(integral_left_rectangles(f, a, b, step2) - integral_left_rectangles(f, a, b, step3)))}')
print(f'Метод левых прямоугольников; Шаг = 0,025| {"%.16f" % float(integral_left_rectangles(f, a, b, step3))}')
print(f'Погрешность по Рунге (метод левых)|        {"%.16f" % float(2 * abs(integral_left_rectangles(f, a, b, step3) - integral_left_rectangles(f, a, b, step4)))}')
print(f'\nМетод трапеций; Шаг = 0,1|                {"%.16f" % float(integral_trapezoid(f, a, b, step1))}')
print(f'Погрешность по Рунге (метод трапеций)|     {"%.16f" % float(4 * abs(integral_trapezoid(f, a, b, step1) - integral_trapezoid(f, a, b, step2)) / 3)}')
print(f'Метод трапеций; Шаг = 0,5|                {"%.16f" % float(integral_trapezoid(f, a, b, step2))}')
print(f'Погрешность по Рунге (метод трапеций)|     {"%.16f" % float(4 * abs(integral_trapezoid(f, a, b, step2) - integral_trapezoid(f, a, b, step3)) / 3)}')
print(f'Метод трапеций; Шаг = 0,025|              {"%.16f" % float(integral_trapezoid(f, a, b, step3))}')
print(f'Погрешность по Рунге (метод трапеций)|     {"%.16f" % float(2 * abs(integral_trapezoid(f, a, b, step3) - integral_trapezoid(f, a, b, step4)))}')
print(f'\nМетод Симпсона; Шаг = 0,1|                {"%.16f" % float(integral_simpson(f, a, b, step1))}')
print(f'Погрешность по Рунге (метод Симпсона)|     {"%.16f" % float(16 * abs(integral_simpson(f, a, b, step1) - integral_simpson(f, a, b, step2)) / 15)}')
print(f'Метод Симпсона; Шаг = 0,05|               {"%.16f" % float(integral_simpson(f, a, b, step2))}')
print(f'Погрешность по Рунге (метод Симпсона)|     {"%.16f" % float(16 * abs(integral_simpson(f, a, b, step2) - integral_simpson(f, a, b, step3)) / 15)}')
print(f'Метод Симпсона; Шаг = 0,025|              {"%.16f" % float(integral_simpson(f, a, b, step3))}')
print(f'Погрешность по Рунге (метод Симпсона)|     {"%.16f" % float(16 * abs(integral_simpson(f, a, b, step3) - integral_simpson(f, a, b, step4)) / 15)}')
print(f'\nЭталонное приближенное значение: {I}')