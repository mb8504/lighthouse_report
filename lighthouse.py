import json

def export_to_csv():
    with open("test_report.json") as f:
        list1 = []
        data = json.load(f)
        header_items = []
        get_header_items(header_items, data)
        list1.append(header_items)

        for obj_key, obj_value in data.items():
            d = []
            add_items_to_data(d, obj_value)
            list1.append(d)        
        print(list1)

def get_header_items(items, obj):
    for x in obj:
        if isinstance(obj[x], dict):
            items.append(x)
            get_header_items(items, obj[x])
        else:
            items.append(x)

def add_items_to_data(items, obj):
    if isinstance(obj, dict):
        for x in obj:
            if isinstance(obj[x], dict):
                sub_items = []  # Create a new list for each recursion
                add_items_to_data(sub_items, obj[x])
                items.append(sub_items)
            else:
                items.append(obj[x])
    else:
        items.append(obj)

export_to_csv()
