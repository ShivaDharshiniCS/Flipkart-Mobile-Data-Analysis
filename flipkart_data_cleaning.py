import pandas as pd

# Load the Excel file
file_path = "C:\Assessment\Filpkart Mobiles.xlsx"  # Replace with your actual file path
xls = pd.ExcelFile(file_path)

# Load data from the relevant sheet
df = xls.parse('Flipkart_Mobiles')

# Drop rows with missing Memory or Storage
df_clean = df.dropna(subset=["Memory", "Storage"])

# Convert Memory and Storage columns to numerical GB values
df_clean["Memory_GB"] = df_clean["Memory"].str.extract(r"(\d+)").astype(float)
df_clean["Storage_GB"] = df_clean["Storage"].str.extract(r"(\d+)").astype(float)

# Create a new Price Segment column
def classify_price(price):
    if price < 10000:
        return "Low"
    elif 10000 <= price < 20000:
        return "Mid"
    else:
        return "Premium"

df_clean["Price Segment"] = df_clean["Selling Price"].apply(classify_price)

# Save the cleaned dataset to Excel (use this in Power BI)
df_clean.to_excel("Cleaned_Flipkart_Mobiles.xlsx", index=False)

# Optional: Print summary insights
print("Total entries after cleaning:", len(df_clean))
print("\nPrice Segment Distribution:\n", df_clean["Price Segment"].value_counts())
print("\nTop 5 Brands by Count:\n", df_clean["Brand"].value_counts().head(5))
print("\nBrands Covering All Segments:\n", df_clean.groupby("Brand")["Price Segment"].nunique().loc[lambda x: x == 3].index.tolist())
print("\nMost Common Memory (GB):", df_clean["Memory_GB"].mode()[0])
print("Most Common Storage (GB):", df_clean["Storage_GB"].mode()[0])
