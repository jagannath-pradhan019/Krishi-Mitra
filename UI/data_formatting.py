import re

def format_name(name: str) -> str:
    parts = name.split("___")
    if len(parts) > 1:
        disease_part = parts[1]
    else:
        disease_part = parts[0]

    cleaned = re.sub(r'_+', ' ', disease_part)
    formatted = cleaned.title()
    return formatted

def normalize_to_list(value):
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return value.splitlines() or [value]
    return []