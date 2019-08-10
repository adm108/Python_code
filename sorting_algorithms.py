""" Four most popular types of sorting algorithms below! """

import random
import time


# ------------------------------- BUBBLE SORT --------------------------------

def bubble_sort(lst):
    x = len(lst) - 1
    for j in range(0, len(lst) - 1):
        check_for_swap = False
        for i in range(0, x):
            if lst[i] > lst[i + 1]:
                swap = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = swap
                check_for_swap = True
        if check_for_swap is False:
            break
        else:
            x = x - 1
    return lst


# ----------------------------- SELECTION SORT ------------------------------

def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


# ------------------------------- INSERT SORT -------------------------------

def insert_sort(numbers):
    x = len(numbers)
    for i in range(1, x):
        j = i - 1
        while numbers[j] > numbers[j + 1] and j >= 0:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            j = j - 1
    return numbers


# -------------------------------- QUICK SORT --------------------------------

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    smaller, equal, larger = [], [], []
    pivot = numbers[-1]
    for element in numbers:
        if element > pivot:
            larger.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            smaller.append(element)
    return quick_sort(smaller) + equal + quick_sort(larger)


example_list = [random.randint(0, 10000) for i in range(0, 10000)]

t1 = time.process_time()
bubble_sort(example_list)
t2 = time.process_time()
print(f"Time of the bubble sort is: {t2 - t1}")
#
# t3 = time.process_time()
# selection_sort(example_list)
# t4 = time.process_time()
# print(f"Time of the selection sort is: {t4 - t3}")
#
# t5 = time.process_time()
# insert_sort(example_list)
# t6 = time.process_time()
# print(f"Time of the insert sort is: {t6 - t5}")

# t7 = time.process_time()
# quick_sort(example_list)
# t8 = time.process_time()
# print(f"Time of the quick sort is: {t8 - t7}")
