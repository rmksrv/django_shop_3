from enum import Enum
from typing import Dict

from django.conf import settings


class FontAwesomeIcons(Enum):
    VK = "fa-vk"
    Facebook = "fa-facebook-f"
    Instagram = "fa-instagram"
    Twitter = "fa-twitter"
    YouTube = "fa-youtube"


PRODUCT_IMAGE_LOCATION = "products/%Y/%m/%d"
CATEGORIES_IMAGE_LOCATION = "categories"
NO_IMAGE_PATH = settings.BASE_DIR / "static" / "images" / "no_image.png"
NO_IMAGE_URL = settings.STATIC_URL + "images/no_image.png"

SITE_NAME = 'Интернет магазин "Кузьминка"'

HEADER_TITLE_LEFT = "Интернет магазин"
HEADER_TITLE_RIGHT = "Кузьминка"

FOOTER_EXTERNAL_LINKS: Dict[str, FontAwesomeIcons] = {
    r"https://vk.com/": FontAwesomeIcons.VK,
    r"https://www.facebook.com/": FontAwesomeIcons.Facebook,
    r"https://www.instagram.com/": FontAwesomeIcons.Instagram,
    r"https://twitter.com/": FontAwesomeIcons.Twitter,
    r"https://www.youtube.com/": FontAwesomeIcons.YouTube,
}
FOOTER_COPYRIGHT_LABEL = SITE_NAME
FOOTER_SITE_MADE_BY_LABEL = "Roman Kosarev"
FOOTER_SITE_MADE_BY_HREF = r"https://github.com/rmksrv"

INDEX_BANNER_HEADER_TEXT = SITE_NAME
INDEX_BANNER_CONTEXT_TEXT = """
    Сложно сказать, почему акционеры крупнейших компаний могут быть призваны к ответу. Ключевые особенности 
    структуры проекта и по сей день остаются уделом либералов, которые жаждут быть представлены в исключительно 
    положительном свете. Как принято считать, независимые государства формируют глобальную экономическую сеть и 
    при этом - описаны максимально подробно.
"""
INDEX_BANNER_IMAGE_URL = settings.STATIC_URL + "images/index_banner_image.jpg"
