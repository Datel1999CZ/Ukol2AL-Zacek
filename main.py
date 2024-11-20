array = [1, 78, 6, 93, 27, 89, 40, 65, 7, 23]

def bubble_sort():
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
            print(array)
    return array
print(bubble_sort())




