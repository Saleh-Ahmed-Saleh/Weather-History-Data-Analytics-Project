import pandas as pd

df = pd.read_csv(r"C:\Users\2019\Downloads\Weather Dataset\weatherHistory.csv")

# print(df.head())
# print(df.shape)
# print(df.index)
# print(df.columns)


# print(df['Precip Type'].value_counts())

# Find all Unique Wind Speed Values in the data

# print(df['Wind Speed (km/h)'].unique())

# print(df[df.Summary == 'Clear'])
# print(df.groupby('Summary').get_group('Clear'))

# Find the Number of Times When the 'Wind Speed Was Exactly 4km/h'.
# print(df[df['Wind Speed (km/h)'] == 4.7495])


# Find Out the Null Values in the data
# print(df.notnull().sum())
# print(df.isnull().sum())

print(df.rename(columns={"Daily Summary": "Weather Condition"}, inplace=True))


# What is the Pressure in this data ?
# df['Pressure (millibars)'].std()
# What is the mean 'Visibility' ?
# df['Visibility (km)'].mean()
# What is the Variance of 'Humidity' in this data ?
# df['Humidity'].var()
# Find all instances when'snow' was recorded
# df["Precip Type"].value_counts()
# df[df["Precip Type"] == "snow"]


# Show all records Where Weather Condition is Fog
# print(df['Weather Condition'].value_counts())
# print(df[df["Weather Condition"].str.contains("Foggy")])


# Find the all instances When 'weather is clear or d'Visibility is above 40
print(df[(df['Summary'] == "Clear") | (df["Visibility (km)"] > 40)])
