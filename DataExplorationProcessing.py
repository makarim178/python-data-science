import pandas as pd
data_csv = pd.read_csv('percent_bachelors_degrees_women_usa.csv')

# print(data_csv.head(5))
# print(data_csv.tail(5))
# print(data_csv.info())


# data_csv.dropna()

print(data_csv.iloc[10])
# loc is for string indexing
# print(data_csv.loc[])