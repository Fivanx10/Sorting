class CustomArray:
    def __init__(self, arr):
        self.arr = arr

    def merge_sort(self):
        if len(self.arr) > 1:
            mid = len(self.arr) // 2
            L = CustomArray(self.arr[:mid])
            R = CustomArray(self.arr[mid:])
            L.merge_sort()
            R.merge_sort()
            i = j = k = 0
            while i < len(L.arr) and j < len(R.arr):
                if L.arr[i] < R.arr[j]:
                    self.arr[k] = L.arr[i]
                    i += 1
                else:
                    self.arr[k] = R.arr[j]
                    j += 1
                k += 1
            while i < len(L.arr):
                self.arr[k] = L.arr[i]
                i += 1
                k += 1
            while j < len(R.arr):
                self.arr[k] = R.arr[j]
                j += 1
                k += 1

# Пример использования
custom_array = CustomArray([3, 1, 4, 2])
custom_array.merge_sort()
print(custom_array.arr)
