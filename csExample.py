import json

with open('test_report.json') as f:
    data = json.load(f)

# Access the 'performance' object within the 'categories' object
performance_data = data['categories']['performance']
accessability_data = data['categories']['accessibility']
best_practices_data = data['categories']['best-practices']
seo_data = data['categories']['seo']
fcp_data = data['audits']['first-contentful-paint']
lcp_data = data['audits']['largest-contentful-paint']
tbt_data = data['audits']['total-blocking-time']
cls_data = data['audits']['cumulative-layout-shift']
si_data = data['audits']['speed-index']

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

# Extract the first contentful paint 'id' and 'score' fields
fcp_id = fcp_data['id']
fcp_score = fcp_data['displayValue']

# Extract the largest contentful paint 'id' and 'score' fields
lcp_id = lcp_data['id']
lcp_score = lcp_data['displayValue']

# Extract the total blocking time 'id' and 'score' fields
tbt_id = tbt_data['id']
tbt_score = tbt_data['displayValue']

# Extract the cumulative layout shift 'id' and 'score' fields
cls_id = cls_data['id']
cls_score = cls_data['displayValue']

# Extract the speed index 'id' and 'score' fields
si_id = si_data['id']
si_score = si_data['displayValue']

# Print the extracted data
print("ID:", performance_id)
print("Score:", performance_score)
print("ID:", accessability_id)
print("Score:", accessability_score)
print("ID:", best_practices_id)
print("Score:", best_practices_score)
print("ID:", seo_id)
print("Score:", seo_score)
print("ID:", fcp_id)
print("Score:", fcp_score)
print("ID:", lcp_id)
print("Score:", lcp_score)
print("ID:", tbt_id)
print("Score:", tbt_score)
print("ID:", cls_id)
print("Score:", cls_score)
print("ID:", si_id)
print("Score:", si_score)