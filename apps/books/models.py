from django.db import models
from common.models import TimeStampedModel


class Category(TimeStampedModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Book(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='uploads/books/')
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    author = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
