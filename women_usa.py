import pandas as pd

# Read the CSV file into a DataFrame: data_csv
data_csv = pd.read_csv("percent_bachelors_degrees_women_usa.csv")

# Print the output of head() method
# print(data_csv)

# Read the first 5 lines of the file into a DataFrame: data
print(data_csv.head())
# print(data_csv.head(5))

# Read the last 5 lines of the file into a DataFrame: data
# print(data_csv.tail(5))

# Read Information
#print(data_csv.info())


#print(data_csv.dropna())
#print(data_csv.fillna('NULL'))

#print(data_csv.isnull())

#print(data_csv.isnull().sum())

#print(data_csv.drop_duplicates())

# print(data_csv.iloc[10])



