#1

def extract(file_path):
  	# Ingest the data to a DataFrame
    raw_data = pd.read_parquet(file_path)
    
    # Return the DataFrame
    return raw_data
  
raw_sales_data = extract("sales_data.parquet")

#2

def transform(raw_data):
  	# Filter rows and columns
    clean_data = raw_data.loc[raw_data["Quantity Ordered"]==1, ["Order ID", "Price Each", "Quantity Ordered"]]
    return clean_data

# Transform the raw_sales_data
clean_sales_data = transform(raw_sales_data)

#3
clean_sales_data.sort_values("Price Each", ascending=False).head() #1700
