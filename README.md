# 📊 Flipkart Mobile Data Analysis & Dashboard

## 📌 Project Overview
This project analyzes the mobile phone market in India using Flipkart product data.  
It includes:
- **Cleaned Dataset** (`Cleaned_Flipkart_Mobiles.xlsx`)
- **Power BI Dashboard** (`Flipkart_Assessment_Dashboard.pbix`)
- **Insights Document** (`Flipkart_Assessment_Q&A.docx`)
- **Python Data Cleaning Script**

The analysis covers market segmentation, brand performance, and key product specifications, providing data-driven insights into consumer trends.

---

## 📂 Files in Repository
| File Name | Description |
|-----------|-------------|
| `Cleaned_Flipkart_Mobiles.xlsx` | Cleaned dataset used for analysis |
| `Flipkart_Assessment_Dashboard.pbix` | Interactive Power BI dashboard |
| `Flipkart_Assessment_Q&A.docx` | Written insights & answers to assessment questions |
| `flipkart_cleaning.py` | Python script used for cleaning the raw dataset |

---

## 🔍 Key Insights
- **Price Segments:**
  - Low Range: < ₹10,000  
  - Mid Range: ₹10,000 – ₹19,999  
  - Premium: ≥ ₹20,000  

- **Top Brands by Model Count:**
  1. Samsung – 696 models  
  2. Apple – 369 models  
  3. realme – 294 models  
  4. OPPO – 260 models  
  5. Nokia – 209 models  

- **Most Common Specs:**
  - RAM: 4 GB  
  - Storage: 64 GB  

- **Market Trend:**
  - Mid-range segment dominates with the highest number of offerings.
  - Samsung leads in variety across all price ranges.
  - Apple dominates the premium category.

---

## 📈 Dashboard Highlights
The **Power BI Dashboard** allows:
- Price range comparison
- Brand market share visualization
- Segment-specific brand presence
- Filtering by specifications

---

## 🛠 Tools & Technologies
- **Excel** → Data cleaning & preparation  
- **Python (Pandas, NumPy)** → Data preprocessing  
- **Power BI** → Dashboard creation  
- **Tableau** → Comparative visualizations (optional)  

---

## 🧹 Data Cleaning Process (Python)
Before creating the Power BI dashboard, I cleaned the raw dataset using **Python** and **pandas**.  
The steps included:
1. Removing rows with missing values in `Memory` or `Storage`.
2. Extracting numerical values from text-based RAM/Storage columns.
3. Categorizing mobiles into **Low**, **Mid**, and **Premium** price segments.
4. Exporting the cleaned dataset for Power BI analysis.

```python
import pandas as pd

# Load the Excel file
file_path = "C:\\Assessment\\Filpkart Mobiles.xlsx"  # Replace with your actual file path
xls = pd.ExcelFile(file_path)

# Load data from the relevant sheet
df = xls.parse('Flipkart_Mobiles')

# Drop rows with missing Memory or Storage
df_clean = df.dropna(subset=["Memory", "Storage"])

# Convert Memory and Storage to numerical GB values
df_clean["Memory_GB"] = df_clean["Memory"].str.extract(r"(\d+)").astype(float)
df_clean["Storage_GB"] = df_clean["Storage"].str.extract(r"(\d+)").astype(float)

# Price segmentation
def classify_price(price):
    if price < 10000:
        return "Low"
    elif 10000 <= price < 20000:
        return "Mid"
    else:
        return "Premium"

df_clean["Price Segment"] = df_clean["Selling Price"].apply(classify_price)

# Save the cleaned dataset
df_clean.to_excel("Cleaned_Flipkart_Mobiles.xlsx", index=False)

# Summary Insights
print("Total entries after cleaning:", len(df_clean))
print("\nPrice Segment Distribution:\n", df_clean["Price Segment"].value_counts())
print("\nTop 5 Brands by Count:\n", df_clean["Brand"].value_counts().head(5))
print("\nBrands Covering All Segments:\n", df_clean.groupby("Brand")["Price Segment"].nunique().loc[lambda x: x == 3].index.tolist())
print("\nMost Common Memory (GB):", df_clean["Memory_GB"].mode()[0])
print("Most Common Storage (GB):", df_clean["Storage_GB"].mode()[0])
