from django.conf.urls import url
from django.contrib.auth import views

app_name = 'account'

urlpatterns = [
    url('login', views.LoginView.as_view(template_name='login.html'), name='login'),
    url('logout', views.LogoutView.as_view(), name='logout'),
]
