# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:06:02 2026

@author: molin
"""

"""
Compare file names (stems, ignoring extensions) between two directory trees.
Produces:
  - paths of files whose stem exists in FIRST but not in SECOND
  - paths of files whose stem exists in SECOND but not in FIRST
"""

from pathlib import Path
from typing import List, Set, Tuple


def collect_files(root: Path) -> Tuple[List[Path], Set[str]]:
    """Return (list of file paths, set of stems) under root (recursive)."""
    files: List[Path] = []
    stems: Set[str] = set()
    for path in root.rglob("*"):
        if path.is_file():
            files.append(path)
            stems.add(path.stem)
    return files, stems


def main() -> None:
    # --- configure these two paths ---
    while True:
        new_dir = input("Enter FIRST Directory ---> ")
        try:
            first_dir = Path(new_dir)
            break
        except:
            print("Error: Invalid Path ={}>".format(new_dir))
            print("  TRY AGAIN!")
    #
    # first_dir  = Path(r"/path/to/FIRST")
    while True:
        new_dir = input("Enter SECOND Directory ---> ")
        try:
            second_dir = Path(new_dir)
            break
        except:
            print("Error: Invalid Path ={}>".format(new_dir))
            print("  TRY AGAIN!")
    #
    # second_dir = Path(r"/path/to/SECOND")
    # ---------------------------------

    if not first_dir.is_dir():
        raise SystemExit(f"FIRST directory does not exist or is not a directory: {first_dir}")
    if not second_dir.is_dir():
        raise SystemExit(f"SECOND directory does not exist or is not a directory: {second_dir}")

    first_files,  first_stems  = collect_files(first_dir)
    second_files, second_stems = collect_files(second_dir)

    only_in_first  = [p for p in first_files  if p.stem not in second_stems]
    only_in_second = [p for p in second_files if p.stem not in first_stems]

    print(f"Files whose stem is in FIRST but not in SECOND ({len(only_in_first)}):")
    for p in sorted(only_in_first):
        print(f"  {p}")

    print()
    print(f"Files whose stem is in SECOND but not in FIRST ({len(only_in_second)}):")
    for p in sorted(only_in_second):
        print(f"  {p}")

    # The two lists are also available as Python objects:
    # only_in_first, only_in_second


if __name__ == "__main__":
    main()