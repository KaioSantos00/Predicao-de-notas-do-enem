from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prediction', views.prediction, name='prediction'),
    path('result_prediction', views.result_prediction, name='result_prediction'),
]