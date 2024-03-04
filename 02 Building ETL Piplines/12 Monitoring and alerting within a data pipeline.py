#1
def transform(raw_data):
	return raw_data.loc[raw_data["Total Price"] > 1000, :]

try:
	clean_sales_data = transform(raw_sales_data)
	logging.info("Successfully filtered DataFrame by 'Total Price'")
	
#2
# Update the exception to be a KeyError, alias as ke
except KeyError as ke:
	# Log a warning-level message
	logging.warning(f"{ke}: Cannot filter DataFrame by 'Total Price'")

#3
	# Create the "Total Price" column, transform the updated DataFrame
	raw_sales_data["Total Price"] = raw_sales_data["Price Each"] * raw_sales_data["Quantity Ordered"]
	clean_sales_data = transform(raw_sales_data)
