from django.db import models
from django.utils import timezone
# Create your models here.

class FeeItem(models.Model):
    payid = models.IntegerField()
    name = models.CharField(max_length=64, verbose_name='FeeName')
    fee = models.IntegerField()
    paydate = models.DateTimeField(auto_now_add=True, verbose_name='Paydate')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.CharField(max_length=500, null=True, verbose_name='desc')
    content = models.CharField(max_length=800, verbose_name='Content')
    def __str__(self):
        return self.title
