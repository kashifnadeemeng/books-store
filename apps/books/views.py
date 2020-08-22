from .models import Book, Category
from django.views.generic import DetailView, ListView


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_books'] = Book.objects.featured()
        return context
