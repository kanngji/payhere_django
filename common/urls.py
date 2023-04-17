from django.urls import path
from . import views
from .views import register
app_name = 'common'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
]