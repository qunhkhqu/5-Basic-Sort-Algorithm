def partition(array, begin, end):
    pivot_idx=begin

    for i in range(begin+1,end+1):
        pivot_idx+=1
        array[i],array[pivot_idx]=array[pivot_idx],array[i]
        
    array[pivot_idx], array[begin]=array[begin], array[pivot_idx]

    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin>=end:
        return
     
    pivot_idx=partition(array,begin,end)

    quick_sort_recursion(array,begin,pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) -1
        
    quick_sort_recursion(array, begin, end)


arr= [1,4,5,6,54,6,8,6,5]
print(arr)

quick_sort(arr)
print(arr)