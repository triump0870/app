from django.contrib import admin
from poll.models import Question
# Register your models here.
# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date','question_text']
	fieldsets = [
	('Question Information', {'fields':['question_text']}),
	('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
	]

admin.site.register(Question,QuestionAdmin)