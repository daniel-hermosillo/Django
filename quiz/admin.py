from django.contrib import admin

from .models import Question, QuizApplication, Quiz, Answer


class QuizApplicationAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'quiz', 'updated_at']
    list_filter = ['answer', 'question', 'quiz', 'updated_at']


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizApplication, QuizApplicationAdmin)
admin.site.register(Quiz)
