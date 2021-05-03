from betterforms.multiform import MultiModelForm
from django import forms
from django.contrib import admin
from django.forms import RadioSelect

from .models import Question, Category, Answer
from django.forms.models import inlineformset_factory
from six import python_2_unicode_compatible

AnswerFormset = inlineformset_factory(Question, Answer,
                                      fields=['content', 'correct', ], extra=4)

class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        choices = Category.objects.all().values_list('name', 'name')

        choice_list = []
        for item in choices:
            choice_list.append(item)
        fields = [
            'category',
            'question',
            'explanation',
            'user',
            'answer_order',
        ]
        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your question'}),
            'explanation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Explanation'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }


class   QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)

class MultiForm(MultiModelForm):
    form_classes = {
        'question': QuestionModelForm,
        'answer': AnswerFormset,
    }
