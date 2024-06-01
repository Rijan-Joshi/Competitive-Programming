import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

file_path= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"
df = pd.read_csv(file_path, header = 0)

#Task 1: Identifying the column with the missing value
missing_data = df.isnull()

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

#Task 2: Replace with Mean
mean_weight = df['Weight_kg'].astype(float).mean()
# df['Weight_kg'].replace(np.nan,mean_weight, inplace = True)
#Recommended Method
df.replace({'Weight_kg' : {np.nan: mean_weight}}, inplace= True)

print(df.head(20))

#Task 3: Replacing the missing value with the most frequent value
frequent_value = df['Screen_Size_cm'].value_counts().idxmax()
print("Frequent value: ", frequent_value)
df.replace({'Screen_Size_cm': {np.nan : frequent_value}}, inplace= True)

#Task 4: 
df[['Weight_kg', 'Screen_Size_cm']]=df[['Weight_kg', 'Screen_Size_cm']].astype(float)

#Data Standardization
df["Weight_kg"] = df["Weight_kg"] * 2.205
df.rename(columns ={"Weight_kg": "Weight_lbs"}, inplace = True)


#Data Normalization
df['CPU_frequency'] = df['CPU_frequency']/df["CPU_frequency"].max()

bins = np.linspace(min(df['Price']), max(df['Price']), 4)
group_names = ["Low", "Medium", "High"]
df['Price-binned'] = pd.cut(df['Price'], bins, labels = group_names, include_lowest=True )

plt.bar(group_names, df['Price-binned'].value_counts())
plt.ylabel("Frequency")
plt.xlabel("Price")
plt.title("Price Binning")
plt.show()

#Indicator Variables
dummy_variable_1 = pd.get_dummies(df["Screen"])
dummy_variable_1.rename(columns = {'IPS Panel': 'Screen-IPS_panel', 'Full HD': 'Screen-Full_HD'}, inplace = True)
df = pd.concat([df, dummy_variable_1], axis =1)


# Dropping the original column "Screen" from the dataset
df.drop("Screen", axis =1, inplace = True)

