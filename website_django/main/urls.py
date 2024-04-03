from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/Login', views.logReg, name='login')
]