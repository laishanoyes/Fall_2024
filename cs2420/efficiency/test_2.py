import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sorting_algorithms import (
    bubble_sort,
    shaker_sort,
    counting_sort,
    merge_sort,
    quick_sort,
    mod_quick_sort
)

# Generate random data
def make_random_data(size):
    return [random.randint(0, 1000) for _ in range(size)]

# Generate mostly sorted data
def make_mostly_sorted_data(size):
    data = make_random_data(size)
    data.sort()
    data[0], data[-1] = data[-1], data[0]  # Swap first and last
    return data

# Test all sorting algorithms
def test_sorting_algorithms(data_generator, sizes):
    results = {}
    for size in sizes:
        data = data_generator(size)
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

def run_tests_and_plot():
    sizes = [2**i for i in range(3, 12)]  # From 8 to 2048
    random_results = test_sorting_algorithms(make_random_data, sizes)
    mostly_sorted_results = test_sorting_algorithms(make_mostly_sorted_data, sizes)

    # Convert results to DataFrames
    random_df = pd.DataFrame(random_results).T
    mostly_sorted_df = pd.DataFrame(mostly_sorted_results).T

    # Log-transform the data for plotting and export
    random_df_log = np.log(random_df)
    mostly_sorted_df_log = np.log(mostly_sorted_df)

    # Plotting
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    for col in random_df_log.columns:
        plt.plot(random_df_log.index, random_df_log[col], label=col)
    plt.title("Random Data: Log(Problem Size) vs Log(Comparisons)")
    plt.xlabel("Log(Problem Size)")
    plt.ylabel("Log(Comparisons)")
    plt.legend()

    plt.subplot(1, 2, 2)
    for col in mostly_sorted_df_log.columns:
        plt.plot(mostly_sorted_df_log.index, mostly_sorted_df_log[col], label=col)
    plt.title("Mostly Sorted Data: Log(Problem Size) vs Log(Comparisons)")
    plt.xlabel("Log(Problem Size)")
    plt.ylabel("Log(Comparisons)")
    plt.legend()

    plt.tight_layout()
    plt.savefig("sorting_algorithms_performance.png")
    plt.show()

    # Save log-transformed data to Excel
    random_df_log.to_excel("random_data_comparisons_log.xlsx", index=True)
    mostly_sorted_df_log.to_excel("mostly_sorted_data_comparisons_log.xlsx", index=True)

run_tests_and_plot()
