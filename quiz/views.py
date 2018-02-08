from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import FormView
from django.contrib import messages

from .forms import QuizFormset, LanIdRequestForm
from .models import Quiz, Question, QuizApplication


class LanIdRequestView(FormView):
    form_class = LanIdRequestForm
    template_name = 'quiz/index.html'

    def get_success_url(self):
        kwargs = {'lanid': self.request.POST.get('lanid')}
        return reverse_lazy('answer_quiz', kwargs=kwargs)


class QuizApplicationView(FormView):
    template_name = 'quiz/quiz_form.html'
    form_class = QuizFormset
    success_url = reverse_lazy('request_lanid')
    lanid = None
    quiz_applications = None

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request,
                             messages.INFO,
                             'Your answers were succesfully saved, thank you!')
        return super(QuizApplicationView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(formset=form))

    def get_context_data(self, **kwargs):
        if 'formset' not in kwargs:
            kwargs['formset'] = self.form_class(queryset=self.quiz_applications)
        return kwargs

    def get_quiz_applications(self):
        quiz, _ = Quiz.objects.get_or_create(lanid=self.lanid)
        for question in Question.objects.all():
            QuizApplication.objects.get_or_create(quiz=quiz, question=question)
        return QuizApplication.objects.filter(quiz=quiz)

    def get(self, request, *args, **kwargs):
        self.lanid = kwargs.get('lanid')
        self.quiz_applications = self.get_quiz_applications()
        formset = self.form_class(queryset=self.quiz_applications)
        options = {'formset': formset, 'lanid': self.lanid}
        return self.render_to_response(self.get_context_data(**options))


@method_decorator(login_required, name='dispatch')
class ResultsApplicationView(ListView):
    model = Question
    template_name = 'quiz/results.html'
