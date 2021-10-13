
def swap(arr,i,j):
        arr[i],arr[j]=arr[j],arr[i]
        return

def bubble_sort(arr):

    n=len(arr)
    swapped=True
    x=-1

    while swapped:
        swapped=False
        x=x+1
        print("Vong:")
        print(x)
        for i in range(1,n-x):
            if arr[i-1]>arr[i]:
                swap(arr,i-1,i)
                swapped=True
                print(arr)
    return arr


arr= [1,4,5,6,54,6,8,6,5]

print(arr)

print(bubble_sort(arr))

print(arr)