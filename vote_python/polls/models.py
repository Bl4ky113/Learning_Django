
import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

class Question (models.Model):
    text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently (self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=5)

    def __str__ (self):
        return str(self.text)


class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)

    def __str__ (self):
        return str(self.text)
