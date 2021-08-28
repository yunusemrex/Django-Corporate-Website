from django.db import models
from ckeditor.fields import RichTextField


class Pages(models.Model):
    title = models.CharField(max_length=250)
    content = RichTextField()
    detail = models.CharField(max_length=250)
    image = models.ImageField(upload_to='page-images')


    class Meta:
        db_table = 'Main_pages'
        verbose_name = 'Main_page'
        verbose_name_plural = 'Main_pages'

    def __str__(self):
        return self.title 