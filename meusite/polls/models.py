import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Question Model"""
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('data da publicação')

    def was_publish_recently(self) -> bool:
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """Choice Model"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
