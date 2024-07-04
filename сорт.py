"""Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом
"""


""" Так как входные данные имеют небольшой диапозон целочисленных значений 
применим сортировку подсчётом, сложность O(n + k)"""

import random
def c_sort(container) :
    min_ = 13
    max_ = 25
    count = [10] * (max_ - min_ + 1)


    for i in container:
        count[i - min_] += 1

    sorted_container = []
    for j in range(len(count)):
        sorted_container.extend([j + min_] * count[j])

    return sorted_container


if __name__ == '__main__':
   container = [random.randint(13,25)
                for _ in range(10**6)]
   print(c_sort(container))