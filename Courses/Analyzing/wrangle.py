import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names= headers)

df.replace('?', np.nan, inplace=True)


# Calculating Average
mean_norm_loss = df['normalized-losses'].astype('float').mean(axis=0)
mean_stroke = df['stroke'].astype('float').mean(axis=0)
mean_bore = df['bore'].astype('float').mean(axis=0)

# Dealing with missing data
df['normalized-losses'].replace(np.nan, mean_norm_loss, inplace=True)
df['stroke'].replace(np.nan, mean_stroke, inplace = True)
df['bore'].replace(np.nan, mean_bore, inplace = True)
df['num-of-doors'].replace(np.nan, df['num-of-doors'].value_counts().idxmax(), inplace=True)

#Dealt with missing data by using dropping method
df.dropna(subset=['price'], axis = 0, inplace = True)
df.reset_index(drop = True, inplace = True)

# Data standardization
df['city-mpg'] = 235/df['city-mpg']
df.rename(columns = {"city-mpg": 'city-L/100km'}, inplace = True)

#Data Normalization
df['height'] = df['height']/ df['height'].max()

#Data Binning
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].astype(float).mean(axis = 0))
df['horsepower'] = df['horsepower'].astype(int)

#Plotting a histogram by using matplotlib
plt.pyplot.hist(df['horsepower'])
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("frequency")
plt.pyplot.title("horsepower bins")
plt.pyplot.grid(True)
plt.pyplot.show()


#Continuation of binning of data
bins = np.linspace(min(df['horsepower']), max(df['horsepower']), 4)
group_names = ['Low', 'Medium', 'High']

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest = True)


pyplot.bar(group_names, df['horsepower-binned'].value_counts())
pyplot.xlabel('horsepower')
pyplot.ylabel('frequency')
pyplot.title('horsepower binning')
pyplot.show()

#Visualizing the bins
pyplot.hist(df['horsepower'], bins = 5)
pyplot.xlabel("Horsepower")
pyplot.ylabel("Count")
pyplot.title("Horsepower Bins")
pyplot.show()

#Creating dummy indicators

dummy_variable_1 = pd.get_dummies(df['aspiration'])
dummy_variable_1.rename(columns = {'std':'aspiration-std', 'turbo':'aspiration-turbo'}, inplace = True)
print(dummy_variable_1.head(10))

df = pd.concat([df, dummy_variable_1], axis =1)
df.drop('aspiration', axis =1, inplace = True)

df.to_csv('clean_df.csv')




