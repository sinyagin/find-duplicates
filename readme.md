# find_duplicate_uuids.py

## Overview
The script identifies duplicate UUIDs in a JSON file, helping debug issues caused by repeated entities IDs.

## Usage
1. Save the script and a JSON file.
2. Run from the command line:
   ```bash
   python find_duplicate_uuids.py <filename>
## Features
- Scans JSON recursively for UUIDs.
- Excludes specific fields (parentId, rootId, _ref).
- Outputs all found UUID duplicates.
## Example
Input JSON:
```json
{
    "entities": [
        { "id": "abc-123", "type": "producer" },
        { "id": "abc-123", "type": "beneficiary" }
    ]
}
```
Command:
```bash
    python find_duplicate_uuids.py example.json
```
Output:
```
Duplicate UUIDs: ['d3d3934a-3ad2-42dd-8c6a-84e019c50a7c', 'f4b3934b-4cd2-53ef-9c7a-95f020d61b8d']
```
Dependencies
- Python 3.x
- Standard libraries: json, re, os, sys, collections