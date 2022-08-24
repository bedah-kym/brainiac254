from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.shortcuts import get_list_or_404
from .models import Question,Choice
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView
# Create your views here.

class homeview(ListView):
    model = Question
    template_name = "polls/index.html"
    context_object_name='questions'
    ordering = ['-pub_date']


class details(DetailView):
    model = Question
    template_name = "polls/details.html"
    context_object_name='q'

class result(DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name='q'

class newchoice(CreateView):
    model = Choice
    fields = ['question','choice_text']


class deletenewpoll(DeleteView):
    model = Question
    success_url = reverse_lazy('polls:home')

def vote(request,question_id):
    q = get_object_or_404(Question,pk=question_id)
    selected_choice = q.choice_set.get(pk=request.POST['choice'])
    if selected_choice not in q.choice_set.all():
        return render(request,"polls/details.html",{"error_message":"your choice is invalid"})
    else:
        selected_choice.votes+=1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:result', args=(q.id,)))
