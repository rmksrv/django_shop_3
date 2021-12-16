from dataclasses import dataclass, asdict
from typing import Dict
from .constants import (
    HEADER_TITLE_LEFT,
    HEADER_TITLE_RIGHT,
    FOOTER_EXTERNAL_LINKS,
    FOOTER_COPYRIGHT_LABEL,
    FOOTER_SITE_MADE_BY_LABEL,
    FOOTER_SITE_MADE_BY_HREF, NO_IMAGE_URL,
    INDEX_BANNER_HEADER_TEXT,
    INDEX_BANNER_CONTEXT_TEXT,
    INDEX_BANNER_IMAGE_URL,
)
from .models import Category


class BaseContextMixin(object):

    def get_context_data(self, **kwargs) -> Dict:
        context = super().get_context_data(**kwargs) | {
            "header": {
                "title_left": HEADER_TITLE_LEFT,
                "title_right": HEADER_TITLE_RIGHT,
            },
            "menu": {
                "categories": Category.objects.filter(products__isnull=False),
                "actions": {
                    "О нас": "#",
                }
            },
            "footer": {
                "copyright_label": FOOTER_COPYRIGHT_LABEL,
                "external_links": FOOTER_EXTERNAL_LINKS,
                "site_made_by_label": FOOTER_SITE_MADE_BY_LABEL,
                "site_made_by_href": FOOTER_SITE_MADE_BY_HREF,
            }
        }
        return context


# TODO: вот наверняка можно сделать как миксин, но я чет не смог придумать, как полностью и изящно
#  засунуть сюда логику получения контекста для категории или дефолт
@dataclass
class BannerContext:
    header_text: str
    content_text: str
    button_text: str = "Посмотреть"
    button_href: str = "#main_section"
    image_url: str = NO_IMAGE_URL
    type: str = "major"  # можем ли юзать django choices для type-hinting?

    @staticmethod
    def index_banner_context():
        return {
            "banner": asdict(BannerContext(
                header_text=INDEX_BANNER_HEADER_TEXT,
                content_text=INDEX_BANNER_CONTEXT_TEXT,
                image_url=INDEX_BANNER_IMAGE_URL,
            ))
        }

    @staticmethod
    def category_product_list_banner_context(category: Category):
        return {
            "banner": asdict(BannerContext(
                header_text=category.name,
                content_text="",
                image_url=category.image.url,
            ))
        }
