from django.urls import path
from . import views

app_name = 'stock_analysis'

urlpatterns = [
    path('',            views.index,  name='index'),
    path('<str:ticker>/', views.detail, name='detail'),
]
