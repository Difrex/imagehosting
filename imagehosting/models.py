# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import os


class Post(models.Model):
    name = models.CharField(max_length=30, blank=True)
    file = models.FileField(upload_to='images')

    def __unicode__(self):
        return self.name

    def thumb_name(self):
        x = os.path.split(self.file.name)[-1]
        return '/thumb_' + x

    thumb_name = property(thumb_name)

    def orig_name(self):
        x = os.path.split(self.file.name)[-1]
        return x

    orig_name = property(orig_name)

    def delete(self, *args, **kwargs):
        # get file data
        storage, path = self.file.storage, self.file.path
        # delete model object
        super(Post, self).delete(*args, **kwargs)
        # delete files
        storage.delete(path)
        storage.delete("/thumb_".join(os.path.split(path)))
