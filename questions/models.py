from django.db import models
from django.conf import settings
from django.urls import reverse
from quiz.models import Quiz
from datetime import date, datetime
User = settings.AUTH_USER_MODEL
# Create your models here.



ANSWER_ORDER_OPTIONS = (
    ('hold', 'hold'),
    ('random', 'Random')
)

class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
       return self.name

    def get_absolute_url(self):
        #return reverse('question-detail', args=(str(self.pk)))
        return reverse('home')


class Question(models.Model):
    #id = models.AutoField();


    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length= 255, default='')
    question = models.CharField(max_length=255)
    explanation = models.TextField(max_length= 2000, blank=True)
    quiz = models.ManyToManyField(Quiz, blank=True)
    answer_order = models.CharField(
        max_length=30, null=True, blank=True,
        choices=ANSWER_ORDER_OPTIONS,
        help_text="The order in which multichoice \
                        answer options are displayed \
                        to the user",
        verbose_name="Answer Order")

    def __str__(self):
       return self.question + self.category

    def get_absolute_url(self):
        #return reverse('question-detail', args=(str(self.pk)))
        return reverse('home')

    def check_if_correct(self, guess):
        answer = Answer.objects.get(id=guess)

        if answer.correct is True:
            return True
        else:
            return False

    def order_answers(self, queryset):
        if self.answer_order == 'content':
            return queryset.order_by('content')
        # if self.answer_order == 'random':
        #     return queryset.order_by('Random')
        if self.answer_order == 'none':
            return queryset.order_by('None')

    def get_answers(self):
        return self.order_answers(Answer.objects.filter(question=self))

    def get_answers_list(self):
        return [(answer.id, answer.content) for answer in self.order_answers(Answer.objects.filter(question=self))]

    def get_all_answ(self):
        return self.answers.all()

    def answer_choice_to_string(self, guess):
        return Answer.objects.get(id=guess).content

    class Meta:
        verbose_name = "Multiple Choice Question"
        verbose_name_plural = "Multiple Choice Questions"




class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name='Question', on_delete=models.CASCADE,related_name = 'answers')
    test = 1
    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text="Enter the answer text that \
                                            you want displayed",
                               verbose_name="Content")

    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text="Is this a correct answer?",
                                  verbose_name="Correct")


    def __str__(self):
        return self.content


    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
