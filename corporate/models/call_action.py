from django.db import models

class CallAction(models.Model):
    call_action_title = models.CharField(max_length=50)
    call_action_text = models.CharField(max_length=75)

    class Meta:
        db_table = 'call_action'
        verbose_name = 'call_action'
        verbose_name_plural = 'call_actions'

    def __str__(self):
        return self.call_action_title

