from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView,DetailView
from django.http import JsonResponse
import random
# Create your views here.

class QuizListView(ListView):
    model = Quiz
    template_name = 'exams/main.html'

class Quiz_detail_view(DetailView):
    model = Quiz
    template_name = 'exams/exam.html'

def Quiz_data_view(request,pk):
    exam = Quiz.objects.get(pk=pk)
    questions = []
    all_answer = []
    for q in exam.get_questions():
        ans = q.get_answers_list()
        all_answer.append(ans)
        questions.append(q)
    random.shuffle(questions)
    return render(request, 'exams/exam_data.html', {'data':questions , 'data_value': all_answer})


