from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice

# def index (request):
    # return render(request, 'polls/index.html', {
        # 'latest_question_list': Question.objects.order_by('-pub_date')[:5]
    # })


# def about_us (request):
    # return HttpResponse('We Are the Patriots')


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
