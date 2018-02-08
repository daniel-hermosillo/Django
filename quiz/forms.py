from django.forms import (
    CharField, Form, ModelForm, RadioSelect, modelformset_factory
)
from django.core.validators import RegexValidator
from django.core.exceptions import ObjectDoesNotExist

from .models import Answer, Question, QuizApplication


class QuizApplicationForm(ModelForm):
    answer_text = CharField(required=False)

    class Meta:
        model = QuizApplication
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(QuizApplicationForm, self).__init__(*args, **kwargs)
        question = Question.objects.get(pk=self.initial['question'])
        self.fields['answer'].widget = RadioSelect()
        qs = question.possible_answers.all()
        if not qs:
            self.fields['answer_text'].initial = getattr(self.instance, 'answer')
        self.fields['answer'].queryset = qs or self.fields['answer'].queryset

    def clean(self):
        super_clean = super(QuizApplicationForm, self).clean()
        answer_text = self.cleaned_data['answer_text']
        if not self.cleaned_data.get('answer') or answer_text:
            try:
                answer = Answer.objects.get(text__iexact=answer_text)
            except ObjectDoesNotExist as e:
                answer = Answer.objects.create(text=answer_text)

            answer.counter += 1
            self.cleaned_data['answer'] = answer
            answer.save()
        self.cleaned_data.pop('answer_text')
        return super_clean


QuizFormset = modelformset_factory(QuizApplication,
                                   form=QuizApplicationForm,
                                   extra=0)


class LanIdRequestForm(Form):
    lanid = CharField(max_length=6, min_length=6,
                      validators=[RegexValidator(regex='[a-zA-Z]{1}\\d{5}')])
