#1.Merge Sort (Злиття)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#2.Insertion Sort (Вставки)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#Timsort
def timsort(arr):
    return sorted(arr)

#Емпіричний аналіз
import timeit
import random

# Функція для вимірювання часу виконання
def measure_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr)
    end_time = timeit.default_timer()
    return end_time - start_time

# Генерація випадкових даних
def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Розмір масивів для тестування
sizes = [100, 1000, 10000]

# Порівняння часу виконання
for size in sizes:
    data = generate_data(size)
    print(f"\nРозмір масиву: {size}")

    # Копіюємо масив для кожного сортування, щоб уникнути сторонніх впливів
    data_copy = data[:]
    time_merge_sort = measure_time(merge_sort, data_copy)
    print(f"Merge Sort: {time_merge_sort:.6f} секунд")

    data_copy = data[:]
    time_insertion_sort = measure_time(insertion_sort, data_copy)
    print(f"Insertion Sort: {time_insertion_sort:.6f} секунд")

    data_copy = data[:]
    time_timsort = measure_time(timsort, data_copy)
    print(f"Timsort (sorted): {time_timsort:.6f} секунд")

#Реалізація функції merge_k_lists

import heapq

def merge_k_lists(lists):
    min_heap = []
    for index, sorted_list in enumerate(lists):
        if sorted_list:
            heapq.heappush(min_heap, (sorted_list[0], index, 0))

    result = []
    while min_heap:
        val, list_index, element_index = heapq.heappop(min_heap)
        result.append(val)
        if element_index + 1 < len(lists[list_index]):
            heapq.heappush(min_heap, (lists[list_index][element_index + 1], list_index, element_index + 1))

    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)