import json

with open('test_report.json') as f:
    data = json.load(f)

# Access the 'performance' object within the 'categories' object
performance_data = data['categories']['performance']
accessability_data = data['categories']['accessibility']
best_practices_data = data['categories']['best-practices']
seo_data = data['categories']['seo']

# Extract the performance 'id' and 'score' fields
performance_id = performance_data['id']
performance_score = performance_data['score']

# Extract the accessability 'id' and 'score' fields
accessability_id = accessability_data['id']
accessability_score = accessability_data['score']

# Extract the best practices 'id' and 'score' fields
best_practices_id = best_practices_data['id']
best_practices_score = best_practices_data['score']

# Extract the seo 'id' and 'score' fields
seo_id = seo_data['id']
seo_score = seo_data['score']

# Print the extracted data
print("ID:", performance_id)
print("Score:", performance_score)
print("ID:", accessability_id)
print("Score:", accessability_score)
print("ID:", best_practices_id)
print("Score:", best_practices_score)
print("ID:", seo_id)
print("Score:", seo_score)
