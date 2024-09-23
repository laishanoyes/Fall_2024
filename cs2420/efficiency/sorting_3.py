#create random list
#create mostly sorted list 
#sys.setrecursionlimit(5000)
#Loop through each function
#Count compares
#for counting sort count the moves
#test on lists ranging from size 8 to size 2K by powers of two [8, 16, 31, 64, 128, 256, 512, 1k, 2k


#imports
import random
#make a random list with the maximum number being the same size as the length of the list
def MakeRandomData(N):
    L = []
    for i in range (N):
        r = random.randrage(0,N)
        L.append(r)
    return L




def MakeSortedData(N):
    ms = MakeRandomData(N):
    ms.sort()
    ms[0], ms[-1] = ms[-1], ms[0]
    return ms
