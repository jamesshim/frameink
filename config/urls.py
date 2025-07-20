from django.contrib import admin
from django.urls import path, include
from frameink import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frameink/', include('frameink.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
]
