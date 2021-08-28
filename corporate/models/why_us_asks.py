from django.db import models


class WhyUsAsks(models.Model):
    title = models.CharField(max_length=120)
    detail = models.CharField(max_length=250) 


    class Meta:
        db_table = 'why_ask'
        verbose_name = 'why_ask'
        verbose_name_plural = 'why_asks'


    def __str__(self):
        return self.title