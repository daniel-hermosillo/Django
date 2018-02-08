from django.db import models


class Quiz(models.Model):
    lanid = models.CharField(max_length=7)

    def __str__(self):
        return '{}'.format(self.lanid)


class Answer(models.Model):
    text = models.CharField(max_length=250)
    counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.text)


class Question(models.Model):
    text = models.CharField(max_length=250)
    possible_answers = models.ManyToManyField(Answer, blank=True)

    def __str__(self):
        return '{}'.format(self.text)


class QuizApplication(models.Model):
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer, null=True, blank=True)
    quiz = models.ForeignKey(Quiz)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.question, self.answer)
