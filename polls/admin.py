from django.contrib import admin
from polls.models import Question
# Register your models here.

#Using Fields
# class QuestionAdmin(admin.ModelAdmin):
	# fields=['pub_date','question_text']

#Using Fieldsets
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
				('Question Information', {'fields':['question_text']}),
				('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
	]

admin.site.register(Question,QuestionAdmin)
