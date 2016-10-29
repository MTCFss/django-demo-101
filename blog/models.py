from django.db import models
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=40)
    family_name = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.CharField(max_length=400, blank=True)
    phone = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return "%s %s" % (self.name, self.family_name)

class Post(models.Model):
    title = models.CharField(max_length=200)
    contenu = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
