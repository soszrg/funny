from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template.context import Context
from models import Question, Choice
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def home(request):
    try:
        question_all = Question.objects.all()
    except:
        raise Http404("No question")
    
    return render(request, 'polls/home.html', {'questions':question_all})

def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    print q
    cs = get_list_or_404(Choice, question=q)
    print cs
    
    return render(request, 'polls/detail.html', {'question':q, 'choices':cs})

def results(request, question_id):
    cs = Quest
    return HttpResponse("You want [%s] question result" %question_id)

def vote(request, question_id):
    choice_id = request.POST.get('choice', None)
    c = get_object_or_404(Choice, pk=int(choice_id))
    c.votes += 1
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))