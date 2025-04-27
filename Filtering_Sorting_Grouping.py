import pandas as pd;

data = pd.DataFrame({
    "Name": ["Rahim","Anna", "Michale", "Sam", "Amayaha", "Arisha", "Sohana", "Mir", "Akter", "Karim"],
    "Age": [35, 25, 28, 29, 30, 31, 32, 33, 34, 35],
    "Job": ["Engineer", "Doctor", "Teacher", "Engineer", "Doctor", "Teacher", "Engineer", "Doctor", "Teacher", "Engineer"],
    "Salary": [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"]
})

# print(data.sort_values(by="Salary", ascending=False))

# print(data.groupby("Department")["Name"].count())
# print(data.groupby("Department")["Salary"].mean())
# print(data.groupby("Department")["Salary"].mean())
# print(data.groupby("Department")["Age"].mean())


# Filtering

# print(data[data["Salary"] > 50000].sort_values(by="Salary", ascending=False))

print(data[(data["Salary"] > 50000) & (data["Salary"] < 80000)])

print("\n", data[data["Age"].isin([30,32])])
print("\n", data[data["Age"].between(20,40)].sort_values(by="Age"))