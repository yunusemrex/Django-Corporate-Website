from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=50)


    class Meta:
        db_table = 'Service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


    def __str__(self):
        return self.title

