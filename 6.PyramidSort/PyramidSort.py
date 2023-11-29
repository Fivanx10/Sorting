import time
import random

# Пирамидальная сортировка
def pyramid(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        pyramid(arr, n, largest)

def pyramid_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        pyramid(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        pyramid(arr, i, 0)
    return arr

# Создание случайного массива
random_arr = [random.randint(0, 100) for _ in range(1000)]

# Замер времени выполнения на случайном массиве для pyramid_sort
start_time = time.time()
sorted_random_arr = pyramid_sort(random_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на случайном массиве:", end_time - start_time, "секунд")

# Создание отсортированного по возрастанию массива
asc_arr = [i for i in range(1000)]

# Замер времени выполнения на отсортированном по возрастанию массиве для pyramid_sort
start_time = time.time()
sorted_asc_arr = pyramid_sort(asc_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на отсортированном по возрастанию массиве:", end_time - start_time, "секунд")

# Создание отсортированного по убыванию массива
desc_arr = [i for i in range(1000, 0, -1)]

# Замер времени выполнения на отсортированном по убыванию массиве для pyramid_sort
start_time = time.time()
sorted_desc_arr = pyramid_sort(desc_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на отсортированном по убыванию массиве:", end_time - start_time, "секунд")