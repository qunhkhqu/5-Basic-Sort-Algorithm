def selection_sort(arr):

    for i in range(len(arr)):
        minimum=i

        for j in range(i+1,len(arr)):
            #Select the smallest value
            if arr[j] < arr[minimum]:
                minimum=j
                
        #Place it the front of the
        #Sorted end of the array
        arr[minimum],arr[i]=arr[i],arr[minimum]
    
    return arr