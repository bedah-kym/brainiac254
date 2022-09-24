from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.shortcuts import get_list_or_404
from .models import Question,Choice,Voteinfo
from django.urls import reverse
from django.http import Http404
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class homeview(ListView):
    model = Question
    template_name = "polls/index.html"
    context_object_name='questions'
    paginate_by = 2

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    def get_total(self):
        pass
"""
class details(DetailView):
    model = Question
    template_name = "polls/details.html"
    context_object_name='q'

    def get_queryset(self):
        try:
            poll=Question.objects.filter(pub_date__lte=timezone.now(),status='active')
        except 404 :
            return render(request,"polls/result.html",{"error_message":"your choice is invalid"})
"""

def details(request,question_id):
    q = get_object_or_404(Question,pk=question_id,)
    context= {
        "error_message":"voting is closed",
        "q":q,
    }
    if request.user.is_authenticated:
        if q.status == 'A':
            return render(request,"polls/details.html",context)
        elif q.status == 'E':
            return render(request,"polls/results.html",context)
        else:
            raise Http404('wrong poll status')
    else:
        context= {
            "not_auth":"Please log in or create an account first"
        }
        return render(request,"polls/details.html",context)

class result(DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name='q'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class deletenewpoll(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Question
    success_url = reverse_lazy('polls:home')

    def test_func(self):
        poll= self.object.get()
        if self.request.user == poll.author :
            return True
        return False

def vote(request,question_id):
    q = get_object_or_404(Question,pk=question_id,)
    voter = request.user
    error_message=""
    try:
        selected_choice = q.choice_set.get(pk=request.POST.get(['choice']))
        if selected_choice in q.choice_set.all():
            if Voteinfo.objects.filter(name=voter,poll_text=q).exists():
                error_message="you have already voted"
            else:
                new=Voteinfo.objects.create(
                poll_text=q,
                name = voter ,
                answer = selected_choice
                )
                selected_choice.votes+=1
                selected_choice.save()
        else:
            error_message="your choice is invalid"

    except KeyError:
        return HttpResponseRedirect(reverse('polls:detail', args=(q.id,)))

    return render(request,'polls/results.html',{"error_message":error_message})
