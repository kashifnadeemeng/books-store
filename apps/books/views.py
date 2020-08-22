from .models import Category
from django.views.generic import DetailView


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
