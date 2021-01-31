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
