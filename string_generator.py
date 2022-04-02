import random
import csv
from pathlib import Path
import string


_possible_chars = string.ascii_lowercase \
                  + string.ascii_uppercase \
                  + string.digits


def random_string(length=8):
    return ''.join(random.choice(_possible_chars) for _ in range(length))


if __name__ == '__main__':
    output_path = Path("random_strings.csv")

    with output_path.open("w") as f:
        writer = csv.writer(f)
        for row in range(1024):
            writer.writerow(random_string() for _ in range(6))
