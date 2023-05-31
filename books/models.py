from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey ('books.Author', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tags = models.ManyToManyField("books.Tag", related_name="books")

    def __str__(self):
        return f"{self.title}, {self.author}"


class Author(models.Model):
    full_name = models.CharField(max_length=30)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.full_name}"


class Tag(models.Model):
    word = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.word}"


class BorrowTwo(models.Model):
    book = models.ForeignKey ('books.Book', on_delete=models.CASCADE, null=True, blank=True)
    rental_date = models.DateField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='user')
    is_returned = models.BooleanField()

