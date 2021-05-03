from django.contrib import admin

# Register your models here.
from .models import Question, Category, Answer

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    fields = (
        'category',
        'question',
        'explanation',
        'user',
        'quiz',
        'answer_order',
    )

    filter_horizontal = ('quiz',)

    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)