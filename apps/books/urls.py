from django.urls import path
from .views import CategoryDetailView

urlpatterns = [
    path('books/<slug>/', CategoryDetailView.as_view(), name='books'),
]
