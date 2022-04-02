from pathlib import Path

import csv

from connection import *


if __name__ == '__main__':
    init()

    input_path = Path("./random_strings_edited.csv")

    with input_path.open("r") as f:
        reader = csv.reader(f)
        for row in reader:
            insert_line(row)

    for row in get_all_rows():
        print(row)
