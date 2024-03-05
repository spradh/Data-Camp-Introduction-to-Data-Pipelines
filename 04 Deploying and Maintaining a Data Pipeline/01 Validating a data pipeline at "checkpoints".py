#1
# Extract and transform tax_data
raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)

# Check the shape of the raw_tax_data DataFrame, compare to the clean_tax_data DataFrame
print(f"Shape of raw_tax_data: {raw_tax_data.shape}")
print(f"Shape of clean_tax_data: {clean_tax_data.shape}")


#2
# Read in the loaded data, observe the head of each
to_validate = pd.read_parquet("clean_tax_data.parquet")
print(clean_tax_data.head(3))
print(to_validate.head(3))


#3
# Check that the DataFrames are equal
print(to_validate.equals(clean_tax_data))
