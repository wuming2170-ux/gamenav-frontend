#!/usr/bin/env python3
"""Generate platforms.json from seed_data.py"""

import re, json

# Read seed_data.py
with open('../backend/seed_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract JSON array using regex
match = re.search(r'PLATFORMS\s*=\s*(\[)', content)
if not match:
    print("Could not find PLATFORMS array")
    exit(1)

# Find the matching bracket
start = match.start(1)
bracket_count = 0
end = start
for i, c in enumerate(content[start:]):
    if c == '[':
        bracket_count += 1
    elif c == ']':
        bracket_count -= 1
    if bracket_count == 0:
        end = start + i + 1
        break

json_str = content[start:end]
platforms = json.loads(json_str)

# Ensure required fields
for p in platforms:
    p.setdefault('logo', '')
    p.setdefault('status', 'active')

# Save
with open('platforms.json', 'w', encoding='utf-8') as f:
    json.dump(platforms, f, ensure_ascii=False, indent=2)

print(f"Generated {len(platforms)} platforms")
