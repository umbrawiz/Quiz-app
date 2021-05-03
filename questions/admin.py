from django.contrib import admin

# Register your models here.
from .models import Question, Category, MCQ, Answer

class AnswerInline(admin.TabularInline):
    model = Answer

class MCQuestionAdmin(admin.ModelAdmin):
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

admin.site.register(MCQ, MCQuestionAdmin)
admin.site.register(Category)