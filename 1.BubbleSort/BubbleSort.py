import time
import random
class SortInterface:
    def bubble_sort(self, arr):
        pass
class BubbleSort(SortInterface):
    def bubble_sort(self, arr):
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

sort = BubbleSort()
array_generator = ArrayGenerator()

random_arr = array_generator.generate_random_array(1000)

start_time = time.time()
sorted_random_arr = sort.bubble_sort(random_arr)
end_time = time.time()
print("Время выполнения сортировки пузырьком на случайном массиве:", end_time - start_time, "секунд")

asc_arr = array_generator.generate_sorted_asc_array(1000)

start_time = time.time()
sorted_asc_arr = sort.bubble_sort(asc_arr)
end_time = time.time()
print("Время выполнения сортировки пузырьком на отсортированном по возрастанию массиве:", end_time - start_time, "секунд")

desc_arr = array_generator.generate_sorted_desc_array(1000)

start_time = time.time()
sorted_desc_arr = sort.bubble_sort(desc_arr)
end_time = time.time()
print("Время выполнения сортировки пузырьком на отсортированном по убыванию массиве:", end_time - start_time, "секунд")

print("bubble_sort")