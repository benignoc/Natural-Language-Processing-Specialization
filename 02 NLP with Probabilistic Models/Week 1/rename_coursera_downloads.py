#!/usr/bin/env python3

from pathlib import Path

p = Path('.')

change_l = list(p.glob("**/utf-8''*"))

for f in change_l:
    splits = f.name.split("''")
    old_path = Path(f)
    new_path = Path(''.join(splits[1:]))
    print(f"Renaming {f} into {new_path}")
    old_path.replace(new_path)

if not change_l:
    print("No files starting with utf-8''")
else:
    print("-------------\nAll done")