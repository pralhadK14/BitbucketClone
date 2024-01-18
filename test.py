import json

# Initialize an empty list to hold generated data
data_list = {}

# Example loop generating data (replace this with your data generation logic)
for i in range(3):  # Just as an example, loop runs 3 times
    generated_data = {
        "id": i,
        "value": f"value_{i}"
        # Add more key-value pairs based on your generated data
    }
    data_list.add(generated_data)

# Convert the list of dictionaries into a JSON array
json_data = json.dumps(data_list, indent=2)

# Output or use the JSON data
print(json_data)

