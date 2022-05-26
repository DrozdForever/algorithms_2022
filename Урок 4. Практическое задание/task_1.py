"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


num = [i for i in range(100)]

print(timeit('func_1(num)', 'from __main__ import func_1, num', number=10000))  # 0.63
print(timeit('func_2(num)', 'from __main__ import func_2, num', number=10000))  # 0.53

# Использовал list comprehension, что позволило ускорить код на 0.1 с.
