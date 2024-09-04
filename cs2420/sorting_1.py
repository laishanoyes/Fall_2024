
import random

def BubbleSort(L):
	sorted = True
	while sorted == True:
		sorted = False
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				L[i], L[i+1] = L[i+1], L[i]
				sorted = True

def ShakerSort(L):
	sorted = True
	while sorted == True:
		sorted == False
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				L[i], L[i+1] = L[i+1], L[i]
				sorted = True
				if sorted == True:
					break

		for i in range(len(L)-2, -1, -1):
			if L[i] > L[i+1]:
				L[i], L[i+1] = L[i+1], L[i]
				sorted = True

def CountingSort(L):
	F=[]
	for i in range(len(L)):
		F.append(0)
	for i in L:
		F[i] += 1
	K = 0
	for i in range(len(F)):
		value = i
		count = F[i]
		for j in range(count):
			L[K] = value
			K += 1

def CreateRandomList(N):
	L = []
	for i in range(N):
		r = random.randrange(0,N)
		L.append(r)
	return L

def main():
	L = CreateRandomList(10)
	L1 = L[:]
	L2 = L[:]
	BubbleSort(L1)
	L2.sort()
	if L1 != L2:
		print("The Bubble sorter is not working properly")
	elif L1 == L2:
		print("List sorted correctly \nOriginal list: ", L, "\nBubble sorted list: ", L1)
	L = CreateRandomList(10)
	L1 = L[:]
	L2 = L[:]
	ShakerSort(L1)
	L2.sort()
	if L1 != L2:
		print("The Shaker sorter is not working properly")
	elif L1 == L2:
		print("List sorted correctly \nOriginal list: ", L, "\nShaker sorted list: ", L1)
	L = CreateRandomList(10)
    L1 = L[:]
    L2 = L[:]
    CountingSort(L1)
    L2.sort()
    if L1 != L2:
		print("The Counting sorter is not working properly")
    elif L1 == L2:
		print("List sorted correctly \nOriginal list: ", L, "\nCounting sorted list: ", L1)

if __name__ == '__main__':
	main()
