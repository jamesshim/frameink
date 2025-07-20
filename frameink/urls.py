from django.urls import path

from . import views

app_name = "frameink"

urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.board, name='board'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]
