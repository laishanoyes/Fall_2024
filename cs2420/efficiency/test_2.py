import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ... (Your sorting functions and data generation functions remain unchanged)

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

