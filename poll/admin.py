from django.contrib import admin
from poll.models import Question, Choice
# Register your models here.
# admin.site.register(Question)
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date','question_text']
	# fieldsets = [
	# ('Question Information', {'fields':['question_text']}),
	# ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
	# ]
	list_display = ('question_text','pub_date','was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
	inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)