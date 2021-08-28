from django.db import models

class TeamMembers(models.Model):
    image = models.ImageField(upload_to='team-images')
    full_name = models.CharField(max_length=40)
    jobs = models.CharField(max_length=25)
    information = models.CharField(max_length=60)
    socialmedia_twitter = models.CharField(max_length=35)
    socialmedia_facebook = models.CharField(max_length=35)
    socialmedia_instagram = models.CharField(max_length=35)
    socialmedia_linkedin = models.CharField(max_length=35)

    class Meta:
        db_table = 'Team Member'
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'


    def __str__(self):
        return self.full_name