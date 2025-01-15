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
Duplicate UUIDs: ['abc-123']
```
Dependencies
- Python 3.x
- Standard libraries: json, re, os, sys, collections