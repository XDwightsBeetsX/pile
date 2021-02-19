"""
File with common sorting methods
"""

def bubble_sort(arr):
    """
    Bubble sort iteratively swaps two elements until sorted
    """
    l = len(arr)
    if l == 0:
        # treat arr of len 0 as sorted
        return arr
    
    for i in range(l):
        madeSwap = False
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                madeSwap = True
        if madeSwap == False:
            break
    
    return arr


def selection_sort(arr):
    """
    Selection sort repeatedly finds the minimum and moves it to the front
    """
    l = len(arr)
    if l == 0:
        return arr
    
    for i in range(l):
        min_i = i
        for j in range(i+1, l):
            if arr[j] < arr[min_i]:
                min_i = j
        temp = arr[i]
        arr[i] = arr[min_i]
        arr[min_i] = temp
    
    return arr


def insertion_sort(arr): 
    """
    Insertion sort iteratively takes the next element in arr
    and moves backward, placing it in the correct position
    """
    for i in range(1, len(arr)): 
        curr = arr[i]
        j = i-1
        while j >= 0 and curr < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = curr
    
    return arr


def merge_sort(arr):
    """
    Merge sort repeatedly divides the arr then
    recombines the parts in sorted order
    """
    l = len(arr)
    if l > 1:
        mid = l//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


def counting_sort(arr, element_range):
    """
    Sorts array by counting element frequencies

    range is expected to be [lower, upper] such as [0, 9]
    """
    l = len(arr)
    element_range_count = element_range[1] - element_range[0] + 1
    output = [0] * l
    count = [0] * element_range_count

    for i in range(0, l):
        count[arr[i]] += 1

    for i in range(1, element_range_count):
        count[i] += count[i - 1]

    i = l - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, l):
        arr[i] = output[i]
    
    return arr


def quick_sort(arr):
    """
    Breaks down array into smaller sections
    then swaps subsections into order

    uses local partition() and sub_quick_sort(),
    which assumes whole array should be sorted
    """
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] < pivot: 
                i += 1 
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]

        return i + 1
    
    def sub_quick_sort(arr, low, high):
        if low < high:
            p = partition(arr, low, high)
            sub_quick_sort(arr, low, p - 1)
            sub_quick_sort(arr, p + 1, high)
    
    l = 0
    h = len(arr) - 1
    sub_quick_sort(arr, l, h)
    
    return arr


arr = [1, 3, 5, 2, 6, 9]
print(bubble_sort(arr))
print(selection_sort(arr))
print(insertion_sort(arr))
print(merge_sort(arr))
print(counting_sort(arr, [0, 9]))
print(quick_sort(arr))
