from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question,Choice


# Create your views here.
# def index(req):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # output = '<br>'.join([q.question_text for q in latest_question_list])
#     context = {'latest_question_list':latest_question_list}
#     return render(req, 'polls/index.html',context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # returns the last 5 published questions
        return Question.objects.order_by('-pub_date')[:5]


# def detail(req, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(req, 'polls/detail.html',{'question':question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def results(req, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(req, 'polls/results.html',{'question':question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(req, question_id):
    question = get_object_or_404(Question,pk=question_id)
    print(question)
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
        print(req.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(req,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice."
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # return HttpResponseRedirect(reverse('polls:results',args=[question.id]))
        return redirect('polls:results',question.id)
