from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import ProjectForm, ReviewForm, QuestionForm, AnswerForm, VideoForm
from .models import Question
from .models import Video, Project


def index(request):
    return render(request, 'frameink/home.html')


def project(request):
    project_list = Project.objects.all().order_by('name')
    return render(request, 'frameink/project.html', {'project_list': project_list})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'frameink/project_detail.html', {'project': project})


def project_create(request):
    project_list = Project.objects.all()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frameink:project')
    else:
        form = ProjectForm()

    return render(request, 'frameink/project.html', {'form': form, 'project_list': project_list, })


@require_POST
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('frameink:project')


def review_create(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.save()
            return redirect('frameink:project_detail', project_id=project.id)
    else:
        form = ReviewForm()
    return render(request, 'frameink/project_detail.html', {'form': form, 'project': project, })


def video_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'video_upload.html', {'form': form})


def video_list(request):
    videos = Video.objects.all().order_by('-uploaded_at')
    return render(request, 'video_list.html', {'videos': videos})


def video_detail(request, pk):
    video = Video.objects.get(pk=pk)
    return render(request, 'video_detail.html', {'video': video})


def board(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'frameink/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'frameink/question_detail.html', context)


@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('frameink:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'frameink/question_detail.html', context)


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('frameink:board')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'frameink/question_form.html', context)
