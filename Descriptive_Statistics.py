import numpy as np
import pandas as pd

# data_csv = pd.read_csv("percent_bachelors_degrees_women_usa.csv")

# data = [100, 20, 5, 40, 5, -100, 49]
# mean_ = np.mean(data)
# median_ = np.median(data)

# from scipy import stats
# mode_ = stats.mode(data)

# print("-==================== Statistics ====================-\n")
# print(f"Mean: {mean_}\nMedian: {median_}\nMode: {mode_[0]}")

# print("\n-==================== Variance & Standard Deviation ====================-\n")
# variance_ = np.var(data)
# std_ = np.std(data)
# print(f"Variance: {variance_}\nStandard Deviation: {std_}")


data_csv = pd.read_csv("percent_bachelors_degrees_women_usa.csv")
print(data_csv.describe())