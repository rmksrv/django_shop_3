from typing import Dict

from django.views.generic import DetailView, ListView

from .models import Category, Product
from .utils import BannerContext, BaseContextMixin


class ProductListView(BaseContextMixin, ListView):
    model = Product
    context_object_name = "products"
    template_name = "product_viewer_app/product_list.html"

    def get_context_data(self, **kwargs) -> Dict:
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            banner_context = BannerContext.category_product_list_banner_context(category)
        else:
            banner_context = BannerContext.product_list_banner_context()

        context = super().get_context_data(**kwargs) | banner_context
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset


class ProductDetailView(BaseContextMixin, DetailView):
    model = Product
    context_object_name = "product"
    template_name = "product_viewer_app/product_detail.html"

    def get_context_data(self, **kwargs) -> Dict:
        banner_context = BannerContext.product_detail_banner_context(self.object)
        context = super().get_context_data(**kwargs) | banner_context
        return context
