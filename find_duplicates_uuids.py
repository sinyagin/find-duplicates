import re
import json
import os
import sys
from collections import Counter

# Regular expression to identify UUIDs
uuid_pattern = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")

# Fields to exclude
excluded_fields = {"parentId", "rootId", "_ref"}

def find_uuids(data, uuids=None, parent_key=None):
    if uuids is None:
        uuids = []

    if isinstance(data, dict):
        for key, value in data.items():
            if key not in excluded_fields:  # Skip excluded fields
                find_uuids(value, uuids, key)
    elif isinstance(data, list):
        for item in data:
            find_uuids(item, uuids, parent_key)
    elif isinstance(data, str):
        if uuid_pattern.fullmatch(data):
            uuids.append(data)
    return uuids

def find_duplicate_uuids(json_data):
    all_uuids = find_uuids(json_data)
    #print("All UUIDs found (excluding specified fields):", all_uuids)
    duplicates = [uuid for uuid, count in Counter(all_uuids).items() if count > 1]
    return duplicates

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find-duplicates.py <filename>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Validate the filename
    if not os.path.isfile(input_file):
        print(f"File not found: {input_file}")
        sys.exit(1)

    if not input_file.endswith('.json'):
        print(f"Invalid file type. Please provide a JSON file.")
        sys.exit(1)

    try:
        with open(input_file, "r") as file:
            json_data = json.load(file)

        # Find duplicates
        duplicates = find_duplicate_uuids(json_data)
        print("Duplicate UUIDs:", duplicates)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
