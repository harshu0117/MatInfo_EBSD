import json
import csv
import os

def format_json_and_csv(input_path, output_json_path, output_csv_path):
    print(f"Reading {input_path}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"Saving pretty-printed JSON to {output_json_path}...")
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"Creating a single merged CSV at {output_csv_path}...")
    
    ebsd_keys = set()
    nano_keys = set()
    
    for id_val in data:
        for entry in data[id_val].get('ebsd_data', []):
            ebsd_keys.update(entry.keys())
        for entry in data[id_val].get('nano_curve', []):
            nano_keys.update(entry.keys())
            
    ebsd_keys = sorted(list(ebsd_keys))
    nano_keys = sorted(list(nano_keys))
    
    # Combined fieldnames
    all_fieldnames = ['Root_ID', 'Entry_Type'] + sorted(list(set(ebsd_keys) | set(nano_keys)))
    
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=all_fieldnames)
        writer.writeheader()
        
        for id_val in sorted(data.keys(), key=lambda x: int(x) if x.isdigit() else x):
            # Write EBSD entries
            for entry in data[id_val].get('ebsd_data', []):
                row = {'Root_ID': id_val, 'Entry_Type': 'EBSD'}
                row.update(entry)
                writer.writerow(row)
            
            # Write Nano Curve entries
            for entry in data[id_val].get('nano_curve', []):
                row = {'Root_ID': id_val, 'Entry_Type': 'NanoCurve'}
                row.update(entry)
                writer.writerow(row)

if __name__ == "__main__":
    format_json_and_csv('final_indentation_dataset.json', 'final_indentation_dataset_formatted.json', 'final_indentation_dataset_merged.csv')
