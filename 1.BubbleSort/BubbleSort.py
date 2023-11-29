import time
import random

class SortInterface:
    def sort(self, arr):
        pass

class BubbleSort(SortInterface):
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

class ArrayGenerator:
    def generate_random_array(self, size):
        return [random.randint(0, 100) for _ in range(size)]

    def generate_sorted_asc_array(self, size):
        return [i for i in range(size)]

    def generate_sorted_desc_array(self, size):
        return [i for i in range(size, 0, -1)]

# Создание экземпляров классов
bubble_sort = BubbleSort()
array_generator = ArrayGenerator()

# Создание случайного массива
random_arr = array_generator.generate_random_array(1000)

# Замер времени выполнения на случайном массиве
start_time = time.time()
sorted_random_arr = bubble_sort.sort(random_arr)
end_time = time.time()
print("Время выполнения сортировки пузырьком на случайном массиве:", end_time - start_time, "секунд")

# Создание отсортированного по возрастанию массива
asc_arr = array_generator.generate_sorted_asc_array(1000)

# Замер времени выполнения на отсортированном по возрастанию массиве
start_time = time.time()
sorted_asc_arr = bubble_sort.sort(asc_arr)
end_time = time.time()
print("Время выполнения сортировки пузырьком на отсортированном по возрастанию массиве:", end_time - start_time, "секунд")

# Создание отсортированного по убыванию массива
desc_arr = array_generator.generate_sorted_desc_array(1000)

# Замер времени выполнения на отсортированном по убыванию массиве
start_time = time.time()
sorted_desc_arr = bubble_sort.sort(desc_arr)
end_time = time.time()
print("Время выполнения сортировки пузырьком на отсортированном по убыванию массиве:", end_time - start_time, "секунд")
