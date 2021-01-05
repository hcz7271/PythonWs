from random import randint

list_numbers = randint(5, 6)


def random_list(count):
    ls = []
    for i in range(0, count, 1):
        ls.append(randint(0, 10000))
    return ls


def partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:

            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # 返回pivit的索引值
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        print(arr)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test above
# arr1 = random_list(list_numbers)
arr1 = [5293, 2152, 4995, 7349, 7747, 6778]
print(arr1)
quickSort(arr1, 0, len(arr1) - 1)

"""
arr = [5293, 2152, 4995, 7349, 7747, 6778]
quickSort(arr=[5293, 2152, 4995, 7349, 7747, 6778],low=0,high=len(arr)-1=5)
    if low=0 < high=5 : True
        pi = partition(arr=[5293, 2152, 4995, 7349, 7747, 6778], low=0, high=5)
            i = low-1 = -1
            pivot = arr[high] = 6778
            for j in range(low=0,high=5):
                # j=0
                if arr[j]=5293 < pivot=6778: True
                    i = i+1 = -1+1 = 0
                    arr[i=0], arr[j=0] = arr[j], arr[i]
                [5293(i,j), 2152, 4995, 7349, 7747, 6778(pivot)]
                
                # j=1
                if arr[j=1]=2152 < pivot=6778: True
                    i+1 = 1
                    arr[j] = arr[i] remain the same
                [5293, 2152(i,j), 4995, 7349, 7747, 6778(pivot)]
                
                # j=2
                i=2
                [5293, 2152, 4995(i,j), 7349, 7747, 6778(pivot)]
                
                # j=3
                if arr[j]=7349 < pivot: False
                i=2
                [5293, 2152, 4995(i), 7349(j), 7747, 6778(pivot)]

                # j=4
                if arr[j]=7747 < pivot: False
                i=2
                [5293, 2152, 4995(i), 7349, 7747(j), 6778(pivot)]
            i=2
            arr[i+1=3], arr[high=5] = 6778,7349 调换pivot
            [5293, 2152, 4995, *6778, 7747, *7349]
            return i+1=3
        pi = 3
        quickSort(arr=[5293, 2152, 4995, *6778, 7747, *7349], low=0, high=pi-1=2)
            if low=0 < high=2 : True
                pi = partition(arr, low=0, high=2)
                    i = -1
                    pivot = arr[high] = 4995
                    [5293, 2152, 4995(pivot), *6778, 7747, *7349]
                    for j in range(0,2):
                        #j=0
                        if arr[j]=5293 < pivot=4995: False
                        [5293(j), 2152, 4995(pivot), *6778, 7747, *7349]
                        
                        #j=1
                        if arr[j]=2152 < pivot: True
                            i=0
                            arr[i=0], arr[j=1] = 2152, 5293
                        [2152(i), 5293(j), 4995(pivot), *6778, 7747, *7349]
                    i=0
                    arr[i+1=1] <-> arr[high=2]
                    [2152, **4995(pivot), **5293, *6778, 7747, *7349]
                    return 1
                pi = 1
                quickSort([2152, **4995, **5293, *6778, 7747, *7349],low=0,high=0)
                    if low<high: False
                quickSort([2152, **4995, **5293, *6778, 7747, *7349],low=2,high=2)
                    if low<high: False
        quickSort(arr=[2152, **4995, **5293, *6778, 7747, *7349],low=4,high=5)
            if low<high : True
                pi = partition(arr,low=4,high=5)
                    i = low-1 = 3
                    pivot = arr[high=5] = 7349
                    [2152, **4995, **5293, *6778(i), 7747(j), *7349(pivot)]
                    for j in range(4,5):
                        #j=4
                        if arr[j]=7747 < pivot=7349: False
                    arr[i+1=4] <-> arr[high=5]
                    [2152, **4995, **5293, *6778, *7349(pivot)***, ***7747]
                    return i+1=4
                pi=4
                ......
        ...
                                    
            


"""
