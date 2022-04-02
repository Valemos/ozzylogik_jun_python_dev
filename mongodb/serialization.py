import csv
from pathlib import Path

from connection import *


def row_to_document(row):
    return {f"s{i}": value for i, value in enumerate(row)}


if __name__ == '__main__':
    input_path = Path("../random_strings_edited.csv")

    with input_path.open("r") as f:
        reader = csv.reader(f)
        for row in reader:
            database["random_strings"].insert_one(row_to_document(row))

    for doc in database["random_strings"].find({}):
        print(doc)
