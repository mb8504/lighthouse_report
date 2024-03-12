#!/bin/bash

import schedule
import time
import subprocess
import json
import csv

def run_lighthouse():
    command = "lighthouse https://mbwebdeveloper.com/ --output=json --output-path=/Users/mikeberg/Desktop/lighthouse/report.json"
    subprocess.run(command, shell=True)
    convert_to_csv()

def convert_to_csv():
    json_file = '/Users/mikeberg/Desktop/lighthouse/report.json'
    csv_file = '/Users/mikeberg/Desktop/lighthouse/report.csv'

    with open(json_file, 'r') as f:
        list1 = []
        data = json.load(f.read())
        temp = data[0]
        header_items = []
        get_header_items(header_items, temp)
        list1.append(header_items)

def get_header_items(items, obj):
    for x in obj:
        if isinstance(obj[x], dict):
            items.append(x)
            get_header_items(items, obj[x])
        else:
            items.append(x)  

    # Extract relevant data from JSON



# Schedule the task to run every 1 minute
schedule.every(1).minutes.do(run_lighthouse)

while True:
    schedule.run_pending()
    time.sleep(1)
