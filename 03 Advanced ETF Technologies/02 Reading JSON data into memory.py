#1

def extract(file_path):
  	# Read the JSON file into a DataFrame, orient by index
	return pd.read_json(file_path, orient="index")

# Call the extract function, pass in the desired file_path
raw_testing_scores = extract("nested_scores.json")
print(raw_testing_scores.head())


#2
# Import the json library
import json

def extract(file_path):
    with open(file_path, "r") as json_file:
        # Load the data from the JSON file
        raw_data = json.load(json_file)
    return raw_data

raw_testing_scores = extract("nested_scores.json")

# Print the raw_testing_scores
print(raw_testing_scores)
