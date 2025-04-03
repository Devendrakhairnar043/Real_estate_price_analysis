import pandas as pd

# Load the original dataset
df = pd.read_csv("C:\\Projects\\real_estate_dataset.csv")  # Make sure this file exists in your project folder

# Clean the dataset (remove missing values, fix types, etc.)
df_cleaned = df.dropna(subset=["price", "bedrooms", "bathrooms", "square_feet"])
df_cleaned.loc[:, "property_type"] = df_cleaned["property_type"].fillna("Unknown")
df_cleaned.loc[:, "listing_date"] = pd.to_datetime(df_cleaned["listing_date"], errors="coerce")

df_cleaned = df_cleaned.drop_duplicates()

# Save the cleaned dataset
df_cleaned.to_csv("real_estate_dataset.csv", index=False)

print("Cleaned dataset saved successfully!")
