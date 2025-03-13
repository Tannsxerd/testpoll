from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(private = False)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def listvote(request):
    votelevel  = []
    Question_ls = Question.objects.all()

    for q_id in Question_ls:
        sum = 0
        choice_ls = Choice.objects.filter(question = q_id)
        print(choice_ls)
        for choice in choice_ls:
            print(choice.votes)
            sum += choice.votes
        if (sum > 10 and sum <50):
            votelevel.append({f"{q_id}": "warm"})
        elif (sum) > 50:
            votelevel.append({f"{q_id}": "hot"})
        print(votelevel)

    return render(request,"polls/votelevel.html",context = {"question_ls" : Question_ls,
                                                           "vote_ls": votelevel})   
    
def private_view(request):
    private_obj= Question.objects.all()
    private_ls = []
    for q in private_obj:
        if q.private :
            private_ls.append(q)

    return  render(request,"polls/private_page.html",context = {"private_list": private_ls } )
