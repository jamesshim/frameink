from django.urls import path

from . import views

app_name = "frameink"

urlpatterns = [
    path('', views.index, name='index'),
    path('project/', views.project, name='project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/create', views.project_create, name='project_create'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),

    path('project/<int:project_id>/review_create', views.review_create, name='review_create'),

    path('video_list/', views.video_list, name='video_list'),
    path('upload/', views.video_upload, name='video_upload'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('board/', views.board, name='board'),
    path('board/<int:question_id>/', views.detail, name='detail'),
    path('board/answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('board/question/create/', views.question_create, name='question_create'),
]

