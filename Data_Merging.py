import pandas as pd
# Creating 2 Dataframes
data1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value': [1, 2, 3, 4]
})
data2 = pd.DataFrame({
    'key': ['C', 'D', 'E', 'F', 'G', 'H'],
    'value': [8, 9, 10, 11, 12, 13]
})

# print(data1)
# print(data2)

# merge_innerjoin = pd.merge(data1, data2, on='key', how='inner')
# print(merge_innerjoin)
# merge_leftjoin = pd.merge(data1, data2, on='key', how='left')
# print(merge_leftjoin)
# merge_rightjoin = pd.merge(data1, data2, on='key', how='right')
# print(merge_rightjoin)

# merged_left_anti = pd.merge(data1, data2, on='key', how='left', indicator=True)

# merged_left_anti = merged_left_anti[merged_left_anti['_merge'] == 'left_only']
# merged_left_anti = merged_left_anti.drop(['_merge'], axis=1)
# merged_left_anti = merged_left_anti.drop(['value_y'], axis=1)
# print(merged_left_anti)

merged_right_anti = pd.merge(data1, data2, on='key', how='right', indicator=True)
merged_right_anti = merged_right_anti[merged_right_anti['_merge'] == 'right_only']
merged_right_anti = merged_right_anti.drop(['_merge'], axis=1)
merged_right_anti = merged_right_anti.drop(['value_x'], axis=1)
print(merged_right_anti)
