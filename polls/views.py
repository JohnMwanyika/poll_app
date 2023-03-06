from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question


# Create your views here.
def index(req):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = '<br>'.join([q.question_text for q in latest_question_list])

    return render(req, 'polls/index.html',{'latest_question_list':latest_question_list})


def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(req, 'polls/detail.html',{'question':question})


def results(req, question_id):
    res = "You are looking at the results of question %s."
    return HttpResponse(res % question_id)


def vote(req, question_id):
    res = "You're voting on question %s."
    return HttpResponse(res % question_id)