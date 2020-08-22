from django.db import models
from common.models import TimeStampedModel
from django.shortcuts import reverse


class Category(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('books', kwargs={'slug': self.slug})


class BookManager(models.Manager):
    def featured(self):
        return self.filter(is_featured=True)


class Book(TimeStampedModel):
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='uploads/books/')
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    author = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)

    objects = BookManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
