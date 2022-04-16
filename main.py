from pandas import read_csv

titanic = read_csv("titanic.csv")

# Read first 10 records
print(titanic.head(10))

# See data types
print(titanic.dtypes)


# Export CSV to Excel File
# needs : openpyxl package
titanic.to_excel("tittanic.xlsx", sheet_name="passengers", index=False)

# Show info about csv object
print(titanic.info())

# Select an especific column (Age)
print(titanic.Age)

# Select several columns (Age, sex)
print(titanic[["Age", "Sex"]].head(1))

# Filtering by Age gt 70
above_70 = titanic[titanic.Age > 70]
print(above_70)
print(above_70.shape)

# Filtering by In [2,3]
classs_2_3 = titanic[titanic.Pclass.isin([2, 3])]
print(classs_2_3)

# Filtering by no value
no_age = titanic[titanic["Age"].notna()]
print(no_age)

# Selecting columns
age_gt70_name = titanic.loc[titanic["Age"] > 70, ["Name", "Sex"]]
print(age_gt70_name)

# Selecting range of rows
rows = titanic.iloc[9:14, 5:8]
print(rows)
