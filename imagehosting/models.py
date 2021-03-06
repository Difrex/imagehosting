# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from django.db import models


class Post(models.Model):
    """ Model for image
    """
    name = models.CharField(max_length=30, blank=True)
    file = models.ImageField(upload_to='images')

    def __unicode__(self):
        return self.name

    @property
    def orig_name(self):
        return os.path.split(self.file.name)[-1]

    @property
    def thumb_name(self):
        return '/thumb_' + self.orig_name

    def delete(self, *args, **kwargs):
        """ Delete file from disc along with record in database
        """
        # get file data
        storage, path = self.file.storage, self.file.path
        # delete model object
        super(Post, self).delete(*args, **kwargs)
        # delete files
        storage.delete(path)
        storage.delete("/thumb_".join(os.path.split(path)))
