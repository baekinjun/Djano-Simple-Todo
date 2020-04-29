from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic

from .models import Question
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'jun/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'jun/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'jun/results.html'

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    return render(request , 'jun/index.html',{'latest_question_list': latest_question_list})

def detail(request,question_id):
    q = get_object_or_404(Question, pk = question_id)
    return render(request, 'jun/detail.html',{'question':q})

def results(request, question_id):
    question = get_object_or_404(Question , pk = question_id)
    return render(request, 'jun/results.html', {'question' : question})

def vote(request , question_id):
    question = get_object_or_404(Question , pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request,'jun/detail.html',{
            'question' : question,
            'error message' : "you didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('jun/results' , question_id = question.id)



