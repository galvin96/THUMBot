from __future__ import unicode_literals

from django.db import models

class FacebookUser(models.Model):
    fbid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    is_female = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.fbid)