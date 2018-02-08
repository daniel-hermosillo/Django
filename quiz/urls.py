from django.conf.urls import url

from .views import LanIdRequestView, QuizApplicationView, ResultsApplicationView


urlpatterns = [
    url(r'^$', LanIdRequestView.as_view(), name='request_lanid'),
    url(r'^results/$', ResultsApplicationView.as_view(), name='results'),
    url(r'^do-quiz/(?P<lanid>[a-zA-Z]{1}\d{5})/$', QuizApplicationView.as_view(),
        name='answer_quiz'),
]
