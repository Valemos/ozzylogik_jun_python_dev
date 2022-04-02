from dataclasses import dataclass

from PIL import Image


@dataclass
class ComputerInfo:
    name: str
    price: int
    review_amount: int
    photos: list[Image.Image]
    graphics_card: str
    video_memory: int
    processor: str
    core_amount: int
    RAM: int
    SSD: str
    HDD: str
    motherboard: str
    unique_name: str = ""
