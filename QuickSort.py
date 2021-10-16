#Quick sort implementation in Python

def swap(i, j, A):
    if i!=j:
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

def QuickSort(A,l,h):
    if l < h:
        pi = partition(A,l,h)
        QuickSort(A,l, pi-1)
        QuickSort(A,pi+1,h)

def partition(A,l,h):
    pivot_index = l
    pivot = A[pivot_index]

    while l<h:
        while l < len(A) and A[l] <= pivot:
            l += 1
        while A[h] > pivot:
            h -= 1

        if l < h:
            swap(l,h,A)

    swap(pivot_index,h,A)
    return h


A = list(map(int,input("Enter elements with , seperation").strip().split(',')))
QuickSort(A,0,len(A)-1)
print(A)
