from typing import Dict, Optional

import pydantic

from .constants import (
    FOOTER_COPYRIGHT_LABEL,
    FOOTER_EXTERNAL_LINKS,
    FOOTER_SITE_MADE_BY_HREF,
    FOOTER_SITE_MADE_BY_LABEL,
    HEADER_TITLE_LEFT,
    HEADER_TITLE_RIGHT,
    INDEX_BANNER_CONTEXT_TEXT,
    INDEX_BANNER_HEADER_TEXT,
    INDEX_BANNER_IMAGE_URL,
    NO_IMAGE_URL,
    BannerTypeClass,
)
from .models import Category, Product
from generic_pages_app.models import GenericPage


class BaseContextMixin(object):

    def get_context_data(self, **kwargs) -> Dict:
        pages = GenericPage.objects.all()

        context = super().get_context_data(**kwargs) | {
            "header": {
                "title_left": HEADER_TITLE_LEFT,
                "title_right": HEADER_TITLE_RIGHT,
            },
            "menu": {
                "categories": Category.objects.filter(products__isnull=False),
                "actions": {
                    page.title: page.absolute_url() for page in pages
                },
            },
            "footer": {
                "copyright_label": FOOTER_COPYRIGHT_LABEL,
                "external_links": FOOTER_EXTERNAL_LINKS,
                "site_made_by_label": FOOTER_SITE_MADE_BY_LABEL,
                "site_made_by_href": FOOTER_SITE_MADE_BY_HREF,
            },
        }
        return context


class BannerContext(pydantic.BaseModel):
    """
    вот наверняка можно сделать как миксин, но я чет не смог придумать, как полностью и изящно
    засунуть сюда логику получения контекста для категории или дефолт
    """

    header_text: str
    content_text: str = ""
    button_text: Optional[str] = "Посмотреть"
    button_href: Optional[str] = "#main_section"
    image_url: str = NO_IMAGE_URL
    type: BannerTypeClass = BannerTypeClass.Major

    @staticmethod
    def index_banner_context() -> Dict:
        return {
            "banner": BannerContext(
                header_text=INDEX_BANNER_HEADER_TEXT,
                content_text=INDEX_BANNER_CONTEXT_TEXT,
                image_url=INDEX_BANNER_IMAGE_URL,
            ).dict()
        }

    @staticmethod
    def product_list_banner_context() -> Dict:
        # TODO: кажется, что здесь должен быть другой текст
        return BannerContext.index_banner_context()

    @staticmethod
    def category_product_list_banner_context(category: Category) -> Dict:
        return {
            "banner": BannerContext(
                header_text=category.name,
                content_text="",
                image_url=category.image.url,
            ).dict()
        }

    @staticmethod
    def product_detail_banner_context(product: Product) -> Dict:
        return {
            "banner": BannerContext(
                header_text=product.name,
                content_text=product.preview_description,
                button_text=None,
                button_href=None,
                image_url=product.image.url,
                type=BannerTypeClass.Style2,
            ).dict()
        }
