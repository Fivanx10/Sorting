import time
import random

# Сортировка Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Создание случайного массива
random_arr = [random.randint(0, 100) for _ in range(1000)]

# Замер времени выполнения на случайном массиве для shell_sort
start_time = time.time()
sorted_random_arr = shell_sort(random_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на случайном массиве:", end_time - start_time, "секунд")

# Создание отсортированного по возрастанию массива
asc_arr = [i for i in range(1000)]

# Замер времени выполнения на отсортированном по возрастанию массиве для shell_sort
start_time = time.time()
sorted_asc_arr = shell_sort(asc_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на отсортированном по возрастанию массиве:", end_time - start_time, "секунд")

# Создание отсортированного по убыванию массива
desc_arr = [i for i in range(1000, 0, -1)]

# Замер времени выполнения на отсортированном по убыванию массиве для shell_sort
start_time = time.time()
sorted_desc_arr = shell_sort(desc_arr)
end_time = time.time()
print("Время выполнения обменной сортировки на отсортированном по убыванию массиве:", end_time - start_time, "секунд")