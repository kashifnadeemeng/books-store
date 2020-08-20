from django.urls import path
from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('books/<slug>/', CategoryDetailView.as_view(), name='books'),
]
