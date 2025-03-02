import codecs

# Read and remove BOM
with codecs.open("full_backup_fixed.json", "r", encoding="utf-8-sig") as f:
    clean_data = f.read()

# Write it back as clean UTF-8 without BOM
with open("full_backup_clean.json", "w", encoding="utf-8") as f:
    f.write(clean_data)

print("BOM removed and saved as full_backup_clean.json")
