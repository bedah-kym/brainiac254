from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class  Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        recent = timezone.now() - datetime.timedelta(days=9)
        future = timezone.now() + datetime.timedelta(days=1)
        return self.pub_date >= recent and self.pub_date < future

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def get_absolute_url(self):
        return reverse('polls:home')
