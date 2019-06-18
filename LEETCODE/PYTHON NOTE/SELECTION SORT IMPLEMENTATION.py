#Implementation of selection sort
def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return arr

a = [1,5,4,2,3]
print(selection_sort(a))
        
            