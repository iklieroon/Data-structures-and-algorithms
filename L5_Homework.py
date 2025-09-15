def bubble_sort(array):
    len_array=len(array)
    for i in range(len_array):
        swap=False
        for j in range(0,len_array-i-1):
            if array[j]<array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                swap=True
        if not swap:
            break
    return array

print(bubble_sort([1,2,3,4,5,6,7,8,9,67]))

def insertion_sort(array):
    for i in range(1,len(array)):
        c=array[i]
        j=i-1
        while j>=0 and array[j]<c:
            array[j+1]=array[j]
            j-=1
        array[j+1]=c
    return array

print(insertion_sort([1,2,3,4,5,6,7,8,9,67]))