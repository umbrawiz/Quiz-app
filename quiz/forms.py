from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# Register your models here.
from .models import Quiz
from questions.models import Question, MCQ
from django.utils.translation import ugettext_lazy as _

class QuizModelForm(forms.ModelForm):
    """
        below is from
        http://stackoverflow.com/questions/11657682/
        django-admin-interface-using-horizontal-filter-with-
        inline-manytomany-field
    """

    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(
            verbose_name=_("Questions"),
            is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(QuizModelForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = \
                self.instance.question_set.all().select_subclasses()

    def save(self, commit=True):
        quiz = super(QuizModelForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz

class QuizForms(forms.ModelAdmin):
    form = QuizModelForm

    list_display = ('title', 'category', )
    list_filter = ('category',)
    search_fields = ('description', 'category', )