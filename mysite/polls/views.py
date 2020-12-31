from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list]) # --> output without having index.html file
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
    
def detail(request, question_id):
    '''
    # this can be done or use get_object_or_404 shortcut for the same
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    ''' 
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = 'you are looking at results for %s.'
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("Voting for question %s" %question_id)