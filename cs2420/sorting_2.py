#import random module
import random

#Create Merge Sort function
def MergeSort(L):
	pass

#Create Quick Sort function
def QuickSort(L):
    pass

#Create Modified Quick Sort function, which counts how many of each number there are and adds that number to a new list
def ModQuickSort(L):
	pass

#Create a random list function that only has values that go up to the length of the list(this is important for the counting sorter as negative and too large of values will mess this up with the current code
def CreateRandomList(N):
    L = []
    for i in range (N):
        r = random.randrange(0,N)
        L.append(r)
    return L

def main():
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
    QuickSort(L1)
    L2.sort()
    if L1 != L2:
        print ("The Quick sorter is not working properly", L, L1, L2)
    else:
        print("List sorted correctly \nOriginal list: ", L, "\nQuick sorted list: ", L1)

#Test Mofified Quick sort
    L = CreateRandomList(10)
    L1 = L[:]
    L2 = L[:]
    ModQuickSort(L1)
    L2.sort()
    if L1 != L2:
        print("The Modified Quick sorter is not working porperly")
    else:
        print("List sorted correctly \nOriginal list: ", L, "\nModigied Quick sorted list: ", L1)

#Call main
if __name__ == '__main__':
    main()
