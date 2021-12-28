from typing import Dict

from django.views.generic import DetailView, ListView

from product_viewer_app.models import Product
from generic_pages_app.utils import BannerContext, BaseContextMixin

from .models import GenericPage


class IndexPageView(BaseContextMixin, ListView):
    model = Product
    queryset = Product.objects.all().order_by("updated_at")
    context_object_name = "products"
    template_name = "generic_pages_app/index.html"

    def get_context_data(self, **kwargs) -> Dict:
        page_title = "Главная"
        banner_context = BannerContext.product_list_banner_context()
        context = super().get_context_data(page_title=page_title, **kwargs) | banner_context
        return context


class GenericPageDetailView(BaseContextMixin, DetailView):
    model = GenericPage
    context_object_name = "page_data"
    template_name = "generic_pages_app/page_detail.html"

    def get_context_data(self, **kwargs) -> Dict:
        page_title = self.object.name
        context = super().get_context_data(page_title=page_title, **kwargs)
        return context
