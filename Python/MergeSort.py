def merge_sort(arr):
    # The last array split
    if len(arr) <=1 :
        return arr
    
    mid=len(arr)//2

    # Perform merge sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
   
    # Merge each side together

    return merge(left, right, arr.copy())


def merge(left,right,merged):

    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):

        # Sort each one and place into the result
        if left[left_cursor]<= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor+=1
        else:
            merged[left_cursor+right_cursor]=right[right_cursor]
            right_cursor+=1
    
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor+right_cursor]=left[left_cursor]

    for right_cursor in range(right_cursor,len(right)):
        merged[left_cursor+right_cursor]=right[right_cursor]

    return merged


arr= [1,4,5,6,54,6,8,6,5,45,4084,58493,57345,5908]
print(arr)

print(merge_sort(arr))


