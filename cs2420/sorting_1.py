#import random module
import random

#Create Bubble Sort function
def BubbleSort(L):
    sorted = True
    while sorted:
#make sorted = False so that if nothing changed the for loop stops
        sorted = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
#Make sorted = True so that the for loop goes again
                sorted = True

#Create Shaker Sort function
def ShakerSort(L):
    sorted = True
    while sorted:
        sorted = False
#go through the list forward
        for i in range (len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                sorted = True
#stop the loop if nothing changes going forward as that means that there is nothing left to sort and it does not need to go backwards
            if sorted == False:
                break
#Go through the list backwards            
        for i in range (len(L)-2, -1, -1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                sorted = True
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

#Call main
if __name__ == '__main__':
    main()
