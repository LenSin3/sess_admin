import codecs
import json

# Read and remove BOM
with codecs.open("full_backup_fixed.json", "r", encoding="utf-8-sig") as f:
    clean_data = f.read()

# Write it back as clean UTF-8 without BOM
with open("full_backup_clean.json", "w", encoding="utf-8") as f:
    f.write(clean_data)

print("BOM removed and saved as full_backup_clean.json")

# Load the original fixture
with open('full_backup_clean.json', 'r') as f:
    data = json.load(f)

# Filter out ContentType objects
cleaned_data = [item for item in data if not (
    item.get('model') == 'contenttypes.contenttype'
)]

# Save the cleaned fixture
with open('full_backup_without_contenttypes.json', 'w') as f:
    json.dump(cleaned_data, f, indent=2)
