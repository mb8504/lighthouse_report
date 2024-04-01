import subprocess
import json
import csv


def run_lighthouse():
    command = "lighthouse https://summer.stanford.edu/facebookads/ --output=json --output-path=/Users/mikeberg/Desktop/lighthouse/report.json"
    subprocess.run(command, shell=True)
    convert_to_csv()

def convert_to_csv():
    json_file = '/Users/mikeberg/Desktop/lighthouse/report.json'
    csv_file = '/Users/mikeberg/Desktop/lighthouse/report.csv'

    # CS PYTHON SCRIPT
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Access the 'performance' object within the 'categories' object
    performance_data = data['categories']['performance']
    accessibility_data = data['categories']['accessibility']
    best_practices_data = data['categories']['best-practices']
    seo_data = data['categories']['seo']
    fcp_data = data['audits']['first-contentful-paint']
    lcp_data = data['audits']['largest-contentful-paint']
    tbt_data = data['audits']['total-blocking-time']
    cls_data = data['audits']['cumulative-layout-shift']
    si_data = data['audits']['speed-index']

    # Initialize a list to store the extracted data
    extracted_data = []

    # Extract the performance 'id' and 'score' fields
    extracted_data.append([performance_data['id'], performance_data['score']])

    # Extract the accessibility 'id' and 'score' fields
    extracted_data.append([accessibility_data['id'], accessibility_data['score']])

    # Extract the best practices 'id' and 'score' fields
    extracted_data.append([best_practices_data['id'], best_practices_data['score']])

    # Extract the seo 'id' and 'score' fields
    extracted_data.append([seo_data['id'], seo_data['score']])

    # Extract the first contentful paint 'id' and 'score' fields
    extracted_data.append([fcp_data['id'], fcp_data['displayValue']])

    # Extract the largest contentful paint 'id' and 'score' fields
    extracted_data.append([lcp_data['id'], lcp_data['displayValue']])

    # Extract the total blocking time 'id' and 'score' fields
    extracted_data.append([tbt_data['id'], tbt_data['displayValue']])

    # Extract the cumulative layout shift 'id' and 'score' fields
    extracted_data.append([cls_data['id'], cls_data['displayValue']])

    # Extract the speed index 'id' and 'score' fields
    extracted_data.append([si_data['id'], si_data['displayValue']])


    # Write the extracted data to a CSV file
    with open('extracted_data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['ID', 'Score'])
        csv_writer.writerows(extracted_data)



run_lighthouse()


# Print the extracted data
# print("ID:", performance_id)
# print("Score:", performance_score)
# print("ID:", accessability_id)
# print("Score:", accessability_score)
# print("ID:", best_practices_id)
# print("Score:", best_practices_score)
# print("ID:", seo_id)
# print("Score:", seo_score)
# print("ID:", fcp_id)
# print("Score:", fcp_score)
# print("ID:", lcp_id)
# print("Score:", lcp_score)
# print("ID:", tbt_id)
# print("Score:", tbt_score)
# print("ID:", cls_id)
# print("Score:", cls_score)
# print("ID:", si_id)
# print("Score:", si_score)