from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.
class  questionmodeltest (TestCase):
    #"was_published_recently with future question test"
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        furture_question = Question(pub_date=time)
        self.assertIs(furture_question.was_published_recently(),False)

    def test_was_published_recently_with_past_question(self):
        time = timezone.now() - datetime.timedelta(days=10)
        past_question = Question(pub_date=time)
        #print('pubdate',past_question.pub_date,'now time=',timezone.now())
        self.assertIs(past_question.was_published_recently(),False)
