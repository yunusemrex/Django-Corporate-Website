from django.db import models
from ckeditor.fields import RichTextField


class AboutDetail(models.Model):
    title = RichTextField(blank=True, null=True)
    detail = models.CharField(max_length=40)


class AboutText(models.Model):
    content = RichTextField()