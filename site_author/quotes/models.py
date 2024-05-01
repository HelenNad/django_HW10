from django.db import models

# Create your models here.


class Author(models.Model):
    fullname = models.CharField(max_length=50)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)


class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class AuthorAdd(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class QuoteAdd(models.Model):
    quote = models.CharField(max_length=250, null=False)
    author = models.ForeignKey(AuthorAdd, on_delete=models.CASCADE, default=None, null=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quote}"
