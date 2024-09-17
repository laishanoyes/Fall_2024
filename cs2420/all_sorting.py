#import random module
import random

#Create Bubble Sort function
def BubbleSort(L):
    changed = True
    while changed:
#make changed = False so that if nothing changed the for loop stops
        changed = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
#Make changed = True so that the for loop goes again
                changed = True

#Create Shaker Sort function
def ShakerSort(L):
    changed = True
    while changed:
        changed = False
#go through the list forward
        for i in range (len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                changed = True
#stop the loop if nothing changes going forward as that means that there is nothing left to sort and it does not need to go backwards
            if changed == False:
                break
#Go through the list backwards            
        for i in range (len(L)-2, -1, -1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                changed = True
#Create Counting Sort function, which counts how many of each number there are and adds that number to a new list
def CountingSort(L):
#Creat an empty list
    F = []
#Add as many zeros to that list for the length of the original list
    for i in range(len(L)):
        F.append(0)
    for i in L:
        F[i] += 1
    k = 0
    for i in range(len(F)):
#Switch the value and the index
        value = i
        count = F[i]
        for j in range(count):
            L[k] = value
            k += 1
#Create Merge Sort function
def MergeSort(L):
    if len(L) <= 1: 
        return
    half = len(L)//2
    A = L[:half]
    B = L[half:]
    MergeSort(A)
    MergeSort(B)
    i=j=k=0
    while i< len(A) and j < len(B):
        if A[i] <= B[j]:
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

#Create Quick Sort function
def QuickSort(L, low, high):
    if high-low + 1 <=1:
        return
    lmgt = low + 1
    for i in range(low+1, high+1):
        if L[i] <= L[low]:
            L[i], L[lmgt] = L[lmgt], L[i]
            lmgt += 1
    pivotindex = lmgt-1
    L[low], L[pivotindex] = L[pivotindex], L[low]
    QuickSort(L, low, pivotindex-1)
    QuickSort(L, pivotindex+1, high)

#Create Modified Quick Sort function, which counts how many of each number there are and adds that number to a new list
def ModQuickSort(L, low, high):
    if high-low +1 <= 1:
        return
    mid = (low+high)//2
    L[low], L[mid] = L[mid], L[low]

    lmgt = low+1
    for i in range(low+1, high+1):
        if L[i] < L[low]:
            L[i], L[lmgt] = L[lmgt], L[i]
            lmgt += 1
    pivotindex = lmgt - 1
    L[low], L[pivotindex] = L[pivotindex], L[low]
    ModQuickSort(L, low, pivotindex-1)
    ModQuickSort(L, pivotindex + 1, high)

#Create a random list function that only has values that go up to the length of the list(this is important for the counting sorter as negative and too large of values will mess this up with the current code
def CreateRandomList(N):
    L = []
    for i in range (N):
        r = random.randrange(0,N)
        L.append(r)
    return L

def main():
#Test Bubble sort
    L = CreateRandomList(10)
    L1 = L[:]
    L2 = L[:]
    BubbleSort(L1)
    L2.sort()
    if L1 != L2:
        print("The Bubble sorter is not working properly", L, L1, L2)
    else:
        print("List sorted correctly \nOriginal list: ", L, "\nBubble sorted list: ", L1)

# Test Shaker sort
    L = CreateRandomList(10)
    L1 = L[:]
    L2 = L[:]
    ShakerSort(L1)
    L2.sort()
    if L1 != L2:
        print ("The Shaker sorter is not working properly", L, L1, L2)
    else:
        print("List sorted correctly \nOriginal list: ", L, "\nShaker sorted list: ", L1)

#Test Counting sort
    L = CreateRandomList(10)
    L1 = L[:]
    L2 = L[:]
    CountingSort(L1)
    L2.sort()
    if L1 != L2:
        print("The counting sorter is not working porperly")
    else:
        print("List sorted correctly \nOriginal list: ", L, "\nCounting sorted list: ", L1)
        
#Test Merge sort
    L = CreateRandomList(10)
    L1 = L[:]
    L2 = L[:]
    MergeSort(L1)
    L2.sort()
    if L1 != L2:
        print("The Merge sorter is not working properly", L, L1, L2)
    else:
        print("List sorted correctly \nOriginal list: ", L, "\nMerge sorted list: ", L1)

# Test Quick sort
    L = CreateRandomList(10)
    L1 = L[:]
    L2 = L[:]
    QuickSort(L1, 0, len(L1)-1)
    L2.sort()
    if L1 != L2:
        print ("The Quick sorter is not working properly", L, L1, L2)
    else:
        print("List sorted correctly \nOriginal list: ", L, "\nQuick sorted list: ", L1)

#Test Mofified Quick sort
    L = CreateRandomList(10)
    L1 = L[:]
    L2 = L[:]
    ModQuickSort(L1, 0, len(L1)-1)
    L2.sort()
    if L1 != L2:
        print("The Modified Quick sorter is not working porperly")
    else:
        print("List sorted correctly \nOriginal list: ", L, "\nModified Quick sorted list: ", L1)

#Call main
if __name__ == '__main__':
    main()
