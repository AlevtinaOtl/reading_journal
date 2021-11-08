from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=150)
    author = models.CharField('Author', max_length=100)
    year = models.PositiveSmallIntegerField('Year of publishing', default=date.today)
    description = models.TextField('Annotation', blank=True)
    review = models.TextField('My review', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
