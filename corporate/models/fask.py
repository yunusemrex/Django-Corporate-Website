from django.db import models


class Asks(models.Model):   
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=250) 


    class Meta:
        db_table = 'Frequently_ask'
        verbose_name = 'Frequently_ask'
        verbose_name_plural = 'Frequently_asks'

    def __str__(self):
        return self.title
