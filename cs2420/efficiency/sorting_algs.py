def BubbleSort(L):
    comparisons = 0
    changed = True
    while changed:
        changed = False
        for i in range(len(L)-1):
            comparisons += 1
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                changed = True
    return comparisons

def ShakerSort(L):
    comparisons = 0
    changed = True
    while changed:
        changed = False
        for i in range (len(L)-1):
            comparisons += 1
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                changed = True
            if changed == False:
                break          
        for i in range (len(L)-2, -1, -1):
            comparisons += 1
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                changed = True
    return comparisons

def CountingSort(L):
    comparisons = 0
    F = []
    for i in range(len(L)):
        F.append(0)
    for i in L:
        F[i] += 1
    k = 0
    for i in range(len(F)):
        value = i
        count = F[i]
        for j in range(count):
            L[k] = value
            k += 1
            comparisons += 1
    return comparisons

def MergeSort(L):
    if len(L) <= 1: 
        return
    comparisons = 0
    half = len(L)//2
    A = L[:half]
    B = L[half:]
    comparisons = merge_sort(A) + merge_sort(B)
    i=j=k=0
    while i< len(A) and j < len(B):
        if A[i] <= B[j]:
            comparisons += 1
            L[k] = A[i]
            i += 1
            k += 1
        else:
            L[k] = B[j]
            j+=1
            k+=1
    while i < len(A):
        L[k] = A[i]
        k+=1
        i+=1
    while j < len(B):
        L[k] = B[j]
        k+=1
        j+=1
    return comparisons

def QuickSort(L, low, high):
    if high-low + 1 <=1:
        return
    comparisons = 0
    lmgt = low + 1
    for i in range(low+1, high+1):
        if L[i] <= L[low]:
            comparisons += 1
            L[i], L[lmgt] = L[lmgt], L[i]
            lmgt += 1
    pivotindex = lmgt-1
    L[low], L[pivotindex] = L[pivotindex], L[low]
    comparisons += QuickSort(L, low, pivotindex-1)
    comparisons += QuickSort(L, pivotindex+1, high)
    return comparisons

def ModQuickSort(L, low, high):
    if high-low +1 <= 1:
        return
    comparisons = 0
    mid = (low+high)//2
    L[low], L[mid] = L[mid], L[low]
    lmgt = low+1
    for i in range(low+1, high+1):
        comparisons += 1
        if L[i] < L[low]:
            L[i], L[lmgt] = L[lmgt], L[i]
            lmgt += 1
    pivotindex = lmgt - 1
    L[low], L[pivotindex] = L[pivotindex], L[low]
    comparisons += ModQuickSort(L, low, pivotindex-1)
    comparisons += ModQuickSort(L, pivotindex + 1, high)
    return comparisons 
