from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT
from django.urls import reverse

class Book(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='available') 
    lent_to = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)


    def __str__(self):
        return f'{self.author} - {self.title}' 

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})

