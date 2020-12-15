from django.db import models

# Create your models here.


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.TextField(max_length=1000)

    def __str__(self):
        return self.firstname
