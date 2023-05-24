from django.urls import path
from . import views

urlpatterns = [
    path('', views.prever_notas, name='index'),
    path('fazer_predicao', views.fazer_predicao, name='realizar_predicao'),
    path('novoform', views.novoform, name='novoform'),
]