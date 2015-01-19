from django.contrib import admin
from polls.models import Question,Choice
# Register your models here.

#Inline Choice Objects
# class ChoiceInline(admin.StackedInline):
# 	model = Choice
# 	extra = 3

#Tabular Choice Objects
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

#Using Fields
# class QuestionAdmin(admin.ModelAdmin):
	# fields=['pub_date','question_text']

#Using Fieldsets
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text','pub_date','published_recently')
	fieldsets = [
				('Question Information', {'fields':['question_text']}),
				('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
