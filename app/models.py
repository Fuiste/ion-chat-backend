from django.db import models
from django.utils import timezone
from custom_user.models import AbstractEmailUser

__author__ = "fuiste"

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(null=False, default=timezone.now())


class Chatter(AbstractEmailUser):
    full_name = models.CharField(max_length=200, null=True, blank=True)
    message_history = models.ManyToManyField('Message', null=True, blank=True)

    class Meta:
        verbose_name = 'Chatter'
        verbose_name_plural = 'Chatters'

    def __unicode__(self):
        return '{0} - {2}'.format(self.full_name, self.email)

    def __str__(self):
        return unicode(self)