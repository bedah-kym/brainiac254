from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.urls import reverse
from django.contrib import admin
# Create your models here.
STATUS_CHOICES = [
    ('A','active'),
    ('E','ended'),
    ('F','future')
]
class  Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    status = models.CharField(max_length=20,choices= STATUS_CHOICES,default='active')
    sender = models.CharField(max_length=200)

    @admin.display(
        boolean=True,
        ordering = 'pub_date',
        description = 'published recently?'
    )
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        recent = timezone.now() - datetime.timedelta(days=9)
        future = timezone.now() + datetime.timedelta(days=1)
        return self.pub_date >= recent and self.pub_date < future


    @admin.action(description = 'close selected polls ?')
    def end_poll(modeladmin,request,queryset):
        queryset.update(status='E')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text

    def get_absolute_url(self):
        return reverse('polls:home')

class Voteinfo (models.Model):
    poll_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='Empty')
    answer = models.CharField(max_length=200,default='not yet voted')
