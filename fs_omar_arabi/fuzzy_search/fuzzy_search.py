import sys
import os

def fuzzy_search(dir: str, pattern: str, filter_by: str) -> list[str]:
    if not os.path.exists(dir) or os.path.isfile(dir):
        print(f"{dir} is invalid", file=sys.stderr)
        sys.exit(1)
    
    matches = []
    entries = os.listdir(dir)

    if filter_by == "files":
        entries = filter(lambda entry: os.path.isfile(entry), entries)
    elif filter_by == "dirs":
        entries = list(filter(lambda entry: os.path.isdir(entry), entries))
    elif filter_by != "":
        print(f"invalid option for filter", file=sys.stderr)
        sys.exit(1)

    for entry in entries:
        if pattern in entry:
            matches.append(entry)
    
    return matches