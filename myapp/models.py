from django.contrib.auth.models import User
from django.db import models
import os
from django.conf import settings


def user_profile_image_path( instance, filename ):
    return os.path.join( settings.STATIC_URL)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=140, blank=True, null=True)
    phonenumber = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=140, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='static/images/user/', null=True, blank=True)

    class Meta:
        db_table = "user_profile"

    def __unicode__(self):
        return u'Profile of user: {0!s}'.format(self.user.username)


