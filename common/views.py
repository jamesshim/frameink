from django.contrib.auth import logout
from django.shortcuts import render, redirect

from common.forms import UserForm


def logout_view(request):
    logout(request)
    return redirect('index')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # 관리자 승인 전까지 로그인 불가
            user.save()
            # 사용자에게 승인 대기 메시지 보여주기
            return render(request, 'common/signup_pending.html')  # 새 템플릿 필요
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


