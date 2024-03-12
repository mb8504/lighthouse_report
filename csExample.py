import json

with open('test_report.json') as f:
    data = json.load(f)

# Access the 'performance' object within the 'categories' object
performance_data = data['categories']['performance']

# Iterate over the key-value pairs in the 'performance' object and print them
for key, value in performance_data.items():
    print(f"{key}: {value}")
