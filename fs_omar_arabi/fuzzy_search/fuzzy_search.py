import sys
import os

def fuzzy_search(dir: str, pattern: str, filter: str) -> list[str]:
    if not os.path.exists(dir) or os.path.isfile(dir):
        print(f"{dir} is invalid", file=sys.stderr)
        sys.exit(1)
    
    matches = []
    entries = os.listdir(dir)
    for entry in entries:
        if pattern in entry:
            matches.append(entry)
    
    return matches