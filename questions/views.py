
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Question, Category, MCQ, Answer
from .forms import QuestionModelForm, AnswerFormset, MultiForm, QuestionForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.views.generic.edit import FormView


# Create your views here.
class Home_view(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class All_question_view(ListView):
    model = MCQ
    template_name = 'questions/questionList.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(All_question_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class Question_detail_view(FormView):

    form_class = QuestionForm
    template_name = 'questions/question.html'



class Add_question_view(CreateView):
    template_name = "questions/add_quiz.html"
    form_class = MultiForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Save the user first, because the profile needs a user before it
        # can be saved.
        question = form['question'].save()
        answer = form['answer'].save(commit=False)
        for a in answer:
            a.question = question
        for a in answer:
            a.save()
        return redirect(reverse_lazy('home'))



class Update_question_view(UpdateView):
    model = MCQ
    form_class = MultiForm
    template_name = "questions/edit.html"

    def get_form_kwargs(self):
        kwargs = super(Update_question_view, self).get_form_kwargs()
        kwargs.update(instance={
            'question': self.object,
            'answer': self.object,
        })
        return kwargs

class Delete_question_view(DeleteView):
    model = MCQ
    template_name = "questions/delete.html"
    success_url = reverse_lazy('home')

def Category_view(request, cats):
    category_questions = Question.objects.filter(category = cats)
    return render(request, 'category.html', {'cats':cats.title(), 'category_questions': category_questions})

class Category_create_view(CreateView):
    model = Category
    template_name = "questions/addCategory.html"
    fields = '__all__'


@login_required()
def question_create_view(request, *args, **kwargs):
    form = QuestionModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = QuestionModelForm()
    return render(request, "forms.html", {"form": form})