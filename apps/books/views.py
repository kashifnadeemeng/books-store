from .models import Category, Book
from django.views.generic import ListView, DetailView


class CategoryListView(ListView):
    model = Category
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['featured_books'] = Book.objects.featured()
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_books.html'
