from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.shortcuts import get_list_or_404
from .models import Question,Choice
from django.urls import reverse
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView
# Create your views here.

class homeview(ListView):
    model = Question
    template_name = "polls/index.html"
    context_object_name='questions'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]
    def get_total(self):
        pass

class details(DetailView):
    model = Question
    template_name = "polls/details.html"
    context_object_name='q'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class result(DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name='q'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class newchoice(CreateView):
    model = Choice
    fields = ['question','choice_text']


class deletenewpoll(DeleteView):
    model = Question
    success_url = reverse_lazy('polls:home')

def vote(request,question_id):
    q = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
        if selected_choice not in q.choice_set.all():
            return render(request,"polls/details.html",{"error_message":"your choice is invalid"})
        else:
            selected_choice.votes+=1
            selected_choice.save()

    except KeyError:
        return HttpResponseRedirect(reverse('polls:detail', args=(q.id,){}))

    return HttpResponseRedirect(reverse('polls:result', args=(q.id,)))
