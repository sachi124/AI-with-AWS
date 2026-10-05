import pandas as pd

# load the titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Display the Dataset Information
print("Dataset Info.....\n")
print(df.info())

# Preview the first few row
print("Dataset Preview:")
print(df.head())

# Seperate the features
categorical_feature = df.select_dtypes(include=["object"]).columns
numerical_features = df.select_dtypes(include=["int64", "float64"]).columns

print("\nCategorical features:", categorical_feature.to_list())
print("\nNumerical features:", numerical_features.to_list())

# display the features of categorical values
print("\n Categorical feature Summary: \n")
for col in categorical_feature:
    print("\n {col}:\n", df[col].value_counts(), "\n")

print("\n Numerical features Summary: \n")
print(df[numerical_features].describe().T)