from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='register'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('confirm', views.SMSCodeConfirm.as_view(), name='logout'),
]