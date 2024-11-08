from random import randint


class QuickSort:
    def __init__(self, arr, randomized=False):
        self.arr = arr
        self.randomized = randomized

    def partition(self, low, high):
        if self.randomized:
            pivot_idx = randint(low, high)
            self.arr[low], self.arr[pivot_idx] = self.arr[pivot_idx], self.arr[low]

        pivot = self.arr[low]
        i = low + 1
        j = high

        while True:
            while i <= high and self.arr[i] <= pivot:
                i += 1
            while self.arr[j] > pivot:
                j -= 1

            if i < j:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            else:
                break

        self.arr[low], self.arr[j] = self.arr[j], self.arr[low]
        return j

    def deterministic_quick_sort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.deterministic_quick_sort(low, pivot_index)
            self.deterministic_quick_sort(pivot_index + 1, high)
        return self.arr


n = int(input("Enter the number of elements: "))
arr = list(map(int, input(f"Enter {n} elements separated by space: ").split()))

randomized = input(
    "Do you want to use randomized pivot selection? (yes/no): ").strip().lower() == "yes"

quick_sort = QuickSort(arr, randomized=randomized)
sorted_arr = quick_sort.deterministic_quick_sort(0, len(arr) - 1)

print("Sorted Array:", sorted_arr)
