
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("C:\\Projects\\real_estate_dataset.csv")

# Display summary statistics
print(df.describe())

# Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["price"], bins=10, kde=True, color="blue")
plt.title("Distribution of Property Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Correlation Heatmap - Only Numeric Columns
numeric_df = df.select_dtypes(include=["number"])  # Select only numeric columns

plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()
