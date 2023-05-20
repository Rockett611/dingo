from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey ('posts.Author', on_delete=models.CASCADE, null=True, blank=True)


class Author(models.Model):
    nick = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nick}, {self.email}"