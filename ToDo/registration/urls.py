from django.urls import path, include
from .views import *

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='reg'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('', home_window, name='back')

]