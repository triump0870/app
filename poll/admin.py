from django.contrib import admin
from poll.models import Question
# Register your models here.
# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date','question_text']
	fieldset = [
	(None, {'fields':['question_text']}),
	('Date Information',{'fields':['pub_date']}),
	]

admin.site.register(Question,QuestionAdmin)