from django.shortcuts import render,get_object_or_404
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.template import loader

# def index(request):
#     latest_question_list=Question.objects.order_by('-pub_date')
#     template=loader.get_template('vote/index.html')
#     context={
#         'latest_question_list':latest_question_list,
#     }
#     return HttpResponse(template.render(context,request))
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'vote/index.html', context)

def detail(request,question_id):
    return HttpResponse("hello,you are looking at question%s."%question_id)

def results(request,question_id):
    response="You are looking at the result of quetestoin%s."
    return HttpResponse(response%question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)