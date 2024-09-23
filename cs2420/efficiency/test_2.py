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
            "CountingSort":counting_sort(data.copy()),
            "MergeSort": merge_sort(data.copy()),
            "QuickSort": quick_sort(data.copy(), 0, size - 1),
            "ModQuickSort": mod_quick_sort(data.copy(), 0, size - 1),
        }
        results[size] = comparisons
    return results

def run_tests_and_plot():
    sizes = [2**i for i in range(3, 12)]  # Problem sizes: 8, 16, 32, ..., 2048
    random_results = test_sorting_algorithms(make_random_data, sizes)
    mostly_sorted_results = test_sorting_algorithms(make_mostly_sorted_data, sizes)

    # Convert results to DataFrames
    random_df = pd.DataFrame(random_results).T
    mostly_sorted_df = pd.DataFrame(mostly_sorted_results).T

    # Change the index to the exponent values
    random_df.index = [i for i in range(3, 12)]  # Corresponding to 2^3, 2^4, ..., 2^11
    mostly_sorted_df.index = [i for i in range(3, 12)]

    # Log-transform the data for plotting and export
    random_df_log = np.log(random_df)
    mostly_sorted_df_log = np.log(mostly_sorted_df)
    try:
    # Save log-transformed data to Excel
        random_df_log.to_excel("random_data_comparisons_log.xlsx", index=True)
        mostly_sorted_df_log.to_excel("mostly_sorted_data_comparisons_log.xlsx", index=True)
    except Exception as e:
        print(f"error saving Excel files: {e}:")
run_tests_and_plot()
