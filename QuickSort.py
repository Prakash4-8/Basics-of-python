# Quick Sort
list1 = [2, 8, 7, 1, 3, 5, 6, 4, 45, 79,0]

def quickSort(list1, low, high):
    if low < high:
        q = partition(list1, low, high)
        quickSort(list1, low, q - 1)
        quickSort(list1, q + 1, high)

def partition(list1, low, high):
    x = list1[high]
    i = low - 1
    for j in range(low, high):
        if list1[j] <= x:
            i += 1
            list1[i], list1[j] = list1[j], list1[i]
    list1[i + 1], list1[high] = list1[high], list1[i + 1]
    return (i + 1)

quickSort(list1, 0, len(list1) - 1)
print(list1)