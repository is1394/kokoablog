from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.id, self.title)
