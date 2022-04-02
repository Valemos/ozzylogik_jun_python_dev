from computer_scraping.computer_info import ComputerInfo
from computer_scraping.website import get_page_or_throw, main_url, title_url, get_image


def strip_int(value: str):
    return int(''.join(filter(str.isdigit, value)))


def parse_computer_html(computer_html):
    computer_page_url = computer_html.find("a")
    page_url = computer_page_url["href"]
    computer_page = get_page_or_throw(main_url + page_url)

    price = computer_page.find(class_="autocalc-product-special").text
    price = strip_int(price)

    review_amount = computer_page.find("a", href="#tab-review").text
    review_amount = int(review_amount[review_amount.index('(') + 1:
                                      review_amount.index(')')])

    photos = []
    for photo in computer_page.find_all("a", class_="thumbnail"):
        photos.append(get_image(photo["href"]))

    computer_info = {}
    for block in computer_page.find(id="tab-specification").find_all("tbody"):
        for row in block.find_all("tr"):
            columns = row.find_all("td")
            if len(columns) < 2: continue
            computer_info[columns[0].text] = columns[1].text

    ram_amount = strip_int(computer_info["Объем памяти ОЗУ"])

    message_ram_as_video_memory = "В качестве видеопамяти используется " \
                                  "буфер из оперативной памяти"
    video_memory = computer_info.get("Объем видеопамяти", message_ram_as_video_memory)
    if video_memory == message_ram_as_video_memory:
        video_memory = ram_amount

    core_amount = strip_int(computer_info["Количество ядер"])

    ssd = strip_int(computer_info.get("Диск SSD", "0"))
    hdd = strip_int(computer_info.get("Диск HDD", "0"))

    return ComputerInfo(
        page_url,
        computer_page.find("h1").text,
        price,
        review_amount,
        photos,
        computer_info["Видеокарта"],
        video_memory,
        computer_info["Процессор"],
        core_amount,
        ram_amount,
        ssd,
        hdd,
        computer_info["На чипсете"]
    )


def parse_page_computers(page):
    for product in page.find_all(class_="product-inner"):
        yield parse_computer_html(product)


def parse_all_computers():
    yield from parse_page_computers(get_page_or_throw(title_url))
    current_page = 2
    while True:
        try:
            yield from parse_page_computers(
                get_page_or_throw(title_url, {"page": current_page})
            )
        except RuntimeError:
            break
