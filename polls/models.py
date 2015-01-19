from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	# title = models.CharField(max=30)
	def __unicode__(self):
		return self.question_text

	def published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1)<=self.pub_date <=now
	published_recently.admin_order_field = 'pub_date'
	published_recently.boolean = True
	published_recently.short_description = 'Published recently?'
	
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text