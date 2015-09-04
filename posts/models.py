#encoding=UTF-8

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

VISIBILITY = getattr(settings, 'VISIBILITY', ())
DEFAULT_VISIBILITY = getattr(settings, 'DEFAULT_VISIBILITY', ())

class Category(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()


    def __unicode__(self):
        return self.title


class Post(models.Model):

    owner = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=DEFAULT_VISIBILITY)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    url = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title



