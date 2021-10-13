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


arr= [1,4,5,6,54,6,8,6,5]

print(arr)

print(selection_sort(arr))

print(arr)