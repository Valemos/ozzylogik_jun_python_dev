import csv
from pathlib import Path


def replace_odd_char(char: str):
    if char.isdigit():
        if int(char) % 2 != 0:
            return '#'
    return char


def replace_chars(value: str):
    return ''.join(map(replace_odd_char, value))


def is_invalid(record):
    return record[0].lower() in "aeiou"


if __name__ == '__main__':
    input_path = Path("random_strings.csv")
    output_path = Path("random_strings_edited.csv")

    initial = []
    with input_path.open("r") as fin, output_path.open("w") as fout:
        input_reader = csv.reader(fin)
        output_writer = csv.writer(fout)

        for line in input_reader:
            if any(is_invalid(record) for record in line):
                continue

            modified_line = map(replace_chars, line)
            output_writer.writerow(modified_line)
