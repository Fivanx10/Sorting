import time
import random

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Создание случайного массива
random_arr = [random.randint(0, 100) for _ in range(1000)]

# Замер времени выполнения на случайном массиве для quick_sort
start_time = time.time()
sorted_random_arr = quick_sort(random_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на случайном массиве:", end_time - start_time, "секунд")

# Создание отсортированного по возрастанию массива
asc_arr = [i for i in range(1000)]

# Замер времени выполнения на отсортированном по возрастанию массиве для quick_sort
start_time = time.time()
sorted_asc_arr = quick_sort(asc_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на отсортированном по возрастанию массиве:", end_time - start_time, "секунд")

# Создание отсортированного по убыванию массива
desc_arr = [i for i in range(1000, 0, -1)]

# Замер времени выполнения на отсортированном по убыванию массиве для quick_sort
start_time = time.time()
sorted_desc_arr = quick_sort(desc_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на отсортированном по убыванию массиве:", end_time - start_time, "секунд")