import io

import requests
from PIL import Image
from bs4 import BeautifulSoup

main_url = "https://it-blok.com.ua/"
title_url = main_url + "computeri.html"


def get_main_page():
    return get_page_or_throw(title_url)


def get_response_or_throw(url, params=None):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) "
                             "Gecko/20100101 Firefox/47.0"}
    response = requests.get(url, params=params, headers=headers)
    if not response.status_code == requests.codes.OK:
        raise RuntimeError(f"cannot get page {url}")
    return response


def get_page_or_throw(url, params=None):
    response = get_response_or_throw(url, params)
    return BeautifulSoup(response.content, 'html.parser')


def get_image(url):
    response = get_response_or_throw(main_url + url)
    return Image.open(io.BytesIO(response.content))
