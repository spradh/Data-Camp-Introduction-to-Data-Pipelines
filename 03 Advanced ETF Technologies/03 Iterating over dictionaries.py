#1
raw_testing_scores_keys = []

# Iterate through the keys of the raw_testing_scores dictionary
for school_id in raw_testing_scores.keys():
  	# Append each key to the raw_testing_scores_keys list
	raw_testing_scores_keys.append(school_id)
    
print(raw_testing_scores_keys[0:3])

#2
raw_testing_scores_values = []

# Iterate through the values of the raw_testing_scores dictionary
for school_info in raw_testing_scores.values():
	raw_testing_scores_values.append(school_info)
    
print(raw_testing_scores_values[0:3])


#3
raw_testing_scores_keys = []
raw_testing_scores_values = []

# Iterate through the values of the raw_testing_scores dictionary
for school_id, school_info in raw_testing_scores.items():
	raw_testing_scores_keys.append(school_id)
	raw_testing_scores_values.append(school_info)

print(raw_testing_scores_keys[0:3])
print(raw_testing_scores_values[0:3])
