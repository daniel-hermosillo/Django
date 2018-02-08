from django.template import Library

from ..models import Question, QuizApplication

register = Library()

@register.simple_tag
def get_question(question_field):
    question = Question.objects.get(pk=question_field.value())
    return question

@register.simple_tag
def get_answer_count(question, answer):
    return QuizApplication.objects.filter(question=question, answer=answer).count()

@register.simple_tag
def get_open_answers(question):
    return QuizApplication.objects.filter(question=question)
