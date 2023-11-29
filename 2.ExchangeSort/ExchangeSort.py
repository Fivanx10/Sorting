import time
import random

# Сортировка обменом
def exchange_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Создание случайного массива
random_arr = [random.randint(0, 100) for _ in range(1000)]

# Замер времени выполнения на случайном массиве для exchange_sort
start_time = time.time()
sorted_random_arr = exchange_sort(random_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на случайном массиве:", end_time - start_time, "секунд")

# Создание отсортированного по возрастанию массива
asc_arr = [i for i in range(1000)]

# Замер времени выполнения на отсортированном по возрастанию массиве для exchange_sort
start_time = time.time()
sorted_asc_arr = exchange_sort(asc_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на отсортированном по возрастанию массиве:", end_time - start_time, "секунд")

# Создание отсортированного по убыванию массива
desc_arr = [i for i in range(1000, 0, -1)]

# Замер времени выполнения на отсортированном по убыванию массиве для exchange_sort
start_time = time.time()
sorted_desc_arr = exchange_sort(desc_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на отсортированном по убыванию массиве:", end_time - start_time, "секунд")