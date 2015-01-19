from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Question 
from pollapp.settings import *

# Create your tests here.

class QuestionMethodTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() should return False for question whose 
		pub_date is in the future.
		"""

		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.published_recently(),False)
