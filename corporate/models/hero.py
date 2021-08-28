from django.db import models


class HeroSection(models.Model):
    header = models.CharField(max_length=45)
    text = models.CharField(max_length=65)
    link = models.CharField(max_length=60) 
    image = models.ImageField(upload_to='hero-images')


    class Meta:
        db_table = 'header'
        verbose_name = 'header'
        verbose_name_plural = 'headers'


    def __str__(self):
        return self.header
