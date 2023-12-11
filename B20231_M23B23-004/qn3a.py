#design and run 2 sorting algorithms of your choice that sorts the list,unsorted_list = [14, 27, 8,-42, 11, 35,-9,56,23]
#and provide the complexity class(as a python comment) of the implemented algorithms


#BUBBLE SORT

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]




#usage for Bubble Sort
unsorted_list = [14, 27, 8, -42, 11, 35, -9, 56, 23]
bubble_sort(unsorted_list)
print("Sorted list using Bubble Sort:", unsorted_list)


# Time Complexity is O(n^2) which is Quadratic