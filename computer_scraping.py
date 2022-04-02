from pathlib import Path
import csv

from computer_scraping.computer_info import ComputerInfo
from computer_scraping.parsing import parse_all_computers


base_folder = Path("data")


def save_photos(computer: ComputerInfo):
    image_folder_path = base_folder / computer.unique_name
    image_folder_path.mkdir(exist_ok=True, parents=True)
    saved_paths = []
    for i, image in enumerate(computer.photos):
        image_path = image_folder_path / f"{i}.png"
        image.save(image_path)
        saved_paths.append(image_path)
    return saved_paths


def save_data(computer: ComputerInfo):
    saved_paths = save_photos(computer)

    save_path = base_folder / f"{computer.RAM}gb.csv"
    with save_path.open("a+") as f:
        writer = csv.writer(f)
        writer.writerow([
            computer.name,
            computer.price,
            computer.review_amount,
            '|'.join(map(str, saved_paths)),
            computer.graphics_card,
            computer.video_memory,
            computer.processor,
            computer.core_amount,
            computer.RAM,
            computer.SSD,
            computer.HDD,
            computer.motherboard
        ])


if __name__ == '__main__':
    for computer in parse_all_computers():
        save_data(computer)
