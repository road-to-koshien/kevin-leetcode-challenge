def mergeSort(arr): 
    print(arr)
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
        # print(L, R)

        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        
        # i = j = k = 0

        # while i < len(L) and j < len(R): 
        #     if L[i] < R[j]: 
        #         arr[k] = L[i] 
        #         i+=1
        #     else: 
        #         arr[k] = R[j] 
        #         j+=1
        #     k+=1

        # while i < len(L): 
        #     arr[k] = L[i] 
        #     i+=1
        #     k+=1
          
        # while j < len(R): 
        #     arr[k] = R[j] 
        #     j+=1
        #     k+=1
    # print(arr)

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i])
    print() 
  
if __name__ == '__main__': 
    arr = [8,7,6,5,4,3]  
    print ("Given array is", )
    # printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", )
    # printList(arr) 
  
















