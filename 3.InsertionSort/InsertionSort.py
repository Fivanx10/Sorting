import time
import random

# Сортировка вставками
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Создание случайного массива
random_arr = [random.randint(0, 100) for _ in range(1000)]

# Замер времени выполнения на случайном массиве для insertion_sort
start_time = time.time()
sorted_random_arr = insertion_sort(random_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на случайном массиве:", end_time - start_time, "секунд")

# Создание отсортированного по возрастанию массива
asc_arr = [i for i in range(1000)]

# Замер времени выполнения на отсортированном по возрастанию массиве для insertion_sort
start_time = time.time()
sorted_asc_arr = insertion_sort(asc_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на отсортированном по возрастанию массиве:", end_time - start_time, "секунд")

# Создание отсортированного по убыванию массива
desc_arr = [i for i in range(1000, 0, -1)]

# Замер времени выполнения на отсортированном по убыванию массиве для insertion_sort
start_time = time.time()
sorted_desc_arr = insertion_sort(desc_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на отсортированном по убыванию массиве:", end_time - start_time, "секунд")