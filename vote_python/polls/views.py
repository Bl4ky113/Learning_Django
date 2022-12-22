from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.db.models import F

from .models import Question, Choice

class IndexView (generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset (self):
        """
            Return the last five published questions.
            Avoiding the ones published in the future
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by(
            '-pub_date'
        )[:5]

class DetailView (generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

    def get_queryset (self):
        """
            Excludes Questions Posted in the Future.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView (generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index (request):
    # return render(request, 'polls/index.html', {
        # 'latest_question_list': Question.objects.order_by('-pub_date')[:5]
    # })


def about_us (request):
    return HttpResponse('We Are the Patriots')


# def detail_question (request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/details.html', {
        # 'question': question
    # })


# def results_question (request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {
        # 'question': question
    # })


def vote_question (request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        print(request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': 'You didn\'t Select a Correct Choice'
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
