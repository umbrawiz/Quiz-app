"""BTL_CNPM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from questions.views import Question_detail_view, All_question_view, Add_question_view, Update_question_view, Delete_question_view, Category_view, Home_view, Category_create_view
import quiz.views

urlpatterns = [
    path("", Home_view.as_view(), name='home'),
    path("question/list", All_question_view.as_view(), name='question-list'),
    path("question/<int:pk>/", Question_detail_view.as_view(), name='question-detail'),
    path("question/create/", Add_question_view.as_view(), name='question-create'),
    path("question/edit/<int:pk>/", Update_question_view.as_view(), name='question-edit'),
    path("question/delete/<int:pk>/", Delete_question_view.as_view(), name='question-delete'),
    path("category/create/", Category_create_view.as_view(), name='category-create'),
    path("category/<str:cats>/", Category_view, name='category'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/", include('accounts.urls')),
    path('admin/', admin.site.urls),
    path("exam/", quiz.views.QuizListView.as_view(),name = 'exam'),
    path("exam/<int:pk>/", quiz.views.Quiz_detail_view.as_view(), name='exam-detail'),
    path("exam/<int:pk>/data", quiz.views.Quiz_data_view, name='exam-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
