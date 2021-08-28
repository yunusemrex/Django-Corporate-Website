from django.db import models
from ckeditor.fields import RichTextField


class Pricing(models.Model):
    plan_name = models.CharField(max_length=35)
    price = models.IntegerField()
    detail1 = models.CharField(max_length=50)
    detail2= models.CharField(max_length=50)
    detail3 = models.CharField(max_length=50)
    detail4 = models.CharField(max_length=50)
    detail5 = models.CharField(max_length=50)



    class Meta:
        db_table = 'Pricing'
        verbose_name = 'Pricing'
        verbose_name_plural = 'Prices'

    def __str__(self):
        return self.plan_name