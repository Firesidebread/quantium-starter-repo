import pandas as pd
import os

# Load all three CSV files from the data folder
data_folder = "data"
files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

dfs = []
for file in files:
    df = pd.read_csv(os.path.join(data_folder, file))
    dfs.append(df)

# Combine all three into one
combined = pd.concat(dfs, ignore_index=True)

# Step 1: Keep only Pink Morsels
combined = combined[combined["product"] == "pink morsel"]

# Step 2: Calculate sales = quantity x price
# Remove $ sign from price if present and convert to float
combined["price"] = combined["price"].str.replace("$", "", regex=False).astype(float)
combined["sales"] = combined["quantity"] * combined["price"]

# Step 3: Keep only the columns we need
output = combined[["sales", "date", "region"]]

# Save to a new CSV file
output.to_csv("data/output.csv", index=False)

print("Done! Output saved to data/output.csv")