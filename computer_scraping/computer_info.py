from dataclasses import dataclass

from PIL import Image


@dataclass
class ComputerInfo:
    url_name: str
    name: str
    price: float
    review_amount: int
    photos: list[Image.Image]
    graphics_card: str
    video_memory: float
    processor: str
    core_amount: int
    RAM: int
    SSD: str
    HDD: str
    motherboard: str
