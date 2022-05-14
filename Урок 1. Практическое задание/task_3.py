"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
company_dict = {'Apple': 5769, 'Samsung': 4861, 'Acer': 3526, 'Starlink': 15486, 'Shrek': 999999}

# -----------------------------


def max_profit_top3(dct):  # O(n)
    new_dct = dct.copy()  # O(n)
    top3_list = []  # O(1)
    i = 0  # O(1)
    while i < 3:  # O(1)
        top3_list.append(max(new_dct.items(), key=lambda x: x[1]))  # O(n)
        new_dct.pop(top3_list[i][0])  # O(1)
        i += 1  # O(1)
    return top3_list  # O(1)


[print(*i, sep=': ') for i in max_profit_top3(company_dict)]

print('-' * 15)

top3 = sorted(company_dict.items(), key=lambda x: x[1], reverse=True)[:3]  # O(n log n)
[print(*i, sep=': ') for i in top3]
