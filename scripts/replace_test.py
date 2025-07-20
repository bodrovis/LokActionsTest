import os
import json

translations_path = os.getenv("TRANSLATIONS_PATH", "locales")
target_file = os.path.join(translations_path, "fr.json")

print(f"Reading file: {target_file}")

with open(target_file, "r", encoding="utf-8") as f:
    data = json.load(f)

def replace_values(obj):
    if isinstance(obj, dict):
        return {k: replace_values(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_values(v) for v in obj]
    elif isinstance(obj, str):
        return obj.replace("test", "REPLACED")
    else:
        return obj

updated_data = replace_values(data)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(updated_data, f, ensure_ascii=False, indent=2)

print("Replacement complete.")
