#1
import logging

# Import extract, transform, and load functions from pipeline_utils
from pipeline_utils import extract, transform, load


#2
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

try:
  	# Extract, transform, and load the tax data
	raw_tax_data = extract("raw_tax_data.csv")
	clean_tax_data = transform(raw_tax_data)
	load(clean_tax_data, "clean_tax_data.parquet")
    
#3
	logging.info("Successfully extracted, transformed and loaded data.")  # Log a success message.
    
except Exception as e:
	logging.error(f"Pipeline failed with error: {e}")  # Log failure message

