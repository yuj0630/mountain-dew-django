#account/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
app_name = "users"
urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
  path('signup/', signup, name='signup'),# 수정해야하는 코드
  # django.contrib.auth앱의 LoginView 클래스를 활용했으므로 별도의 views.py 파일 수정이 필요 없음
]