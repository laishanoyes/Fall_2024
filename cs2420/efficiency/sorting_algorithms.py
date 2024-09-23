# sorting_algorithms.py

def bubble_sort(L):
    comparisons = 0
    changed = True
    while changed:
        changed = False
        for i in range(len(L) - 1):
            comparisons += 1
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                changed = True
    return comparisons

def shaker_sort(L):
    comparisons = 0
    changed = True
    while changed:
        changed = False
        for i in range(len(L) - 1):
            comparisons += 1
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                changed = True
        if not changed:
            break
        for i in range(len(L) - 2, -1, -1):
            comparisons += 1
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                changed = True
    return comparisons

def counting_sort(L):
    comparisons = 0
    F = [0] * (max(L) + 1)
    for i in L:
        F[i] += 1
    k = 0
    for i in range(len(F)):
        value = i
        count = F[i]
        for j in range(count):
            comparisons += 1
            L[k] = value
            k += 1
    return comparisons

def merge_sort(L):
    if len(L) <= 1:
        return 0
    half = len(L) // 2
    A = L[:half]
    B = L[half:]
    comparisons = merge_sort(A) + merge_sort(B)
    i = j = k = 0
    while i < len(A) and j < len(B):
        comparisons += 1
        if A[i] <= B[j]:
            L[k] = A[i]
            i += 1
        else:
            L[k] = B[j]
            j += 1
        k += 1
    while i < len(A):
        L[k] = A[i]
        k += 1
        i += 1
    while j < len(B):
        L[k] = B[j]
        k += 1
        j += 1
    return comparisons

def quick_sort(L, low, high):
    if high - low + 1 <= 1:
        return 0
    comparisons = 0
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        comparisons += 1
        if L[i] <= L[low]:
            L[i], L[lmgt] = L[lmgt], L[i]
            lmgt += 1
    pivotindex = lmgt - 1
    L[low], L[pivotindex] = L[pivotindex], L[low]
    comparisons += quick_sort(L, low, pivotindex - 1)
    comparisons += quick_sort(L, pivotindex + 1, high)
    return comparisons

def mod_quick_sort(L, low, high):
    if high - low + 1 <= 1:
        return 0
    comparisons = 0
    mid = (low + high) // 2
    L[low], L[mid] = L[mid], L[low]
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        comparisons += 1
        if L[i] < L[low]:
            L[i], L[lmgt] = L[lmgt], L[i]
            lmgt += 1
    pivotindex = lmgt - 1
    L[low], L[pivotindex] = L[pivotindex], L[low]
    comparisons += mod_quick_sort(L, low, pivotindex - 1)
    comparisons += mod_quick_sort(L, pivotindex + 1, high)
    return comparisons

