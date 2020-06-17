from django.db import models
from django.urls import reverse

# Create your models here.

class Invoice(models.Model):
    first_name = models.CharField('First Name',max_length=256)
    last_name = models.CharField('Last Name',max_length=256)

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('list_invoice',)
