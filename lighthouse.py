import schedule
import time
import subprocess
import json
import csv

# def run_lighthouse():
#     command = "lighthouse https://mbwebdeveloper.com/ --output=json --output-path=/Users/mikeberg/Desktop/lighthouse/report.json"
#     subprocess.run(command, shell=True)
#     convert_to_csv()

def export_to_csv():
    with open("test_report.json") as f:
        list1 = []
        data = json.load(f)
        temp = data
        header_items = []
        get_header_items(header_items, temp)
        list1.append(header_items)
        print(list1)
      
def get_header_items(items, obj):
    for x in obj:
        if isinstance(obj[x], dict):
            items.append(x)
            get_header_items(items, obj[x])
        else:
            items.append(x)

export_to_csv()

