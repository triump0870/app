from django.shortcuts import get_object_or_404, render
# from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question,Choice
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.

# ********First Index function***********
# def index(request):
# 	# return HttpResponse("Hello, world. You're at the polls index.")
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = RequestContext(request, {
# 		'latest_question_list':latest_question_list,
# 		})
# 	# output = ', '.join([p.question_text for p in latest_question_list])
# 	# return HttpResponse(output)
# 	return HttpResponse(template.render(context))

# *******Second Index function***********
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	context = {'latest_question_list':latest_question_list}
# 	return render(request,'polls/index.html',context)

# ********Third index view***********
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		"""Return the latest five published question."""
		return Question.objects.order_by('-pub_date')[:5]

# *******First detail function***********
# def detail(request, question_id):
	# return HttpResponse("You're looking at question %s."%question_id)

# *******Second detail function**********
# def detail(request,question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404
# 	return render(request,'polls/detail.html',{'question':question})

# ******Third detail function************
# def detail(request,question_id):
# 	question = get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/detail.html',{'question':question})
	
# *******Fourth detail view***********
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

# *******First result view******	
# def results(request,question_id):
# 	# response = "You're looking at the results of question %s."
# 	# return HttpResponse(response % question_id)
# 	question = get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/results.html',{'question':question})

# ********Second result view*********
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

# *******First vote view*********
def vote(request,question_id):
	# return HttpResponse("You're voting on question %s."%question_id)
	p=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redislay the question voting form
		return render(request,'polls/detail.html',{
			'question':p,
			'error_message':"You didn't select a choice.",
			})
	else:
		selected_choice.votes+= 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a 
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))


