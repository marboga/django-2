from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Interest(models.Model):
    name = models.TextField(max_length=40)
    created_at = models.DateTimeField(datetime.now())
    class Meta:
        db_table = 'interests'

class User(models.Model):
    first_name = models.TextField(max_length=40)
    last_name = models.TextField(max_length=40)
    age = models.IntegerField()
    created_at = models.DateTimeField(datetime.now())
    occupation = models.TextField(max_length=40)
    interest = models.ForeignKey(interests)
    class Meta:
        db_table = 'users'
