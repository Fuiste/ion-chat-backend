from django.db import models
from django.utils import timezone
from custom_user.models import AbstractEmailUser

__author__ = "fuiste"

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=1000, null=True, blank=True)
    msg_from = models.ForeignKey('Chatter', related_name='msg_from', null=True, blank=True)
    msg_to = models.ForeignKey('Chatter', related_name='msg_to', null=True, blank=True)
    created_at = models.DateTimeField(null=False, default=timezone.now())


class Chatter(AbstractEmailUser):
    NO_TOKEN = "no token"
    TOKEN_IOS = "ios"
    TOKEN_ANDROID = "android"

    full_name = models.CharField(max_length=200, null=True, blank=True)
    imgur_url = models.CharField(max_length=400, null=False, default="http://i.imgur.com/23el4Y8.jpg")
    device_token = models.CharField(max_length=400, null=False, default=NO_TOKEN)
    device_type = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = 'Chatter'
        verbose_name_plural = 'Chatters'

    def __unicode__(self):
        return '{0} - {1}'.format(self.full_name, self.email)

    def __str__(self):
        return unicode(self)