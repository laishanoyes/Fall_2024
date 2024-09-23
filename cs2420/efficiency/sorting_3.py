#Loop through each function
#Count compares
#for counting sort count the moves
#test on lists ranging from size 8 to size 2K by powers of two [8, 16, 31, 64, 128, 256, 512, 1k, 2k

#set recursion limit
import sys

sys.setrecursionlimit(5000)

#imports
import random
import pandas as pd
import numpy as np
from sorting_algorithms import (
        bubble_sort,
        shaker_sort,
        counting_sort,
        merge_sort,
        quick_sort,
        mod_quick_sort
)


#make a random list with the maximum number being the same size as the length of the list
def MakeRandomData(N):
    L = []
    for i in range (N):
        r = random.randrange(0,N)
        L.append(r)
    return L

#Call MakeRandomData, sort it, and switch the first and last items in order to make mostly sorted data
def MakeSortedData(N):
    ms = MakeRandomData(N)
    ms.sort()
    ms[0], ms[-1] = ms[-1], ms[0]
    return ms


def TestAlgs(new_list, sizes):
    results = {}
    for size in sizes:
        data = new_list(size)
        comparisons = {
                "BubbleSort": bubble_sort(data.copy()),
                "ShakerSort": shaker_sort(data.copy()),
                "CountingSort": counting_sort(data.copy()),
                "MergeSort": merge_sort(data.copy()),
                "QuickSort": quick_sort(data.copy(), 0, size - 1),
                "ModQuickSort": mod_quick_sort(data.copy(), 0, size - 1),
        }
        results[size] = comparisons
    return results

def RunTests_MakeTable():
    sizes = [2**i for i in range(3,13)]
    random_results = TestAlgs(MakeRandomData, sizes)
    mostly_sorted_results = TestAlgs(MakeSortedData, sizes)

    random_df = pd.DataFrame(random_results).T
    mostly_sorted_df = pd.DataFrame(mostly_sorted_results).T

    random_df.index = [i for i in range(3, 13)]
    mostly_sorted_df.index = [i for i in range(3, 13)]

    random_df_log = np.log2(random_df)
    mostly_sorted_df_log = np.log2(mostly_sorted_df)

#    random_df_log.to_excel("random_data_comparisons_log.xlsx", index=True)
#    mostly_sorted_df_log.to_excel("mostly_sorted_data_comparisons_log.xlsx", index=True)
    random_df.to_excel("random_data_comparisons.xlsx", index=True)
    mostly_sorted_df.to_excel("mostly_sorted_data_comparisons.xlsx", index=True)
RunTests_MakeTable()

















