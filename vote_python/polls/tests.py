import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice

def create_question (question_text='test_question', days_difference=0):
    question_time = timezone.now() + datetime.timedelta(days=days_difference)

    return Question.objects.create(text=question_text, pub_date=question_time)

class QuestionModelTests (TestCase):

    def test_was_published_recently_with_future_questions (self):
        """
            was_published_recently() returns False for Questions
            whose pub_date is in the future
        """
        test_time = timezone.now() + datetime.timedelta(days=10)

        future_question = Question(text='Future Question', pub_date=test_time)

        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_recent_questions (self):
        """
            was_published_recently() returns True for Questions
            whose pub_date is in the recent past (less than 5 days)
        """
        test_time = timezone.now() - datetime.timedelta(days=1)

        recent_question = Question(text='Recent Question', pub_date=test_time)

        self.assertTrue(recent_question.was_published_recently())


class QuestionIndexViewTests (TestCase):

    def test_no_questions (self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question (self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days_difference=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question (self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days_difference=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question (self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days_difference=-30)
        create_question(question_text="Future question.", days_difference=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_questions (self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days_difference=-30)
        question2 = create_question(question_text="Past question 2.", days_difference=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )

class QuestionDetailViewTests (TestCase):
    def test_future_question (self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days_difference=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question (self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days_difference=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.text)
