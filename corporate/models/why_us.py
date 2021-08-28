from django.db import models

class WhyUs(models.Model):
    header = models.CharField(max_length=55)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/why-us')


    class Meta:
        db_table = 'why_us'
        verbose_name = 'why_us'

